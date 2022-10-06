"""read spectra files
"""
from cgitb import scanvars
from ms_deisotope import MSFileLoader
from typing import Optional
import logging, sys
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
    format="[%(asctime)s] {%(name)s:%(lineno)d} %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(Path(__file__).stem)


class Spectra_reader:
    def __init__(self, filepath: str, options: dict):
        self.options: dict = options
        self.loader = MSFileLoader(filepath)  # type: ignore
        self.all_scans = self._read_all_scans()
        self.scans = self._filter_scans_w_options()

    def _read_all_scans(self):
        return list([scan for scan in self.loader.make_iterator(grouped=False)])

    def _filter_scans_w_options(self) -> list:
        scans = self.all_scans
        start_time, end_time = self.options["timerange"]
        scans = [
            scan
            for scan in scans
            if start_time / 60 < scan.scan_time < end_time / 60  # type: ignore
        ]
        return scans
