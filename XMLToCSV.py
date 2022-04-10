import boto3
import xml.etree.ElementTree as ET
import pandas
import config
import re
from helper import *


def XMLStringToXML_ET(xmlString: str) -> ET.Element:
    # This will be used to convert XML content from String to Element
    """To convert XML String to XML Element

    Args:
        xmlString (str): XML file content in string format

    Raises:
        f: Custom Error

    Returns:
        ET.Element: XML Element Object
    """
    try:
        return ET.fromstring(xmlString)
    except Exception as e:
        raise createErrorStr("converting XML string to XML Element", e)


def XMLElementToRows(xmlElement: ET.Element) -> list[dict]:
    # This will be used to convert XML Element to array of rows
    """To convert XML Element to List of rows

    Args:
        xmlElement (ET.Element): XLM Element to convert

    Raises:
        f: Custom error

    Returns:
        list[dict]: list of rows
    """
    try:
        rows = []
        # iterate over all sub element of roor xmlObject and create rows for each data
        for element in xmlElement:
            element: ET.Element
            id = element.attrib['id']
            author = element.find('author').text
            title = element.find('title').text
            genre = element.find('genre').text
            price = element.find('price').text
            publish_date = element.find('publish_date').text
            description = re.sub(
                "\s\s+", " ", element.find('description').text)
            rows.append({
                "id": id,
                "author": author,
                "title": title,
                "genre": genre,
                "price": price,
                "publish_date": publish_date,
                "description": description
            })
        return rows
    except Exception as e:
        raise createErrorStr("converting XML Element to Rows", e)


def rowsToDF(rows: list[dict], columnHeader: list[str]) -> pandas.DataFrame:
    # Will be used to covnert list of row to pandas dataframe
    """To covert Rows to pandas DataFrame

    Args:
        rows (list[dict]): List of all rows
        columnHeader (list[str]): Column headers to use

    Raises:
        f: Custom Error

    Returns:
        pandas.DataFrame: Dataframe converted from rows
    """
    try:
        return pandas.DataFrame(rows, columns=columnHeader)
    except Exception as e:
        raise createErrorStr("converting Rows to pandas DataFrame", e)


def DFToCSV(DF: pandas.DataFrame) -> str:
    """To convert pandas DF to CSV string

    Args:
        DF (pandas.DataFrame): pandas DF

    Returns:
        str: CSV string
    """
    # Will be used to convert pandas DF to CSV File
    try:
        return DF.to_csv(index=False)
    except Exception as e:
        raise createErrorStr("converting pandas DataFrame to CSV", e)


def XMLToCSV(bucket: str, XMLfileKey: str) -> None:
    """Entry point of XML to CSV conversion

    Args:
        bucket (str): name
        XMLfileKey (str): key

    """
    try:
        s3 = boto3.resource('s3')

        # Read XML file to string
        xmlStr = str(readFileContentFromS3(bucket, XMLfileKey, s3))
        # print(xmlStr)
        # XML File content to XML ElementTree
        xmlElement = XMLStringToXML_ET(xmlStr)
        # Array of rows
        rows = XMLElementToRows(xmlElement)
        # pandas dataframe
        df = rowsToDF(rows, config.tableColumns)
        # DF to CSV Str
        csvStr = DFToCSV(df)
        csvStr = re.sub('\n\n+', "", csvStr)
        # save CSV file
        csvFileKey: str = XMLfileKey[:-3]+'csv'  # change extension
        csvFileKey = csvFileKey.replace('XML/', 'CSV/')  # change Folder

        writeFileContentToS3(csvStr, bucket, csvFileKey, s3)

        # delete source xml file
        deleteFile(bucket, XMLfileKey, s3)
    except Exception as e:
        raise createErrorStr("converting XML to CSV", e)
