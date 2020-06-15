# s3-list-buckets

This [AWS S3](https://aws.amazon.com/s3/) step container lists the buckets
in an AWS account and sets an output, `buckets`, to an array containing
information about them.

## Specification

| Setting | Child setting | Data type | Description | Default | Required |
|---------|---------------|-----------|-------------|---------|----------|
| `aws` || mapping | A mapping of AWS account configuration. | None | True |
|| `connection` | AWS Connection | Relay Connection for the AWS account. Use the Connection sidebar to configure the AWS Connection | None | True |

## Outputs

| Name | Data type | Description |
|------|-----------|-------------|
| `buckets` | array of bucket names | List of the names of S3 buckets in the account. |

## Example

```yaml
steps:
# ...
- name: s3-list-buckets
  image: projectnebula/s3-list-buckets
  spec:
    aws:
      connection: !Connection { type: aws, name: my-aws-account } 
```

## Output Example
Example output of `buckets`
```
[
  'bucket-1-us-east-1',
  'bucket-2-us-east-1',
  'bucket-3-us-west-2',
  'bucket-4-us-west-2',
  'bucket-5-us-east-2',
]
 
