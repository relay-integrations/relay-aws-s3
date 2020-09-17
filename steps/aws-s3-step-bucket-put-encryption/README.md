# aws-s3-step-bucket-put-encryption

This [AWS S3](https://aws.amazon.com/s3/) step container enables default encryption
on a list of AWS S3 buckets. Currently, default encryption is the only supported option.


## Example

```yaml
steps:
# ...
- name: s3-put-bucket-encryption
  image: relaysh/aws-s3-step-bucket-put-encryption
  spec:
    aws:
      connection: !Connection { type: aws, name: my-aws-account } 
    buckets:
    - bucket-1-us-east-1
    - bucket-2-us-east-2
```