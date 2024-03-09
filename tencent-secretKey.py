# -*- coding=utf-8
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import logging

# https://www.tencentcloud.com/zh/document/product/1045/48105?lang=zh&pg=

logging.basicConfig(level=logging.INFO, stream=sys.stdout)
secret_key = ''
secret_id = ''
region = ''
token = None
scheme = 'https'

config = CosConfig(Region=region, SecretId=secret_id,
                   SecretKey=secret_key, Token=token, Scheme=scheme)
client = CosS3Client(config)

response = client.put_object(
    Bucket='',
    Key='a.txt',
    Body='test'
)
