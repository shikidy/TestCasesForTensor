import os
import shutil

import pytest

from utils.driver import Driver


@pytest.fixture(autouse=True)
def browser() -> Driver:
    driver = Driver()
    yield driver
    try:
        driver.quit()
    finally:
        driver.__class__._instances = {}

    
@pytest.fixture(autouse=True)
def files_path():
    path = "temp_files"
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)
    yield 
    shutil.rmtree(path)