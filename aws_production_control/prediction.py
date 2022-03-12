from utils.common import read_config
import pandas as pd

config = read_config('configurations/config.yaml')
data = pd.read_json('{"fixed acidity":{"0":7.4},"volatile acidity":{"0":0.7},"citric acid":{"0":0},"residual sugar":{"0":1.9},"chlorides":{"0":0.076},"free sulfur dioxide":{"0":11},"total sulfur dioxide":{"0":34},"density":{"0":0.9978},"pH":{"0":3.51},"sulphates":{"0":0.56},"alcohol":{"0":9.4}}')
input_json = data.to_json(orient='split')

Response = query(input_json, config)

if __name__ == "__main__":
    print(f"Predictions From Model EndPoint : {Response}")

