FROM relaysh/core:latest-python
RUN pip install --upgrade boto3
COPY "./step.py" "/entrypoint.py"
ENTRYPOINT []
CMD ["python3", "/entrypoint.py"]

LABEL "org.opencontainers.image.title"="Get AWS S3 bucket encryption"
LABEL "org.opencontainers.image.description"="This task lists all AWS S3 buckets encryption settings given a list of bucket names."
LABEL "com.puppet.nebula.sdk.version"="v1"
