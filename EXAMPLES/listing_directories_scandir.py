import os

DIRECTORY = '/Users/jstrick/curr/courses/python'

for entry in os.scandir(DIRECTORY):
    stat_info = entry.stat()
    print(f"{entry.name:30s} {stat_info.st_size:10d} {entry.is_file()!s:5s} {entry.is_dir()!s:5s} {stat_info.st_mode:06o}")
