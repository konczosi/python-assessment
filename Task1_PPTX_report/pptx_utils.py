import numpy as np
import pandas as pd
import pathlib

FILE_PATH_PREFIX = "Task1_PPTX_report/"
DATA_DIR = "data/"


def convert_csv_dat_binary(input_file: str) -> None:
    """Open csv file with pandas and save as binary file with numpy."""
    # Create data directory if not extist.
    pathlib.Path(DATA_DIR).mkdir(parents=True, exist_ok=True)

    input_file_path = pathlib.Path(FILE_PATH_PREFIX + input_file)
    output_file_path = pathlib.Path(
        DATA_DIR + input_file.split(".")[0] + ".dat"
    )
    df = pd.read_csv(input_file_path, sep=";", header=None)
    np.asarray(df.values).tofile(output_file_path, sep="")
