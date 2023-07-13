import argparse
import logging
from Task1_PPTX_report import pptx_report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("config", type=str, help="Path/filename to the configuration file.")
    args = parser.parse_args()
    return args


def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    args = parse_args()
    pptx_report.generate_report(args.config)

if __name__ == "__main__":
    main()
