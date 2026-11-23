# AWS DevOps Automation

Academic infrastructure and automation project combining boto3 reporting, DynamoDB operations, S3 uploads, a Lambda handler, a CloudFormation template and a GitHub Actions workflow.

## Technologies

Python, boto3, Bash, Flask, Docker Compose, AWS EC2, S3, CloudWatch, Auto Scaling, DynamoDB, Lambda, CloudFormation and Systems Manager.

## Capabilities

- `automatizacion.py`: EC2 inventory, 24-hour CPU averages, S3 listing and Auto Scaling inspection.
- `s3_automatizacion.py`: creates a local sample file and uploads it to the account-specific bucket.
- `dynamodb_operaciones.py`: creates a table and demonstrates create, update, read and delete of one sample record.
- `lambda/lambda_function.py`: returns a sample JSON response.
- `template.yaml`: EC2 security group, instance and versioned S3 bucket.
- `docker/`: Flask demo with `/` and `/health`; the separate Nginx container uses its default configuration.
- GitHub Actions validates the Flask module, packages sources and supports an explicit manual deployment action.

## Local setup

```bash
git clone https://github.com/Angel0208ia/aws-devops-automation.git
cd aws-devops-automation
python -m venv .venv
```

Activate the virtual environment (`source .venv/bin/activate` on Bash, `.venv\Scripts\Activate.ps1` on PowerShell), then:

```bash
pip install -r requirements.txt
python automatizacion.py
```

Configure AWS credentials outside the repository using a profile or IAM role. The scripts use `us-east-1`. The first report queries the configured AWS account; it is not an offline demonstration.

For the local web service:

```bash
cd docker
docker compose up --build
```

Visit http://localhost:5000/health. Port 80 serves the separate default Nginx page; this configuration does not proxy Nginx to Flask.

## Cloud prerequisites

The template assumes an AWS Learner Lab setup, a usable default VPC, `LabInstanceProfile`, and an AMI valid in the selected region. Review those values before deploying. The DynamoDB demo writes and then deletes its sample record; the S3 demo uploads data. `lifecycle.json`, if applied, expires matching objects after 30 days.

GitHub Actions needs secrets `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` and optional `AWS_SESSION_TOKEN`. The deployment job runs only through **Run workflow**. It uploads an artifact and sends a demonstration SSM command; it does not install the Flask artifact on EC2. SSM requires a managed instance and the appropriate IAM permissions.

`setup.sh` targets a dnf-based Linux environment. `usuarios.sh` changes ownership and Docker-group membership; inspect it before running. `limpieza_logs.sh` removes project log files older than seven days.

## Scope and verification

Intermediate DevOps learning project with several small service demonstrations, not a production platform. Listings currently use single API responses and may omit resources requiring pagination. No AWS provisioning, system setup, cleanup scripts or deployment was executed during this audit. No application screenshots were present.
