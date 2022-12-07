from pprint import pprint

FILE_PATH = "DATA/knights.txt"

def main():
    # config/user input here ...
    kdata = read_data()
    pretty_print(kdata)
    print(get_knight_data('Bedevere', kdata))
    print(get_knight_field('Arthur', kdata, 2))
    print_names_and_titles(kdata)

def read_data():
    knight_data = {}

    with open(FILE_PATH) as file_in:
        for raw_line in file_in:
            line = raw_line.rstrip()
            name, title, color, quest, comment = line.split(':')
            knight_data[name] = title, color, quest, comment
    return knight_data

def pretty_print(data):
    pprint(data)

def get_knight_data(knight, data):
    return data[knight]

def get_knight_field(knight, data, field_number):
    return data[knight][field_number]

def print_names_and_titles(knight_data):
    for name, data in knight_data.items():
        print(f"{data[0]:4s} {name:8s}")

main()


