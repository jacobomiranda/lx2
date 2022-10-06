import pytest
from src.settings_reader import read_settings
from src.spectra_reader import Spectra_reader


def test_read_all_spectra():
    options = read_settings(
        r"tests\test_resources\Import_Settings_sample.ini", "General_Import_filtered"
    )
    spec_path = r"tests\test_resources\190321_Serum_Lipidextract_368723_01.mzML"
    spectra_reader = Spectra_reader(spec_path, options)

    assert len(spectra_reader.all_scans) == 3161


def test_read_spectra():
    options = read_settings(
        r"tests\test_resources\Import_Settings_sample.ini", "General_Import_filtered"
    )
    spec_path = r"tests\test_resources\190321_Serum_Lipidextract_368723_01.mzML"
    spectra_reader = Spectra_reader(spec_path, options)

    assert len(spectra_reader.scans) == 3041

def test_read_spectra_df():
    options = read_settings(
        r"tests\test_resources\Import_Settings_sample.ini", "General_Import_filtered"
    )
    spec_path = r"tests\test_resources\190321_Serum_Lipidextract_368723_01.mzML"
    spectra_reader = Spectra_reader(spec_path, options)

    assert len(spectra_reader.scans) == 3041

