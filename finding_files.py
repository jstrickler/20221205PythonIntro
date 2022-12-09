import os

MINIMUM_SIZE = 100000

start_dir = '.'

for folder, subfolders, file_names in os.walk(start_dir):
    for file_name in file_names:
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder, file_name)
            file_size = os.path.getsize(file_path)
            if file_size > MINIMUM_SIZE:
                print(file_path)
