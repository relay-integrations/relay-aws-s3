# s3-get-bucket-encryption

This [AWS S3](https://aws.amazon.com/s3/) step container lists the bucket encryption 
settings in an AWS account given a list of bucket names. It sets an output, `encryptionConfigurations`, 
to an array containing the encryption configurations for each bucket.

## Specification

| Setting | Child setting | Data type | Description | Default | Required |
|---------|---------------|-----------|-------------|---------|----------|
| `aws` || mapping | A mapping of AWS account configuration. | None | True |
|| `connection` | AWS Connection | Relay Connection for the AWS account. Use the Connection sidebar to configure the AWS Connection | None | True |
| `buckets` || array of bucket names | List of S3 bucket names | None | True | 

## Outputs

| Name | Data type | Description |
|------|-----------|-------------|
| encryptionConfigurations | Mapping | Dictionary of S3 bucket names and their encryption configurations. See below example.|

## Example

```yaml
steps:
# ...
- name: s3-get-bucket-encryption
  image: projectnebula/s3-get-bucket-encryption
  spec:
    aws:
      connection: !Connection { type: aws, name: my-aws-account } 
    buckets:
    - bucket-1-us-east-1
    - bucket-2-us-east-2
```

## Output Example
Example output of `encryptionConfigurations`

{
   'bucket-1-us-east-1':
      {
         'ApplyServerSideEncryptionByDefault': 
            {
               'SSEAlgorithm': 'AES256'
            }
      },
   'bucket-2-us-east-1': None
}
