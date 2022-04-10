# xml-to-csv-to-rds
How to convert XML file to CSV file and save it to RDS on AWS using lambda function
<br>
For this code I have created below stucture in aws s3
	
	AWS S3
		|->my-working-bucket
			|
			|-> XML
			|-> CSV
			|-> dbCredentials.json

dbCredentials.json will be used to store DB credentials in below format

	{
    "host": "aws-ds-host",
    "db": "db-name",
    "username": "db username",
    "password": "db password",
    "port": db port
	}

Any PUT Action to this bucket is bound to lambda triggers

steps
	
	1. Find file type that triggered lambda
	2. Call related function [xml->csv or csv->rds]
	3. Related conversion and storing of data


As AWS lambda by default does not support pymysql and pandas we need to attach layers of the same.

	--pymysql
	[use of linux if preferable]
	<1> Download pymysql
	-> use of python folder is must for layer to work. DON'T CHANGE IT'S NAME

	>> mkdir python 
	>> pip install pymysql -t python --no-user
	>> zip -r pymysql.zip ./python

	--pandas
	-> Layer is already available on aws lambda by default. But we need to attach it to use it.


Upload layer

	Do below steps for pymysql
	-> AWS --> lambda --> layers --> add layer --> fill up details and upload layer

Attach layer

	-> AWS --> lambda --> our function --> "Layers" section --> Add a layer --> do below steps
	
	<1> To add pymysql
	-> Select "Custom Source" under "Layer Source" --> select layer name (that we created before by uploading zip) --> select version --> Add
	<2> To add inbuild pandas layer
	-> Select "AWS Layers" unser "Layer Source" --> select "AWSDataWrangler..." --> select version --> Add


You are now good to use your custom and aws inbuilt layers.
pymysql.zip is placed under dependancy folder for reference
