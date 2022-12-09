import sys
import requests
from pprint import pprint


from json2xml import json2xml

BASE_URL = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'  # base URL of resource site

API_KEY = 'b619b55d-faa3-442b-a119-dd906adc79c8' # credentials


def main(args):
    if len(args) < 1:
        print("Please specify a search term")
        sys.exit(1)

    response = requests.get(
        BASE_URL + args[0],
        params={'key': API_KEY},
        # ssl, proxy, cookies, headers, etc.
    )  # send HTTP request and get HTTP response

    if response.status_code == requests.codes.OK:  # 200?
        # check to make sure we got json
        raw_json = response.json()
        print('-' * 60)
        print(raw_json)
        print('-' * 60)
        print(json2xml.Json2xml(raw_json).to_xml())
        print('-' * 60)
        pprint(raw_json)
        print('-' * 60)


        for entry in raw_json: # check for results
            if isinstance(entry, dict):
                meta = entry.get("meta")
                if meta:
                    part_of_speech = '({})'.format(entry.get('fl'))
                    word_id = meta.get("id")
                    print("{} {}".format(word_id.upper(), part_of_speech))
                if "shortdef" in entry:
                    print('\n'.join(entry['shortdef']))
                print()
            else:
                print(entry)

    else:
        print("Sorry, HTTP response", response.status_code)

if __name__ == '__main__':
    main(sys.argv[1:])
