# aws-s3-step-bucket-upload-content

This AWS S3 uploader step container uploads a single file, directory, or inline content to
an S3 bucket.

## Examples

Here is an example of the step in a Nebula workflow:

```YAML
steps:

...

- name: s3-uploader
  image: relaysh/aws-s3-step-bucket-upload-content
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