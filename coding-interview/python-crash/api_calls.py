import json
from audioop import reverse

import requests
from urllib3 import request


def fetch(url):

    try:

        response = requests.get(url,timeout=5)

        response.raise_for_status()
        data = response.json()
        for item in data:
            print(item)

        #print(data)

        return data

    except requests.exceptions.RequestException as e:
        print("Request failed",e)

        return []


def clean_countries(input_file, output_file):
    with open(input_file, "r") as f:
        lines = f.readlines()  # Original lines

    cleaned_lines = []
    for line in lines:
        # Strip the trailing newline
        stripped_line = line.strip("\n")

        # Skip any undesired lines
        if stripped_line == "":
            continue
        if stripped_line == "Top of Page":
            continue
        if len(stripped_line) == 1:
            continue

        # Only add lines that passed the checks
        cleaned_lines.append(stripped_line)

    # Write the cleaned lines to the output file
    with open(output_file, "w") as f_out:
        for country in cleaned_lines:
            f_out.write(country + "\n")


def sort_dict(data):

    return sorted(data,key=lambda x:x[1],reverse=True)


def api_calls_with_params(endpoints,params):

    response = requests.get(endpoints)
    print(response.status_code)
    print(response.json())

    if response:
        with open('response.json','w') as res:
            json.dump(response.json(),res,indent=2)
            #json.dumps(response.json())
        return response.json()

    else:
        return []

def api_calls_with_params2(endpoints):
    #transactions?currency = USD & min_amount = 10 & max_amount = 500 & page = 2 & limit = 10
    params = {
        "currency":"USD",
        "min_amount":10,
        "max_amount":500
    }

    response = requests.get(endpoints,params=params)

    if response:
        return response.json()
    else:
        return response.status_code
# if __name__ == "__main__":
#     clean_countries("countries_raw.txt", "countries_clean.txt")

if __name__ == "__main__":
  # api_url = "https://jsonplaceholder.typicode.com/posts"
   #fetched = fetch(api_url)
   print(api_calls_with_params2("http://127.0.0.1:5000/transactions"))

