# aws-s3-step-bucket-put-acls

This [AWS S3](https://aws.amazon.com/s3/) step container changes a list of AWS S3 buckets 
ACLs to a provided [canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl). The following ACLs can be specified: 
- `private`
- `public-read`
- `public-read-write`
- `authenticated-read`

For more information on setting S3 bucket ACLs, check out the [AWS API documentation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketAcl.html) here.  