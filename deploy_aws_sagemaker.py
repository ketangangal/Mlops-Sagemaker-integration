from utils.sagemaker_integration import deploy_model_aws_sagemaker
from utils.common import read_config


if __name__ == "__main__":
    config = read_config("./config.yaml")
    response = deploy_model_aws_sagemaker(config)
    print(response)

