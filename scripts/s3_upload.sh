#!/bin/bash

LOG_DIR="/logs"
S3_BUCKET="s3://your-bucket/logs"

for file in $(find $LOG_DIR -type f -mtime +7); do
    gzip "$file"
    aws s3 cp "$file.gz" "$S3_BUCKET/"
    rm "$file.gz"
done
