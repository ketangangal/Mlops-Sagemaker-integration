import subprocess
import os
from from_root import from_root
import boto3
import mlflow.sagemaker as mfs
import json


def upload(s3_bucket_name=None, mlruns_direc=None):
    try:
        output = subprocess.run(["aws", "s3", "sync", "{}".format(mlruns_direc),
                                 "s3://{}".format(s3_bucket_name)],
                                stdout=subprocess.PIPE,
                                encoding='utf-8')

        print("\nSaved to bucket: ", s3_bucket_name)
        return f"Done Uploading : {output.stdout}"

    except Exception as e:
        return f"Error Occurred While Uploading : {e.__str__()}"


def deploy_model_aws_sagemaker(config=None):
    try:
        app_name = config['params']['app_name']
        execution_role_arn = config['params']['execution_role_arn']
        image_ecr_url = config['params']['image_ecr_url']
        region = config['params']['region']
        s3_bucket_name = config['params']['s3_bucket_name']
        experiment_id = config['params']['experiment_id']
        run_id = config['params']['run_id']
        model_name = config['params']['model_name']

        model_uri = "s3://{}/{}/{}/artifacts/{}/".format(s3_bucket_name, experiment_id, run_id, model_name)
        print(model_uri)
        mfs.deploy(app_name=app_name,
                   model_uri=model_uri,
                   execution_role_arn=execution_role_arn,
                   region_name=region,
                   image_url=image_ecr_url,
                   mode=mfs.DEPLOYMENT_MODE_CREATE)

        return "Deployment Successfully"
    except Exception as e:
        return f"Error Occurred while Deploying : {e.__str__()} "


def make_prediction():
    pass


def switching_models():
    pass


def remove_deployed_model():
    pass


if __name__ == "__main__":
    runs = os.path.join(from_root(), 'mlruns/')
    print("Path to mlruns Exists :", os.path.exists(runs))
    status = upload(s3_bucket_name='mlops-sagemaker-runs-exp', mlruns_direc=runs)
    print(status)