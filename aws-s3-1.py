import boto3
	 
	 
	AWS_ACCESS_KEY_ID='刚才保存下来的AWS access key id'
	AWS_SECRET_ACCESS_KEY='刚才保存下来的AWS Secret Access Key'
	AWS_BUCKET_NAME='S3 桶的名字'
	region_name='你使用AWS所在的区域'
	 
	 
	 
	def upload_file_to_s3(file_path):
	# 将数据上传到s3中
	    if file_path is None:
	        raise ValueError("Please enter a valid and complete file path")
	 
	    session = boto3.Session(aws_access_key_id=AWS_ACCESS_KEY_ID,
	       aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
	       region_name=region_name)  #这个必须加，不然会报错，此处根据自己的 s3 地区位置改变)
	    s3 = session.client("s3")
	    s3.upload_file(Filename=os.path.join('./',file_path), Key=f"{file_path}", Bucket=AWS_BUCKET_NAME)
	 
	 
	 
	upload_file_to_s3('FilePath.csv')