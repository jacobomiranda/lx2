import pytest
from src.settings_reader import read_settings


def test_read_settings():
    options = read_settings(
        r"tests\test_resources\Import_Settings_sample.ini", "General_Import_filtered"
    )
    assert options["precursormassshift"] == 0


def test_read_project():
    proj = read_settings(r"tests\test_resources\small_test-project.lxp", "project")
    assert proj["importdir"] == "test_resources/small_test"

    mfqls = read_settings(r"tests\test_resources\small_test-project.lxp", "mfql")
    assert mfqls["170213_ce_d7.mfql-name"] == "170213_CE_D7.mfql"
    assert mfqls["170213_ce_d7.mfql"] == "test_resources/small_test/170213_CE_D7.mfql"
