# aws-s3-step-bucket-get-acls

This [AWS S3](https://aws.amazon.com/s3/) step container lists the bucket
ACLs in an AWS account given a list of bucket names. It sets an output, `bucketACLs`, 
to an array containing the ACL grants.

## Example

```yaml
steps:
# ...
- name: s3-get-bucket-acls
  image: relaysh/aws-s3-step-bucket-get-acls
  spec:
    aws:
      connection: !Connection { type: aws, name: my-aws-account } 
    buckets:
    - bucket-1-us-east-1
    - bucket-2-us-east-2
```