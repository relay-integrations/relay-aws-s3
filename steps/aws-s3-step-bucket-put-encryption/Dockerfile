FROM relaysh/core:latest-python
RUN pip install --upgrade boto3
COPY "./step.py" "/entrypoint.py"
ENTRYPOINT []
CMD ["python3", "/entrypoint.py"]

LABEL "org.opencontainers.image.title"="Put AWS S3 bucket encryption"
LABEL "org.opencontainers.image.description"="This step container enables default encryption on a list of AWS S3 buckets."
LABEL "com.puppet.nebula.sdk.version"="v1"
