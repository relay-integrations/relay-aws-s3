FROM relaysh/core:latest-python
RUN pip install --upgrade boto3
COPY "./step.py" "/entrypoint.py"
ENTRYPOINT []
CMD ["python3", "/entrypoint.py"]

LABEL "org.opencontainers.image.title"="List AWS S3 buckets"
LABEL "org.opencontainers.image.description"="This task lists the S3 buckets in a given account and region."
LABEL "com.puppet.nebula.sdk.version"="v1"
