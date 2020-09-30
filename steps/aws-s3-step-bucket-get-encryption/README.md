# aws-s3-step-bucket-get-encryption

This [AWS S3](https://aws.amazon.com/s3/) step container lists the bucket encryption 
settings in an AWS account given a list of bucket names. It sets an output, `encryptionConfigurations`, 
to an array containing the encryption configurations for each bucket.

## Example

```yaml
steps:
# ...
- name: s3-get-bucket-encryption
  image: relaysh/aws-s3-step-bucket-get-encryption
  spec:
    aws:
      connection: !Connection { type: aws, name: my-aws-account } 
    buckets:
    - bucket-1-us-east-1
    - bucket-2-us-east-2
```