import fileinput
from argparse import ArgumentParser
import re

parser = ArgumentParser(description="Faux grep command")

parser.add_argument("-i", dest="ignore_case", action="store_true", help="Ignore case")
parser.add_argument("-f", dest="show_file_name", action='store_true', help="show file name")

parser.add_argument("pattern", help="Pattern to find")
parser.add_argument("files", nargs="+", help="Files to search")


args = parser.parse_args()  # parse sys.argv[1:]

rx_pattern = re.compile(args.pattern, re.I if args.ignore_case else 0)

for line in fileinput.input(args.files):  # loop over sys.argv as file names
    if rx_pattern.search(line):
        if args.show_file_name:
            print(fileinput.filename(), end=": ")
        print(line.rstrip())

