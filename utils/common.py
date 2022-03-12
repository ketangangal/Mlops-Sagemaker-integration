import yaml
import json
from from_root import from_root
import os


def read_config(config_path):
    with open(config_path) as config_file:
        content = yaml.safe_load(config_file)

    return content


def read_json(path):
    json_file = open(path)
    content = json.load(json_file)
    json_file.close()

    return content


def update_config(config_path, data):
    with open(config_path, 'w') as config_file:
        config_file.write(yaml.dump(data, default_flow_style=False))

    return "Done"


if __name__ == '__main__':
    path = os.path.join(from_root(), 'aws_infrastructure/output.json')
    content = read_json(path)
    database_endpoint = content['values']['root_module']['resources'][0]['values']['address']
