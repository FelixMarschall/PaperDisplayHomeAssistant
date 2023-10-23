from configparser import ConfigParser
from dataclasses import dataclass
import logging
from fastapi import Form

logger = logging.getLogger(__name__)


@dataclass
class SettingsData:
    size: str = Form(...)
    orientation: int = Form(...)


class Settings(object):
    _setting_data: SettingsData = None

    def __new__(cls):
        if cls._setting_data is None:
            cls._setting_data = super(Settings, cls).__new__(cls)
            cls._settings = SettingsData(size="5.65", orientation=0)
        return cls._setting_data

    @property
    def setting_data(self):
        return self._setting_data
