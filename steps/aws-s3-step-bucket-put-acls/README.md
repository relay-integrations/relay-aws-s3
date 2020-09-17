# aws-s3-step-bucket-put-acls

This [AWS S3](https://aws.amazon.com/s3/) step container changes a list of AWS S3 buckets 
ACLs to a provided [canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl). The following ACLs can be specified: 
- `private`
- `public-read`
- `public-read-write`
- `authenticated-read`

For more information on setting S3 bucket ACLs, check out the [AWS API documentation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketAcl.html) here.  

## Example

```yaml
steps:
# ...
- name: s3-put-bucket-acls
  image: relaysh/aws-s3-step-bucket-put-acls
  spec:
    aws:
      connection: !Connection { type: aws, name: my-aws-account } 
    buckets:
    - bucket-1-us-east-1
    - bucket-2-us-east-2
    acl: private 
```
