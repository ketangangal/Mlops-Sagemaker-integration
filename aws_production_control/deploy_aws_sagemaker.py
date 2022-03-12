from utils.sagemaker_integration import sagemaker_integration
from utils.common import read_config


if __name__ == "__main__":
    config = read_config("aws_configurations/config.yaml")
    sagemaker = sagemaker_integration(config)
    response = sagemaker.deploy_model_aws_sagemaker()
    print(response)

