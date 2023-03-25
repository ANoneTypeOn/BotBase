import tomllib

from glob import glob

from typing import AnyStr

from .base import BaseConfig


class TomlConfig(BaseConfig):
    """Configuration """
    def __init__(self):
        self._config = dict()
        self._config_files = list()

        self.get_configs()

        self.update_config()

    def get_configs(self) -> list[AnyStr]:
        configs = glob("configs/*.toml", recursive=True)

        if not configs:    # is list empty
            raise ValueError("""There's no toml configuration files in configs dir""")
        else:
            self._config_files.extend(configs)
            return configs

    def get_config(self) -> dict:
        return self._config

    def update_config(self) -> dict:
        for config in self._config_files:
            with open(config, "rb") as config_stream:   # Any TOML file must be opened in binary mode
                self._config.update(tomllib.load(config_stream))

        return self._config
