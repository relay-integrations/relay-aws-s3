# aws-s3-step-bucket-list

This [AWS S3](https://aws.amazon.com/s3/) step container lists the buckets
in an AWS account and sets an output, `buckets`, to an array containing
information about them.

## Example

```yaml
steps:
# ...
- name: s3-list-buckets
  image: relaysh/aws-s3-step-bucket-list
  spec:
    aws:
      connection: !Connection { type: aws, name: my-aws-account } 
```