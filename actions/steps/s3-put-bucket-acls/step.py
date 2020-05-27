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

buckets = relay.get(D.buckets)
acl = relay.get(D.acl)
print ("Modifying the following bucket(s) to {}:".format(acl))

for bucket in buckets:
  print(bucket)
  s3.put_bucket_acl(Bucket=bucket, ACL=acl)
  
print('\nModified {} bucket(s)'.format(len(buckets)))