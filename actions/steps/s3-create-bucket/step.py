#!/usr/bin/env python
from functools import partial

import boto3
from nebula_sdk import Interface, Dynamic as D

relay = Interface()

sess = boto3.Session(
  aws_access_key_id=relay.get(D.aws.connection.accessKeyID),
  aws_secret_access_key=relay.get(D.aws.connection.secretAccessKey)
)
s3 = sess.client('s3')

region = relay.get(D.aws.region)
bucketName = relay.get(D.name)

try:
  response = s3.create_bucket(
      Bucket=bucketName,
      CreateBucketConfiguration={ 'LocationConstraint': region }
  )
  print ("Created bucket {}".format(bucketName))
except Exception as e: 
  print (e)

