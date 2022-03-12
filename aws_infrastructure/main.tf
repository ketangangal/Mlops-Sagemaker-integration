provider "aws" {
  access_key= var.access_key
  secret_key= var.secret_key
  region = var.region
}

# Aws Security Group For Mysql
resource "aws_security_group" "security_group" {
  name        = var.security_group
  description = "Allow All Traffic"
  vpc_id      = var.vpc_id

  ingress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  tags = {
    Name = "mlops-mysql-security-group"
  }
}

# Sagemaker Role Creation
resource "aws_iam_role" "sagemaker_role_name" {
  name = var.sagemaker_role_name

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "sagemaker.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

# S3 Bucket Initialization
resource "aws_s3_bucket" "s3" {
  bucket = var.bucket_name
}

resource "aws_s3_bucket_acl" "s3" {
  bucket = aws_s3_bucket.s3.id
  acl    = "public-read-write"
}

# Mysql Server Initialization
resource "aws_db_instance" "mysql" {
  identifier           = var.identifier
  allocated_storage    = var.allocated_storage
  engine               = var.engine
  engine_version       = var.engine_version
  instance_class       = var.instance_class
  db_name              = var.mysql_db_name
  username             = var.mysql_username
  password             = var.mysql_password
  parameter_group_name = var.parameter_group_name
  skip_final_snapshot  = var.skip_final_snapshot
  vpc_security_group_ids = [aws_security_group.security_group.id]
  publicly_accessible = var.publicly_accessible
}
