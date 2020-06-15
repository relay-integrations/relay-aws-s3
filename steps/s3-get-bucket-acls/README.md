# s3-get-bucket-acls

This [AWS S3](https://aws.amazon.com/s3/) step container lists the bucket
ACLs in an AWS account given a list of bucket names. It sets an output, `bucketACLs`, 
to an array containing the ACL grants.

## Specification

| Setting | Child setting | Data type | Description | Default | Required |
|---------|---------------|-----------|-------------|---------|----------|
| `aws` || mapping | A mapping of AWS account configuration. | None | True |
|| `connection` | AWS Connection | Relay Connection for the AWS account. Use the Connection sidebar to configure the AWS Connection | None | True |
| `buckets` || array of bucket names | List of S3 bucket names | None | True | 

## Outputs

| Name | Data type | Description |
|------|-----------|-------------|
| bucketACLs | Mapping | Dictionary of S3 bucket names as their ACL grants. See below example.|

## Example

```yaml
steps:
# ...
- name: s3-get-bucket-acls
  image: projectnebula/s3-get-bucket-acls
  spec:
    aws:
      connection: !Connection { type: aws, name: my-aws-account } 
    buckets:
    - bucket-1-us-east-1
    - bucket-2-us-east-2
```

## Output Example
Example output of `bucketACLs`
```
{
   "bucket-1-us-east-1":[
      {
         "Grantee":{
            "DisplayName":"my-aws-account",
            "ID":"44811c1fbc6d4ed613321424153e1be6ad632101365c36f8620a7faadc44a1ef",
            "Type":"CanonicalUser"
         },
         "Permission":"FULL_CONTROL"
      }
   ],
   "bucket-2-us-east-2":[
      {
         "Grantee":{
            "DisplayName":"my-aws-account",
            "ID":"1524c1fbc6d4ed6133214153e1be6ad63412221365c36f8620a7faadc44a1ef",
            "Type":"CanonicalUser"
         },
         "Permission":"FULL_CONTROL"
      }
   ]
}
 ```
