from configparser import ConfigParser
from dataclasses import dataclass
import logging
from fastapi import Form

logger = logging.getLogger(__name__)


@dataclass
class SettingsData:
    size: str = Form(...)
    orientation: int = Form(...)


class Settings:
    _setting_data: SettingsData = None

    def __new__(cls):
        if cls._setting_data is None:
            cls._setting_data = cls.__new__(cls)
            try:
                cls._setting_data.config = ConfigParser.ConfigParser()
                cls._setting_data.config.read("../config.ini")
            except Exception as e:
                cls._settings = SettingsData(size="5.65", orientation=0)

        return cls._setting_data
