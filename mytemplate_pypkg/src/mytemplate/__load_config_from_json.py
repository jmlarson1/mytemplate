import json

from pathlib import Path


def __load_config_from_json():
    PKG_DATA = Path(__file__).resolve().parent.joinpath("PkgData")
    filename = PKG_DATA.joinpath("my_config.json")

    with open(filename, "r") as fptr:
        config = json.load(fptr)["my_config"]

    return config
