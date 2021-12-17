import boto3
import os, glob

# access_key = os.environ["AWS_ACCESS_KEY"]
# secret_key = os.environ["AWS_SECRET_KEY"]

# s3 = boto3.resource("s3", aws_access_key_id=access_key, aws_secret_access_key=secret_key)

for file in glob.glob("*.jpg"):
    print(file)

img_file = [x for x in glob.glob("*.jpg")][0]

with open(img_file, "rb") as img:
    s3.Bucket('siotimages').put_object(Key=img_file, Body=img)

os.remove(img_file)
# find jpg file
# open file
# send to s3
# delete image








# s3client = boto3.client("s3", aws_access_key_id=access_key, aws_secret_access_key=secret_key)

# data = s3client.get_object(Bucket="siotimages", Key="test.jpg")
# pprint(data)

# pprint(dir(data["Body"]))

# with open("test_download.jpg", "wb") as img:
#     img.write(data["Body"].read())

# AKIAUZN3TC2NVAUB6VNI
# W3sX2NzYcqasEgS8ZYuXbuYzw61xpjE8XW6cP4f4