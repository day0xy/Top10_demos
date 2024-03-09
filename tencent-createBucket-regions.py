from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import os
import logging

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

secret_id = os.environ['AKIDZuxhBMAbeOovjDtI42h3mCJ7dsnQwkSq']
secret_key = os.environ['MUKs73g01j8DzTdU2HDqBDzpLbYBSOzF']
token = None
scheme = 'https'

# 遍历地域名列表
regions = [
    'ap-beijing-1',
    'ap-beijing',
    'ap-nanjing',
    'ap-shanghai',
    'ap-guangzhou',
    'ap-chengdu',
    'ap-chongqing',
    'ap-shenzhen-fsi',
    'ap-shanghai-fsi',
    'ap-beijing-fsi'
]

for region in regions:
    config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme)
    client = CosS3Client(config)

    response = client.create_bucket(
        Bucket='examplebucket-1250000000'
    )
