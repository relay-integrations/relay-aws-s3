#!/usr/bin/env python
from functools import partial

import boto3
import json
from nebula_sdk import Interface, Dynamic as D

relay = Interface()

sess = boto3.Session(
  aws_access_key_id=relay.get(D.aws.connection.accessKeyID),
  aws_secret_access_key=relay.get(D.aws.connection.secretAccessKey)
)
s3 = sess.client('s3')

buckets = relay.get(D.buckets)

all_encryption_configurations = {}
not_encrypted = []

for bucket in buckets:
  try:
    configurations = s3.get_bucket_encryption(Bucket=bucket)
    all_encryption_configurations[bucket] = configurations['ServerSideEncryptionConfiguration']['Rules']
    print ("\nBucket {}:".format(bucket))
    print(*[rule for rule in all_encryption_configurations[bucket]], sep="\n")
  except:
    all_encryption_configurations[bucket] = None
    not_encrypted.append(bucket)
    continue

print("\n{} Buckets with no encryption:".format(len(not_encrypted)))
print(*[bucket for bucket in not_encrypted], sep="\n")

print('\nAdding {0} sets of bucket(s) encryption configurations to the output `encryptionConfigurations`'.format(len(all_encryption_configurations)))
relay.outputs.set('encryptionConfigurations', all_encryption_configurations)
