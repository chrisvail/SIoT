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

