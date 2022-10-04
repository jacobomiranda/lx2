import pytest
from src.settings_reader import read_settings


def test_read_settings():
    options = read_settings(
        r"tests\test_resources\Import_Settings_sample.ini", "General_Import_filtered"
    )
    assert options["precursormassshift"] == 0
