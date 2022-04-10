def checkExtension(filePath: str, extension: str) -> bool:
    """to check extension of file with specified

    Args:
        extension (str): reference extention with .

    Returns:
        bool: if file is with given extension
    """
    filePath = filePath.upper()
    extension = extension.upper()
    return filePath.endswith(extension)


def readFileContentFromS3(bucket: str, fileKey: str, s3) -> str:
    """Read s3 file content

    Args:
        bucket (str): name
        fileKey (str): key
        s3 (_type_): boto3 s3 resource

    Returns:
        str: content in file
    """
    try:
        # get file object from s3
        fileObject = s3.Object(bucket, fileKey)
        # read file content
        fileContent = fileObject.get()['Body'].read().decode('utf-8')
        return fileContent
    except Exception as e:
        raise createErrorStr("reading file", e)


def writeFileContentToS3(content: str, bucket: str, fileKey: str, s3) -> None:
    """To write given content to s3 object specified with bucket and key

    Args:
        bucket (str): name
        fileKey (str): key
        s3 (_type_): boto3 s3 resource object
    """
    try:
        fileObject = s3.Object(bucket, fileKey)
        fileObject.put(Body=content)
        pass

    except Exception as e:
        raise createErrorStr("writing file", e)


def deleteFile(bucket: str, fileKey: str, s3) -> None:
    """To delete specified s3 file

    Args:
        bucket (str): name
        fileKey (str): key
        s3 (_type_): boto3 s3 object
    """
    try:
        s3.Object(bucket, fileKey).delete()
    except Exception as e:
        raise createErrorStr("deleting file", e)


def createErrorStr(errorIn: str, error: str) -> str:
    """create custom error sting

    Args:
        errorIn (str): task name/description creating error
        error (str): error created

    Returns:
        str: custom error message
    """
    return (f"[Error : Error in {errorIn}]\n{{{error}}}")
