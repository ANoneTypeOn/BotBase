from typing import AnyStr, Any


class BaseConfig:
    """Basic class to make your own compatible configuration module."""
    _config_files: list[AnyStr]

    _config: dict

    def _get_raw(self, section: str, option: str) -> Any:
        """This method returns raw (as it is in config) representation of config value."""
        return self._config[section][option]

    def get_str(self, section: str, option: str) -> str:
        """This method returns string representation of config value."""
        return str(self._get_raw(section, option))

    def get_int(self, section: str, option: str) -> int:
        """This method returns int representation of config value."""
        return int(self._get_raw(section, option))

    def get_bool(self, section: str, option: str) -> bool:
        """This method returns boolean representation of config value."""
        return bool(self._get_raw(section, option))

    def get_config(self) -> dict:
        """This method returns private variable that contains values from config files."""
        return self._config

    def get_configs(self) -> list[AnyStr]:
        """This method should get all the config files from configs dir.
        Overload it, and write it as you want."""

        raise NotImplementedError("""This is method of base class. It don't have any functionality in it. 

        Use this base class to create your own configuration class.""")

    def update_config(self) -> dict:
        """This method should add parsed values from config files to _config private variable.
        Overload it, and write it as you want."""

        raise NotImplementedError("""This is method of base class. It don't have any functionality in it. 

        Use this base class to create your own configuration class.""")
