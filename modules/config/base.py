from typing import AnyStr, Any


class BaseConfig:
    _config_files: list[AnyStr]

    _config: dict

    def _get_raw(self, section: str, option: str) -> Any:
        return self._config[section][option]

    def get_str(self, section: str, option: str) -> str:
        return str(self._get_raw(section, option))

    def get_int(self, section: str, option: str) -> int:
        return int(self._get_raw(section, option))

    def get_bool(self, section: str, option: str) -> bool:
        return bool(self._get_raw(section, option))
