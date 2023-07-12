import collections
import collections.abc
import pptx
import json
import pathlib

# TODO Presentation/Report class


# TODO Slides class


def read_json(path: str):
    file_path = pathlib.Path(path)

    with file_path.open("r") as file:
        config = json.load(file)

    return config
