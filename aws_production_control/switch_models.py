from utils.sagemaker_integration import sagemaker_integration
from utils.common import read_config


if __name__ == "__main__":
    config = read_config("configurations/config.yaml")
    sagemaker = sagemaker_integration(config)
    response = sagemaker.switching_models()
    print(response)
