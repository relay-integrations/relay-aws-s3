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
print ("Found the following bucket ACLs:")

bucket_acls={}
for bucket in buckets:
  acls = s3.get_bucket_acl(Bucket=bucket)
  print ("\nBucket {}:".format(bucket))
  print ("\n{:<20} {:<75} {:<30}".format('TYPE', 'DISPLAYNAME OR URI', 'PERMISSION')) 
  for grant in acls['Grants']:
    if 'DisplayName' in grant['Grantee'].keys():
      print("{:<20} {:<75} {:<30}".format(grant['Grantee']['Type'], grant['Grantee']['DisplayName'], grant['Permission']))
    else:
      print("{:<20} {:<75} {:<30}".format(grant['Grantee']['Type'], grant['Grantee']['URI'], grant['Permission']))
    
  bucket_acls[bucket] = acls['Grants']

print('\nAdding {0} sets of bucket(s) ACLs to the output `bucketACLs`'.format(len(bucket_acls)))
relay.outputs.set('bucketACLs', bucket_acls)