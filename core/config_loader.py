import yaml


def config_load():
    with open("config/config.yaml") as f:
        return yaml.safe_load(f)
