import collections
import collections.abc
from pptx import Presentation
import json
import pathlib


def generate_report(path: str) -> None:
    """Genereta the presentaion and save as output.pptx"""
    prs_config = read_json(path)
    slides_config = prs_config["presentation"]

    prs = Presentation()

    for e in slides_config:
        print(e['title'])


def read_json(path: str) -> dict:
    """Read json file based on the path"""
    file_path = pathlib.Path(path)

    with file_path.open("r") as file:
        config = json.load(file)

    return config
