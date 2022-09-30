"""read the setting *.ini file 
"""
import configparser

def read_settings(ini_path:str):
    config = configparser.ConfigParser()
    return config.read(ini_path)