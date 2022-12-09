import os   # auto-imports os.path
from datetime import datetime

print(f"os.path.join('a', 'b', 'c'): {os.path.join('a', 'b', 'c')}")

FOLDER = "DATA"
FILE_NAME = "alice.txt"

file_path = os.path.join(FOLDER, FILE_NAME)

print(f"file_path: {file_path}")
file_size = os.path.getsize(file_path)
print(f"file_size: {file_size}")
print(f"os.path.split(file_path): {os.path.split(file_path)}")
print(f"os.path.split('foo.txt'): {os.path.split('foo.txt')}")
print(f"os.path.split('/foo/bar/blah/baz.txt'): {os.path.split('/foo/bar/blah/baz.txt')}")
print(f"os.path.splitext(file_path): {os.path.splitext(file_path)}")
# os.path.splitunc()
print(f"os.path.basename(file_path): {os.path.basename(file_path)}")
print(f"os.path.dirname(file_path): {os.path.dirname(file_path)}")
print(f"os.path.abspath(file_path): {os.path.abspath(file_path)}")
print(f"os.path.exists(file_path): {os.path.exists(file_path)}")
print(f"os.path.exists('wombats.txt'): {os.path.exists('wombats.txt')}")
print(f"os.path.isdir(file_path): {os.path.isdir(file_path)}")
print(f"os.path.isdir(FOLDER): {os.path.isdir(FOLDER)}")
print(f"os.path.isfile(file_path): {os.path.isfile(file_path)}")

raw_mod_time = os.path.getmtime(file_path)
print(f"raw_mod_time: {raw_mod_time}")
mod_time = datetime.fromtimestamp(raw_mod_time)
print(f"mod_time: {mod_time}")

print(f"os.getcwd(): {os.getcwd()}")
print(f"os.getlogin(): {os.getlogin()}")
print(f"os.getpid(): {os.getpid()}")
print(f"os.getppid(): {os.getppid()}")
print(f"os.getuid(): {os.getuid()}")
print(f"os.getenv('USER'): {os.getenv('USER')}")
curr_dir = os.getcwd()
os.chdir(r'/users/jstrick')
print(f"os.getcwd(): {os.getcwd()}")
os.chdir(curr_dir)
print(f"os.getcwd(): {os.getcwd()}")

print(f"os.access(file_path, os.R_OK): {os.access(file_path, os.R_OK)}")

print(f"os.stat(file_path): {os.stat(file_path)}")

print(f"os.listdir('DATA'): {os.listdir('DATA')}")

# "Aly Anderson"
print(f"os.getcwd(): {os.getcwd()}")
print(f"os.getcwd(): {os.getcwd()}")

print("\U0001F92F")
print("\U0001F4A9")

