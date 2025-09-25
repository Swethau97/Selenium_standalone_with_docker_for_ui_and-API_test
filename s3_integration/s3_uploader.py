import boto3
import os
from datetime import datetime


class S3ReportUploader:
    def __init__(self, bucket_name="pytest-reports-ec2", region='ap-south-1'):
        self.bucket_name = bucket_name
        self.s3_client = boto3.client('s3', region_name=region)

    def upload_report(self, report_path):
        """Upload pytest HTML report to S3"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            s3_key = f"reports/pytest_report_{timestamp}.html"

            self.s3_client.upload_file(report_path, self.bucket_name, s3_key)

            print(f"Report uploaded to: s3://{self.bucket_name}/{s3_key}")
            return s3_key

        except Exception as e:
            print(f"Upload failed: {e}")
            return None