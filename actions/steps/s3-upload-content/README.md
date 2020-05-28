# s3-upload-content

This AWS S3 uploader step container uploads a single file, directory, or inline content to
an S3 bucket.

Use the following specifications:

## Specifications

| Setting | Child setting | Data type | Description | Default | Required |
|-----------|------------------|-----------|-------------|---------|----------|
| `aws` || mapping | A mapping of AWS account configuration. | None | True |
|| `accessKeyID` | string | An access key ID for the AWS account. You can pass the ID into Nebula as a secret. See the example below. | None | True |
|| `secretAccessKey` | string | The secret access key corresponding to the access key ID. Pass the key into Nebula as a secret. See the example below.| None | True |
|| `region` | string | The AWS region to use (for example, `us-west-2`). | None | True |
| `bucket` || string | The name of the target S3 bucket | None | True |
| `key` || string | Specify a key name for the object. | None | If `sourceContent` is present |
| `sourcePath` || string | The relative path, within the Git repository given in the `git` parameters, to upload. One of `sourcePath` or `sourceContent` must be specified. | None | If `sourceContent` is not present |
| `sourceContent` || string | The data to upload as a string. | None | If `sourcePath` is not present |
| `git` || mapping | A map of git configuration. If you're using HTTPS, only `name` and `repository` are required. | None | Required if `sourcePath` is present |
|| `ssh_key` | string | The SSH key to use when cloning the git repository. You can pass the key to Nebula as a secret. See the example below. | None | True |
|| `known_hosts` | string | SSH known hosts file. Use a Nebula secret to pass the contents of the file into the workflow as a base64-encoded string. See the example below. | None | True |
|| `name` | string | A directory name for the git clone. | None | True |
|| `branch` | string | The Git branch to clone. | `master` | False |
|| `repository` | string | The git repository URL. | None | True |
| `filters[]` || array | A YAML sequence (array) of path filters, applied in order. | None | False |
|| `type` | string | The type of the filter, one of `include` or `exclude`. | None | True |
|| `pattern` | string | The pattern for the filter. See the [S3 CLI documentation](https://docs.aws.amazon.com/cli/latest/reference/s3/index.html#use-of-exclude-and-include-filters) for details on the syntax. | None | True |
| `acl` || string | The canned ACL to use for the uploaded objects. For a list of canned ACLs, see [Access Control List (ACL) Overview](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl)| None | False |
| `storageClass` || string | The storage class to use for the uploaded objects. For informaton on storage classes, see [Amazon S3 Storage Classes](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html) | None | False |
| `contentType` || string | The media type of the uploaded object. Automatically detected when using `sourcePath` if possible. | Automatically detected, falling back to `binary/octet-stream` | False |
| `cacheControl` || string | The value of the HTTP `Cache-Control` header to associate with the uploaded objects. | None | False |
| `contentDisposition` || string | The value of the HTTP `Content-Disposition` header to associate with the uploaded objects. | None | False |
| `contentEncoding` || string | The value of the HTTP `Content-Encoding` header to associate with the uploaded objects. | None | False |
| `contentLanguage` || string | The value of the HTTP `Content-Language` header to associate with the uploaded objects. | None | False |
| `expires` || string | The time at which the uploaded object is no longer cacheable, in ISO 8601 format. | None | False |
| `metadata` || mapping | A YAML mapping of arbitrary key-value data to store with the uploaded objects. | None | False |

> **Note**: The value you set for a secret must be a string. If you have multiple key-value pairs to pass into the secret, or your secret is the contents of a file, you must encode the values using base64 encoding, and use the encoded string as the secret value.

## Examples

Here is an example of the step in a Nebula workflow:

```YAML
steps:

...

- name: s3-uploader
  image: projectnebula/s3-upload-content
  spec:
    aws:
      accessKeyID: !Secret key-id
      secretAccessKey: !Secret access-key
      region: us-west-2  
    bucket: my-bucket
    key: my-docs
    sourcePath: ./docs
    git: 
      ssh_key: !Secret ssh_key
      known_hosts: !Secret known_hostss
      name: my-git-repo
      branch: dev
      repository: path/to/your/repo 
    filters:
    - type: include
      pattern: *.txt
    - type: exclude
      pattern: .git/*  
    acl: public-read
    storageClass: STANDARD 
    metadata:
      author: John Smith
```