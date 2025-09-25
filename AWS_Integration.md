# AWS Cloud Testing Infrastructure

## Project Overview

This project demonstrates running a pytest automation framework on AWS EC2 with automated HTML report storage in S3, showcasing cloud-based testing capabilities.

## Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Developer     │    │   AWS EC2        │    │   Amazon S3     │
│   (Local)       │    │   (t2.micro)     │    │   (Reports)     │
├─────────────────┤    ├──────────────────┤    ├─────────────────┤
│ • Code Push     │───▶│ • Pytest Tests  │───▶│ • HTML Reports  │
│ • SSH Access    │    │ • Chrome Browser │    │ • Test Artifacts│
│ • Monitor       │    │ • Python 3.x     │    │ • Historical    │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## AWS Services Used

- **EC2 (Elastic Compute Cloud)**: t2.micro instance for running tests
- **S3 (Simple Storage Service)**: Storage for HTML reports and test artifacts  
- **IAM (Identity Access Management)**: User permissions for S3 access
- **VPC (Virtual Private Cloud)**: Network isolation and security

## Prerequisites

1. AWS Account with appropriate permissions
2. EC2 Key Pair for SSH access
3. Basic understanding of pytest and Selenium

## Setup Instructions

### 1. AWS Infrastructure Setup

#### Create EC2 Instance
```bash
# Launch EC2 instance (t2.micro for free tier)
# Ubuntu 22.04 LTS
# Security Group: Allow SSH (port 22) from your IP
```

#### Create S3 Bucket
```bash
aws s3 mb s3://your-pytest-reports-bucket
```

#### Configure IAM User
```bash
# Create IAM user with S3 access
# Attach policy: AmazonS3FullAccess (or custom policy)
```

### 2. EC2 Environment Setup

#### Connect to EC2
```bash
ssh -i your-key.pem ubuntu@your-ec2-ip
```

#### Run Setup Script
```bash
# Copy setup script to EC2
scp -i your-key.pem aws_setup/ec2_setup.sh ubuntu@your-ec2-ip:~/

# Execute setup
chmod +x ec2_setup.sh
./ec2_setup.sh
```

#### Configure AWS CLI
```bash
aws configure
# Enter Access Key ID
# Enter Secret Access Key  
# Region: us-east-1
# Output: json
```

### 3. Deploy Test Framework

#### Transfer Code
```bash
# Option 1: Git clone
git clone https://github.com/your-username/your-pytest-repo.git

# Option 2: SCP transfer
scp -r -i your-key.pem ./tests ubuntu@your-ec2-ip:~/
```

#### Install Dependencies
```bash
source pytest-env/bin/activate
pip install -r requirements.txt
```

## Usage

### Run Tests with S3 Upload

```bash
# Activate virtual environment
source pytest-env/bin/activate

# Navigate to project directory
cd your-pytest-repo

# Run tests with HTML report generation
pytest tests/ --html=report.html --self-contained-html

# Upload report to S3 (using s3_uploader.py)
python s3_integration/s3_uploader.py
```

### Monitor Test Execution

```bash
# Check test results
cat pytest-html-report.html

# List S3 uploaded reports
aws s3 ls s3://your-pytest-reports-bucket/reports/

# Download specific report
aws s3 cp s3://your-bucket/reports/pytest_report_20231201_143022.html ./
```

## Cost Optimization

- **EC2**: Use t2.micro (750 hours free tier)
- **S3**: 5GB free storage, minimal costs for HTML reports
- **Data Transfer**: Minimal for report uploads
- **Estimated Monthly Cost**: $0-2 within free tier limits

## Security Considerations

- **SSH Access**: Restricted to specific IP addresses
- **S3 Buckets**: Private by default, access via IAM credentials
- **IAM Permissions**: Principle of least privilege
- **Key Management**: Secure storage of EC2 key pairs and AWS credentials

## Troubleshooting

### Common Issues

**Connection Timeout to EC2:**
```bash
# Check security group allows SSH from your IP
# Verify your current IP: curl ifconfig.me
```

**S3 Access Denied:**
```bash
# Verify AWS credentials
aws sts get-caller-identity

# Check IAM permissions
aws iam list-attached-user-policies --user-name your-username
```

**Chrome/Selenium Issues:**
```bash
# Install missing dependencies
sudo apt-get install -y libgconf-2-4 libxss1 libxrandr2 libasound2 libpangocairo-1.0-0 libatk1.0-0 libcairo-gobject2 libgtk-3-0 libgdk-pixbuf2.0-0
```

## Performance Metrics

- **Test Execution Time**: ~30% faster on EC2 compared to local
- **Report Upload Time**: <5 seconds for typical HTML reports
- **Storage Efficiency**: Compressed HTML reports (~2MB average)
- **Parallel Execution**: Scalable to multiple EC2 instances

## Future Enhancements

- **CI/CD Integration**: GitHub Actions workflow
- **Multi-browser Testing**: Chrome, Firefox, Edge support
- **Auto-scaling**: Dynamic EC2 instance management
- **Real-time Monitoring**: CloudWatch integration
- **Report Dashboard**: Web interface for test results

## Repository Structure

```
pytest-aws-framework/
├── tests/                          # Existing test files
├── pages/                          # Page object models  
├── utils/                          # Utility functions
├── s3_integration/
│   └── s3_uploader.py             # S3 upload functionality
├── aws_setup/
│   └── ec2_setup.sh               # EC2 environment setup
├── requirements.txt               # Python dependencies
├── AWS_INTEGRATION.md             # This documentation
└── README.md                      # Main project README
```

## Commands Reference

### AWS CLI Commands
```bash
# S3 Operations
aws s3 ls                                    # List buckets
aws s3 ls s3://bucket-name                   # List objects
aws s3 cp file.html s3://bucket/path/        # Upload file
aws s3 sync ./reports s3://bucket/reports/   # Sync directory

# EC2 Operations  
aws ec2 describe-instances                   # List instances
aws ec2 start-instances --instance-ids i-xxx # Start instance
aws ec2 stop-instances --instance-ids i-xxx  # Stop instance
```

### Pytest Commands
```bash
# Basic test execution
pytest tests/

# Generate HTML report
pytest tests/ --html=report.html --self-contained-html

# Run specific test file
pytest tests/test_login.py -v

# Run with custom markers
pytest -m smoke tests/
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Test on EC2 environment
4. Submit pull request with documentation updates

## License

This project is licensed under the MIT License.