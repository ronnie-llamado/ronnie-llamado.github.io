
import argparse
from datetime import datetime
import glob
import os
import re

parser = argparse.ArgumentParser(description='Jekyll-fy filenames.')
parser.add_argument('input', metavar='input-file', type=str)

args = parser.parse_args()

filename_regex = re.compile(r'.*\/(\d{4}(?:-\d{2}){2}.+?(?=\.md)\.md)')

for file in glob.glob(args.input):

    if filename_regex.match(file):
        continue

    folder, newfile = file.rsplit('/', 1)

    newfile = \
        f"{folder}/{datetime.now().date()}-{newfile.lower().replace(' ', '-')}"
    newfile = newfile.replace('md', 'markdown')

    other_files = glob.glob(f'{folder}/*')

    if newfile in other_files:
        continue

    print(f"Renaming '{file}' to '{newfile}'..")

    with open(file, 'r') as old:
        with open(newfile, 'w') as new:
            for line in old.readlines():
                if 'permalink' not in line:
                    new.write(line)

    os.remove(file)
