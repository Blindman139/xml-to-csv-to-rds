import boto3
import pymysql
import pymysql.cursors
import csv
import json
from helper import *


def getDBCredentials(bucket: str, dbCredFileKey: str, s3) -> dict:
    """It will fetch credentials to connect with Amazon RDS MySql DB

    Args:
        bucket (str): bucket name
        dbCredFileKey (str): credential s3 file key
        s3 : boto3 s3 resource

    Returns:
        dict: dictionary with DB credentials
    """
    try:
        credStr = readFileContentFromS3(bucket, dbCredFileKey, s3)
        return json.loads(credStr)
    except Exception as e:
        raise (createErrorStr("fetching DB credentials from s3", e))


def connectToDatabase(dbCredentials: dict) -> pymysql.connections.Connection:
    """It will connect to data base and will return connection object

    Args:
        dbCredentials (dict): DB credential

    Returns:
        pymysql.connections.Connection: DB connection object
    """
    try:
        _connection = pymysql.connect(
            host=dbCredentials['host'],
            db=dbCredentials['db'],
            user=dbCredentials['username'],
            passwd=dbCredentials['password'],
            port=dbCredentials['port']
        )
        return _connection
    except Exception as e:
        raise (createErrorStr("connecting to DB", e))


def closeConnection(con: pymysql.connections.Connection) -> None:
    """To safely close connection

    Args:
        con (pymysql.connections.Connection): possible connection object
    """
    try:
        if con:
            con.close()
    except Exception as e:
        raise (createErrorStr("closing DB connection", e))


# read csv to tuple
# create sel query to insert statements


def readCSVFile(bucket: str, fileKey: str, s3) -> list[tuple]:
    """read csv file from s3 bucket to list of tuple

    Args:
        bucket (str): name
        fileKey (str): key name
        s3 (_type_): boto3 s3 object

    Returns:
        list[tuple]: list of csv row tuples
    """
    try:
        fileContent = readFileContentFromS3(bucket, fileKey, s3)
        fileContent = fileContent.splitlines()
        fileContent = fileContent[1:]  # remove header row
        reader = csv.reader(fileContent)
        rows = []
        for row in reader:
            rows.append(tuple(row))
        return rows

    except Exception as e:
        raise (createErrorStr("reading csv file from s3", e))


def CSVToRDS(bucket: str, csvFileKey: str) -> None:
    """Entry point to convert CSV and store to RDS

    Args:
        bucket (str): name
        csvFileKey (str): file key
    """
    try:
        s3 = boto3.resource('s3')

        # read csv from s3 to list[tuple]
        csvData = readCSVFile(bucket, csvFileKey, s3)

        # remove brackets and create into (,,,),(,,,)... format
        insertRowData = str(csvData)[1:-1]

        dbCredFileKey = 'dbCredentials.json'
        dbCredentials = getDBCredentials(bucket, dbCredFileKey, s3)
        # get db connection created
        con = connectToDatabase(dbCredentials)

        # create cursor
        cur: pymysql.cursors.Cursor = con.cursor()

        # Insert query
        query = """
            INSERT INTO books values
            {insertRowData}
        """

        query = query.format(insertRowData=insertRowData)
        # print(query)
        cur.execute(query)
        con.commit()
        closeConnection(con)
        deleteFile(bucket, csvFileKey, s3)

    except Exception as e:
        closeConnection(con)
        raise (createErrorStr("converting CSV to RDS", e))
