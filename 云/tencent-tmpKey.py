# -*- coding=utf-8
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import os
import logging

# 正常情况日志级别使用INFO，需要定位时可以修改为DEBUG，此时SDK会打印和服务端的通信信息
logging.basicConfig(level=logging.INFO, stream=sys.stdout)

# 1. 设置用户属性, 包括 secret_id, secret_key, region 等。Appid 已在 CosConfig 中移除，请在参数 Bucket 中带上 Appid。Bucket 由 BucketName-Appid 组成
tmp_secret_id = 'AKID0ap0IUWoVitphy_K_RXgcsavuxGsWYBplbCZaOMLBAr21Lg5IGmGCLYXkpz8dTF6'     # 临时密钥的 SecretId，临时密钥生成和使用指引参见 https://cloud.tencent.com/document/product/436/14048
tmp_secret_key = 'dnI6iFyS7AEdLyNHZrJrYIpSonB8GjpCAMRaiF6wNHc'   # 临时密钥的 SecretKey，临时密钥生成和使用指引参见 https://cloud.tencent.com/document/product/436/14048
token = '7PuNiKIBUP4cEYOVDHC7P3UvKBnoxQua63b298d60dacb72e68bd32494e74ab20hBZZlad1uLwNWb4slb2cKTlByHhojiYHsUTGwp3Kx6dFSHsBYldubJ6BqEb6SYj1_mcottZG_4elmXQEGN8q5rPIeXikjVigkVOnl5UoSO0-kH5YtLN5NOR0C4SNn5puDoSSKpISaAFNGvoRfgp4lWthRDONEJPFnQKM5fFehW54eJBGHgZ2wZ5_GBIrZV7ATMy3xyHAbz3-0IrZzL8k2Ij76ZhFe0gPPuWPiACCl0EjvH8eLDzvkI7BovnEWsRLgl5P4MT6Py2P5A_ti237PlkAaMxmDHhHuZa655wpIrUiVhAtj-f2byE5voor9VWHrIZtQpSmRix404s2WIkH5NCpoyqo-y_BE41WyeJ4rLtee9Lsptnw7rFKHVxOk4qvVPK9TrIWxn6UhKUZEWspP6hgP51hEyyiG9jd3N4NtLL2L8Fxb_4hZAsIkIlAH4Pv3i2lbRSVd0C6e-L90uuTdSmJVJ6FBvHC9O2qgO4uRXS77duqTBwDc_u4tQo_5YghdBXMXnn24stTwHgki-kK9Q'                # 临时密钥的 Token，临时密钥生成和使用指引参见 https://cloud.tencent.com/document/product/436/14048
region = 'ap-beijing'      # 替换为用户的 region，已创建桶归属的 region 可以在控制台查看，https://console.cloud.tencent.com/cos5/bucket
                           # COS 支持的所有 region 列表参见https://cloud.tencent.com/document/product/436/6224
scheme = 'https'           # 指定使用 http/https 协议来访问 COS，默认为 https，可不填

config = CosConfig(Region=region, SecretId=tmp_secret_id, SecretKey=tmp_secret_key, Token=token, Scheme=scheme)
client = CosS3Client(config)

response = client.list_objects(
    Bucket='zenvideo-pro-1258344701',
    Prefix='/'

)

