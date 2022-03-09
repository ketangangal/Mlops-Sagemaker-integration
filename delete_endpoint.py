from utils.sagemaker_integration import remove_deployed_model
from utils.common import read_config

# Instructions

# Ins 1
# One thing to note is that you should make sure you don’t accidentally leave any resources running
# because the costs can certainly stack up over time and put a dent in your wallet. For services like SageMaker
# endpoints, you are charged by the hour, so be sure to delete them once you’re done with them.

# Ins 2
# As for the S3 bucket and the ECR container, those are a one-time charge that only bill for data transfer.


if __name__ == "__main__":
    config = read_config("configurations/config.yaml")
    response = remove_deployed_model(config)
    print(response)
