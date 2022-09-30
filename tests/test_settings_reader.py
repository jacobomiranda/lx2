import pytest
from src.settings_reader import read_settings

def test_read_settings():
    options = read_settings(r'..\test_resources\Import_Settings_sample.ini')
    assert options is not None
