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

print ("Found the following buckets:\n")
bucket_list=[]
for bucket in s3.list_buckets()['Buckets']:
  bucket_list.append(bucket['Name'])
  print (bucket['Name'])

print('\nAdding {0} bucket(s) to the output `buckets`'.format(len(bucket_list)))
relay.outputs.set('buckets', bucket_list)
