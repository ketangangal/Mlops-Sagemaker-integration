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


def query(input_json, config=None):
    try:
        app_name = config['params']['app_name']
        region = config['params']['region']
        client = boto3.session.Session().client("sagemaker-runtime", region)
        response = client.invoke_endpoint(
            EndpointName=app_name,
            Body=input_json,
            ContentType='application/json; format=pandas-split',
        )
        preds = response['Body'].read().decode("ascii")
        preds = json.loads(preds)
        return preds
    except Exception as e:
        return f"Error Occurred While Prediction : {e.__str__()}"


def switching_models(config=None):
    try:
        app_name = config['params']['app_name']
        execution_role_arn = config['params']['execution_role_arn']
        image_ecr_url = config['params']['image_ecr_url']
        region = config['params']['region']
        s3_bucket_name = config['params']['s3_bucket_name']
        experiment_id = config['params']['experiment_id']
        new_run_id = config['params']['run_id']
        model_name = config['params']['model_name']

        new_model_uri = "s3://{}/{}/{}/artifacts/{}/".format(s3_bucket_name, experiment_id, new_run_id, model_name)

        response = mfs.deploy(app_name=app_name,
                              model_uri=new_model_uri,
                              execution_role_arn=execution_role_arn,
                              region_name=region,
                              image_url=image_ecr_url,
                              mode=mfs.DEPLOYMENT_MODE_REPLACE)

        return f"Model Successfully Changed : {new_run_id}"

    except Exception as e:
        return f"Error While Changing Model : {e.__str__()}"


def remove_deployed_model(config=None):
    try:
        app_name = config['params']['app_name']
        region = config['params']['region']

        mfs.delete(app_name=app_name, region_name=region)
        return f"Endpoint Successfully Deleted : {app_name}"

    except Exception as e:
        return f"Error While Deleting EndPoint : {e.__str__()}"


if __name__ == "__main__":
    runs = os.path.join(from_root(), 'mlruns/')
    print("Path to mlruns Exists :", os.path.exists(runs))
    status = upload(s3_bucket_name='mlops-sagemaker-runs-exp', mlruns_direc=runs)
    print(status)
