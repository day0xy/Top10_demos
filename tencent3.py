# -*- coding=utf-8
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import os
import logging

# 正常情况日志级别使用INFO，需要定位时可以修改为DEBUG，此时SDK会打印和服务端的通信信息
logging.basicConfig(level=logging.INFO, stream=sys.stdout)

# 1. 设置用户属性, 包括 secret_id, secret_key, region 等。Appid 已在 CosConfig 中移除，请在参数 Bucket 中带上 Appid。Bucket 由 BucketName-Appid 组成
tmp_secret_id = 'AKIDjFfunVxlLjGDP0Iiz__aCdUtZylIuBm7y3xgGD_KJVxaRT3MBf3XcijSaP1Uj-vn'     # 临时密钥的 SecretId，临时密钥生成和使用指引参见 https://cloud.tencent.com/document/product/436/14048
tmp_secret_key = 'bic8myu/U+OfP987QZsu1oqeRdOSOzYLsF+7fPtWrL0='   # 临时密钥的 SecretKey，临时密钥生成和使用指引参见 https://cloud.tencent.com/document/product/436/14048
token = '8XNlviVi43koG5URwNA5jYCo0SVJ5Ota9536b255cd78860dbba4e33bb1debc35eOGPlemvaJZkIUqWwPIVCMUEZb3Ox4LkY84DTanJk257PSr0LglElCLQNggxkZi5vUAKBxDFaQDy2NX0mZp9JGf5jVOYQCFFpXXH1EuTZSo4HZzXvo444joR1_tBdBKn1Gjv9UG_ilPy-byL2dwvWkdHdIG0LZQlHVL2Yp5LWRl2R5jklJNINUUlgcSeyV9v0OCoJ5ZBdPvSgOW7rt7fWq_bZku4c27dvy5Qbvn_zwhzlsjoeYfXZ1qmQ8W-2d5qXgtMKdrm-lkGk25rxLgWcZ5TBhDOtCok8TUlns99s0P_zjiUGtsvDehgx1pq9bKFPc9rZRomi2Bopn0fgFVkBqGmipnxyWGabpAGfXLRdQPhvaYZnwDSTS_jfnIf7ddaiWrkNEqeAqrL7fw2MwLLjeFXhfAN9AvBsR8jEspytHXasx-EEzR8rtY7X59wO_L0AIniG18b7dbcvIn7997S8rGe7LHLTU7fNl6uZBu2_0UMhlA5QGAe3TW7XD-ChLk3mprPMPjMMMh_Ju_Fk_Jjvg'                # 临时密钥的 Token，临时密钥生成和使用指引参见 https://cloud.tencent.com/document/product/436/14048
region = 'ap-beijing'      # 替换为用户的 region，已创建桶归属的 region 可以在控制台查看，https://console.cloud.tencent.com/cos5/bucket
                           # COS 支持的所有 region 列表参见https://cloud.tencent.com/document/product/436/6224
scheme = 'https'           # 指定使用 http/https 协议来访问 COS，默认为 https，可不填

config = CosConfig(Region=region, SecretId=tmp_secret_id, SecretKey=tmp_secret_key, Token=token, Scheme=scheme)
client = CosS3Client(config)
marker = ""
while True:
    response = client.list_objects(
        Bucket='zenvideo-pro-1258344701',
        Prefix='assets/upload/9j04remiva1f7u1h4fv8g25/20240314',
        Marker=marker
    )
    if 'Contents' in response:
        print(response['Contents'])
    if response['IsTruncated'] == 'false':
        break 
    marker = response['NextMarker']
