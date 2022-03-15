# Get the current tracking uri

# Mysql Local Server
# ---------------------------------------------------------
# mlflow server
# --backend-store-uri mysql://root:ketangangal@127.0.0.1:3306/mlops
# --default-artifact-root ./artifacts
# --host 127.0.0.1 -p 5000

# Mysql Server Remote
# ---------------------------------------------------------
# mlflow server
# --backend-store-uri mysql://admin:blackpanther@database-1.ctn6vycs4wym.ap-south-1.rds.amazonaws.com/mlops
# --default-artifact-root ./artifacts
# --host 127.0.0.1
# -p 5000

# from utils.aws_s3 import s3_bucket
#
# s3 = s3_bucket()
#
# print(s3.list_buckets())


# -var="access_key=AKIA6B5GUWRZEC3LCCUJ" -var="secret_key=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" -var="region=ap-south-1"

