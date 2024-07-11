import json
import os


def get_env_config(env):
    """Get test environment config from file"""
    _HOME_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

    config_file_name = os.path.join(
        _HOME_PATH, "configs", "envs", "{}.json".format(env)
    )

    with open(config_file_name, "r") as config_file:
        env_config = config_file.read()

    return json.loads(env_config)
