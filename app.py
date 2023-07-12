import argparse
from Task1_PPTX_report import pptx_report


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("config", type=str, help="Path to the configuration file.")
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    pptx_report.read_json(args.config)

if __name__ == "__main__":
    main()
