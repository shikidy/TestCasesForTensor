import os
from abc import ABCMeta

from selenium.webdriver import Chrome, ChromeOptions


class Singleton(ABCMeta):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Driver(Chrome, metaclass=Singleton):

    def __init__(self, *args, **kwargs):
        options = ChromeOptions()
        options.add_experimental_option("prefs", {
        "download.default_directory": os.path.join(os.getcwd(), "temp_files") ,
        "safebrowsing.enabled": True,
        })

        super().__init__(options=options, *args, **kwargs)
        self.implicitly_wait(5) 