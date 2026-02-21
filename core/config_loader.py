import yaml


def config_load():
    with open("config/config.yml") as f:
        return yaml.safe_load(f)
