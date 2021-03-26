#!/usr/bin/env python
from functools import partial

import boto3
from relay_sdk import Interface, Dynamic as D

relay = Interface()

session_token = None
try:
  session_token = relay.get(D.aws.connection.sessionToken)
except:
  pass

sess = boto3.Session(
  aws_access_key_id=relay.get(D.aws.connection.accessKeyID),
  aws_secret_access_key=relay.get(D.aws.connection.secretAccessKey),
  aws_session_token=session_token
)
s3 = sess.client('s3')
bucketName = relay.get(D.name)

try:
  response = s3.delete_bucket(
      Bucket=bucketName
  )
  print("Deleting bucket {}", bucketName)
except Exception as e: 
  print (e)

