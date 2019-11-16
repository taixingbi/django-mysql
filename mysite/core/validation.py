from django.http import HttpResponseBadRequest
from django.core.exceptions import ValidationError
from django.core.exceptions import SuspiciousOperation
import json

import logging
logger = logging.getLogger(__name__)

class validation:
    def __init__(self, data):
        self.data= data

    def isJson(self):
        try:
            dataJson= json.loads(self.data)
            print(dataJson)
            return dataJson
        except:
            msg= 'Json format is not correct'
            raise SuspiciousOperation(msg)

    def format(self, data):
        try:
            data['LanguageCode']
            data['MediaFormat']
            data['OutputBucketName']
        except:
            msg= 'keys: LanguageCode, MediaFormat or OutputBucketName not exist'
            raise SuspiciousOperation(msg)

        # except ValueError:
        #     msg= 'Invalid JSON'
        #     logger.error(msg)
        #     raise HttpResponseBadRequest(msg)
                
        if data['LanguageCode']!= "en-US":
            msg= 'key: LanguageCode must be en-US'
            logger.error(msg)
            raise SuspiciousOperation(msg)

        if data['MediaFormat']!= "wav":
            msg= 'key: MediaFormat must wav'
            logger.error(msg)
            raise SuspiciousOperation(msg)
                   
        return data

    def request(self):
        dataJson= self.isJson()
        self.format(dataJson)

        return dataJson


if __name__ == '__main__':   

    data= {
            "LanguageCode": "en-US",
            "Media": { 
            "MediaFileUri": "string"
            },
            "MediaFormat": "wav",
            "MediaSampleRateHertz": "number",
            "OutputBucketName": "thrivee-dev/audiotranscribe/demo.wav",
            "Settings": { 
            "ChannelIdentification": "boolean",
            "MaxSpeakerLabels": "number",
            "ShowSpeakerLabels": "boolean",
            "VocabularyName": "string"
            },
            "TranscriptionJobName": "string"
        }

    print(data)
    validation(data).format()
    
        
