# Mlops-Sagemaker-integration
## MLFlow provides explicit AWS SageMaker support in its operationalization code.
```
create --prefix ./env python=3.8 -y && conda activate ./env 
```

### Run 2-3 times with different alpha and li ratio
```
python main.py alpha l1_ratio
```
### To See logs 
```commandline
mlflow ui
```
### PREREQUISITES 
1. Install AWS CLI 
2. Open Cmd : aws configure
3. Paste Public key , private key and Region
4. Run below command

### Permissions 
1. AmazonEC2ContainerRegistryFullAccess
2. AmazonS3FullAccess
3. EC2InstanceProfileForImageBuilderECRContainerBuilds
4. AWSAppRunnerServicePolicyForECRAccess

## Create Image and Upload on docker 
```
mlflow sagemaker build-and-push-container
```
## Run Server
```
mlflow server
--backend-store-uri mysql://admin:pass@endpoint/DB-name
--default-artifact-root ./artifacts
--host 127.0.0.1
-p 5000
```



### Send Ml-runs on Aws-S3 Bucket
```commandline
python utils/sagemaker_integration.py
```


### To build and Push Container
```commandline
mlflow sagemaker build-and-push-container
```


## Check Errors If occurred try:
```
docker.errors.DockerException: Install pypiwin32 package to enable npipe:// support
Solution : Instead of pip install pypiwin32  Try : conda install -c anaconda pywin32
```




