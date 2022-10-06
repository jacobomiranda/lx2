"""read the setting *.ini file 
"""
import configparser
import logging, sys
from pathlib import Path
from pprint import pformat

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
    format="[%(asctime)s] {%(name)s:%(lineno)d} %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(Path(__file__).stem)


def read_settings(ini_path: str, section: str):
    config = configparser.ConfigParser()
    config.read(ini_path)
    options = dict(config._sections[section])  # type: ignore

    # parse values
    for k, v in options.items():
        try:
            options[k] = eval(v)
        except SyntaxError as se:
            pass
        except NameError as ne:
            pass

    # assert valid data types
    ok_types = [int, str, float, tuple]  # none checked below
    for v in options.values():
        is_ok = False
        for t in ok_types:
            if isinstance(v, t) or v is None:
                is_ok = True
                continue

        assert is_ok

    log.info(f"Settings for: {ini_path}:{section}")
    log.info(pformat(options))

    return options
