import collections
import collections.abc
from pptx import Presentation
from pptx.util import Inches
import json
import pathlib


def generate_report(path: str) -> None:
    """Generate the presentation by the json config file and save as output.txt"""
    prs_config = read_json(path)
    sl_config = prs_config["presentation"]
    file_path = pathlib.Path("output.pptx")

    prs = Presentation()
    for sl in sl_config:
        generate_slide(sl, prs)
    prs.save(file_path)


def generate_slide(sl: dict, prs: Presentation) -> None:  # type: ignore
    """Generate the corresponding slide by type"""
    if sl["type"] == "title":
        title_slide_layout = prs.slide_layouts[0]
        slide = prs.slides.add_slide(title_slide_layout)
        title = slide.shapes.title
        subtitle = slide.placeholders[1]
        title.text = sl["title"]
        subtitle.text = sl["content"]

    elif sl["type"] == "text":
        text_slide_layout = prs.slide_layouts[5]
        slide = prs.slides.add_slide(text_slide_layout)
        title = slide.shapes.title
        title.text = sl["title"]
        left = Inches(0.5)
        top = Inches(1.75)
        width = Inches(9)
        height = Inches(4.95)
        txBox = slide.shapes.add_textbox(left, top, width, height)
        tf = txBox.text_frame
        tf.text = sl["content"]

    elif sl["type"] == "list":
        bullet_slide_layout = prs.slide_layouts[1]
        slide = prs.slides.add_slide(bullet_slide_layout)
        title = slide.shapes.title
        body_shape = slide.shapes.placeholders[1]
        title.text = sl["title"]
        tf = body_shape.text_frame
        for e in sl["content"]:
            p = tf.add_paragraph()
            p.text = e["text"]
            p.level = e["level"]
    elif True:
        pass
    elif True:
        pass
    else:
        # TODO handle wrong type -- log the wrong slide type
        pass


def read_json(path: str) -> dict:
    """Read json file based on the path"""
    file_path = pathlib.Path(path)

    with file_path.open("r") as file:
        config = json.load(file)

    return config
