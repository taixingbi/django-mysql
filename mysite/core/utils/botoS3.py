from botocore.exceptions import ClientError
import logging
logger = logging.getLogger(__name__)

import boto3, botocore
import os

class s3Bucket:
    def __init__(self, bucket, key, fileName):
        self.bucket= bucket
        self.key= key
        self.fileName= fileName

    def loadFile(self, overwirte= False):
        print("\nloading..  from S3 ", self.bucket, self.key)
        if overwirte==False and os.path.exists(self.fileName):
            return self.fileName

        s3 = boto3.client(
            's3',
            aws_access_key_id='AKIARJLDNDHBRFUVNTHR',
            aws_secret_access_key='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'
        )

        try:
            s3.download_file(self.bucket, self.key, self.fileName)
            print("succefully load S3  from " + self.bucket + "/" +self.key + " to " + self.fileName)
            return self.fileName
        except ClientError as e:
            logger.error(e)
            raise (e, "fail loading from S3 " + self.bucket + "/" + self.key + " to " + self.fileName)

