FROM relaysh/core:latest-python
RUN pip install --upgrade boto3
COPY "./step.py" "/entrypoint.py"
ENTRYPOINT []
CMD ["python3", "/entrypoint.py"]

LABEL "org.opencontainers.image.title"="Create AWS S3 bucket"
LABEL "org.opencontainers.image.description"="This task creates an AWS S3 bucket."
LABEL "com.puppet.nebula.sdk.version"="v1"
