from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import os

# 1. 设置用户属性, 包括 secret_id, secret_key, region等。Appid 已在 CosConfig 中移除，请在参数 Bucket 中带上 Appid。Bucket 由 BucketName-Appid 组成
secret_id = os.environ['AKIDZuxhBMAbeOovjDtI42h3mCJ7dsnQwkSq']
secret_key = os.environ['MUKs73g01j8DzTdU2HDqBDzpLbYBSOzF']
token = None               # 如果使用永久密钥不需要填入 token，如果使用临时密钥需要填入
region = 'ap-beijing'
scheme = 'https'           # 指定使用 http/https 协议来访问 COS，默认为 https，可不填

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme)
client = CosS3Client(config)