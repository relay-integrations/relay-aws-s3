# aws-s3-step-bucket-create

This [AWS S3](https://aws.amazon.com/s3/) step container creates a bucket
with a provided set of configurations. 

## Example

```yaml
steps:
# ...
- name: s3-create-bucket
  image: relaysh/aws-s3-step-bucket-create
  spec:
    aws:
      connection: !Connection { type: aws, name: my-aws-account } 
      region: us-west-2
    name: my-bucket-1
```