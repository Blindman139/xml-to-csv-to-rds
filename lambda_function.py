from helper import *
import XMLToCSV
import CSVToRDS


def lambda_handler(event, context):
    """Entry point of lambda function.
        This will first check for input file folder and it's type.
        And then it will invoke function accordingly.

    Args:
        event (dict): It will contain event data of s3 put action in specific bucket
        context (dict): Not Used
    """
    try:
        # check input file type and name and proceed accordingly
        # finds triggering bucket and filekey
        bucket = event["Records"][0]["s3"]["bucket"]["name"]
        fileKey = event["Records"][0]["s3"]["object"]["key"]

        notValidFileFlag = True
        # check if file was in CSV folder or XML Folder
        if fileKey.find("XML/") != -1:
            # file inside XML folder for XML->CSV
            # check for file extension
            if checkExtension(fileKey, '.xml'):
                notValidFileFlag = False
                print("Starting XML to CSV Conversion...")
                XMLToCSV.XMLToCSV(bucket, fileKey)
                print("XML to CSV Conversion Successful.")

        elif fileKey.find("CSV/") != -1:
            # file inside CSV folder for CSV->RDS
            # check for file extension
            if checkExtension(fileKey, '.csv'):
                notValidFileFlag = False
                print("Starting CSV to RDS Conversion...")
                CSVToRDS.CSVToRDS(bucket, fileKey)
                print("CSV to RDS Conversion Successful.")

        if notValidFileFlag:
            print(f"Not valid file - {fileKey}")
            return

    except Exception as e:
        print(e)
        print("----------------------------")
        print(f"Error while running on file {fileKey}")
