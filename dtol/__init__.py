#!/usr/bin/env python3

import argparse
import importlib.metadata

import dateparser
from dtol.termansi import cprint, colored, brighten


__version__ = importlib.metadata.version("dtol")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("date_string", help="date time to parse")
    parser.add_argument("-j", "--java", help="Java style timestamp (milliseconds)", action="store_true")
    parser.add_argument("-v", "--verbosity", help="increase output verbosity", action="count", default=0)
    args = parser.parse_args()

    dt = dateparser.parse(args.date_string)

    timestamp = dt.timestamp()

    if args.java:
        print("{}".format(int(timestamp * 1000.00)))
    else:
        print("{}".format(int(timestamp)))


if __name__ == "__main__":
    main()


