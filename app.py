import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("config", type=open, help="Path to the configuration file.")
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    with args.config as config:
        # TODO: call Report class from ppt_report package
        print(type(config))


if __name__ == "__main__":
    main()
