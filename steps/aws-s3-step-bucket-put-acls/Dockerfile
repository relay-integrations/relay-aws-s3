FROM relaysh/core:latest-python
RUN pip install --upgrade boto3
COPY "./step.py" "/entrypoint.py"
ENTRYPOINT []
CMD ["python3", "/entrypoint.py"]

LABEL "org.opencontainers.image.title"="Put AWS S3 bucket ACLs"
LABEL "org.opencontainers.image.description"="This step container changes a list of AWS S3 buckets ACLs to a provided canned ACL."
LABEL "com.puppet.nebula.sdk.version"="v1"
