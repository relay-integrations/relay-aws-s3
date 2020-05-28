# s3-create-bucket

This [AWS S3](https://aws.amazon.com/s3/) step container creates a bucket
with a provided set of configurations. 


## Specification

| Setting | Child setting | Data type | Description | Default | Required |
|---------|---------------|-----------|-------------|---------|----------|
| `aws` || mapping | A mapping of AWS account configuration. | None | True |
|| `connection` | AWS Connection | Relay Connection for the AWS account. Use the Connection sidebar to configure the AWS Connection | None | True |
|| `region` || string | Name of the AWS region to create the bucket in | None | True | 
| `name` || string | Name of the S3 bucket to create. To learn more about valid bucket names, see [Rules for Bucket Naming](https://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html#bucketnamingrules). | None | True |



## Example

```yaml
steps:
# ...
- name: s3-create-bucket
  image: projectnebula/s3-create-bucket
  spec:
    aws:
      connection: !Connection { type: aws, name: my-aws-account } 
      region: us-west-2
    name: my-bucket-1
```