# s3-put-bucket-encryption

This [AWS S3](https://aws.amazon.com/s3/) step container enables default encryption
on a list of AWS S3 buckets. Currently, default encryption is the only supported option.

## Specification

| Setting | Child setting | Data type | Description | Default | Required |
|---------|---------------|-----------|-------------|---------|----------|
| `aws` || mapping | A mapping of AWS account configuration. | None | True |
|| `connection` | AWS Connection | Relay Connection for the AWS account. Use the Connection sidebar to configure the AWS Connection | None | True |
| `buckets` || array of bucket names | List of S3 bucket names to modify the ACL | None | True | 


## Example

```yaml
steps:
# ...
- name: s3-put-bucket-encryption
  image: projectnebula/s3-put-bucket-encryption
  spec:
    aws:
      connection: !Connection { type: aws, name: my-aws-account } 
    buckets:
    - bucket-1-us-east-1
    - bucket-2-us-east-2
```