# s3-put-bucket-acls

This [AWS S3](https://aws.amazon.com/s3/) step container changes a list of AWS S3 buckets 
ACLs to a provided canned ACL. The following ACLs can be specified: 
- `private`
- `public-read`
- `public-read-write`
- `authenticated-read`

## Specification

| Setting | Child setting | Data type | Description | Default | Required |
|---------|---------------|-----------|-------------|---------|----------|
| `aws` || mapping | A mapping of AWS account configuration. | None | True |
|| `connection` | AWS Connection | Relay Connection for the AWS account. Use the Connection sidebar to configure the AWS Connection | None | True |
| `buckets` || array of bucket names | List of S3 bucket names to modify the ACL | None | True | 
| `acl` || string | One of `private`, `public-read`, `public-read-write`, `authenticated-read` | None | True |


## Example

```yaml
steps:
# ...
- name: s3-put-bucket-acls
  image: projectnebula/s3-put-bucket-acls
  spec:
    aws:
      connection: !Connection { type: aws, name: my-aws-account } 
    buckets:
    - bucket-1-us-east-1
    - bucket-2-us-east-2
    acl: private 
```