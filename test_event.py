CSV_PUT = {
    "Records": [
        {
            "eventVersion": "2.1",
            "eventSource": "aws:s3",
            "awsRegion": "ap-south-1",
            "eventTime": "2022-04-05T17:10:45.364Z",
            "eventName": "ObjectCreated:Put",
            "userIdentity": {
                "principalId": "A2U50U9G980KST"
            },
            "requestParameters": {
                "sourceIPAddress": "103.251.19.114"
            },
            "responseElements": {
                "x-amz-request-id": "2D22DK9ANSQVMMVT",
                "x-amz-id-2": "472KwVg6/5ppZ0KtK4D2CjEcI/ToJ4GOgf7KEIK9XoNcv+2M4sP6TddipFF2nM6oBLLnLv9/hCdwedBuB6hiii4EN55VlG60"
            },
            "s3": {
                "s3SchemaVersion": "1.0",
                "configurationId": "86412f6b-dff4-4688-824d-38ed57e7a560",
                "bucket": {
                    "name": "xml-to-csv-to-rds-bucket",
                    "ownerIdentity": {
                        "principalId": "A2U50U9G980KST"
                    },
                    "arn": "arn:aws:s3:::xml-to-csv-to-rds-bucket"
                },
                "object": {
                    "key": "CSV/sample.csv",
                    "size": 4548,
                    "eTag": "056adbe14b99bd3b00f3a7baba1757f3",
                    "sequencer": "00624C78154C9FC2CC"
                }
            }
        }
    ]
}

XML_PUT = {
    "Records": [
        {
            "eventVersion": "2.1",
            "eventSource": "aws:s3",
            "awsRegion": "ap-south-1",
            "eventTime": "2022-04-05T17:10:56.539Z",
            "eventName": "ObjectCreated:Put",
            "userIdentity": {
                "principalId": "A2U50U9G980KST"
            },
            "requestParameters": {
                "sourceIPAddress": "103.251.19.114"
            },
            "responseElements": {
                "x-amz-request-id": "FGNDDCN6RYPK21VW",
                "x-amz-id-2": "8W82iJmTEhz/bBk5MFZ/7KRLIWPTI4nbFGp6OPELkwjk3ZNHI6eJ6LY9hBEg9uxIJmbBtVS4HkaRtQzi/Hcf/QG1j+GOSsuX9bSuT8LyfQQ="
            },
            "s3": {
                "s3SchemaVersion": "1.0",
                "configurationId": "86412f6b-dff4-4688-824d-38ed57e7a560",
                "bucket": {
                    "name": "xml-to-csv-to-rds-bucket",
                    "ownerIdentity": {
                        "principalId": "A2U50U9G980KST"
                    },
                    "arn": "arn:aws:s3:::xml-to-csv-to-rds-bucket"
                },
                "object": {
                    "key": "XML/sample.xml",
                    "size": 4548,
                    "eTag": "056adbe14b99bd3b00f3a7baba1757f3",
                    "sequencer": "00624C782081E983ED"
                }
            }
        }
    ]
}
