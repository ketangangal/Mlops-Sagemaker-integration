# Mlops-Sagemaker-integration
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

### Send Ml-runs on Aws-S3 Bucket
```commandline
python utils/sagemaker_integration.py
```