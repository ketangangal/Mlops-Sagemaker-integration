from utils.sagemaker_integration import switch_models
from utils.common import read_config


if __name__ == "__main__":
    config = read_config("configurations/config.yaml")
    response = switching_models(config)
    print(response)
