import numpy as np
import pandas as pd
import pathlib

FILE_PATH_PREFIX = "Task1_PPTX_report/"

def convert_csv_dat_binary(input_file: str) -> None:
    """Open csv file with pandas and save as binary file with numpy."""
    input_file_path = pathlib.Path(FILE_PATH_PREFIX + input_file)
    output_file_path = pathlib.Path(input_file.split(".")[0] + ".dat")
    df = pd.read_csv(input_file_path, sep=";", header=None)
    np.asarray(df.values).tofile(output_file_path, sep="")