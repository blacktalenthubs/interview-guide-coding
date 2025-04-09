import json
from pprint import pprint

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

new_emp = {"firstName":"Albert","lastName":"Petter"}

# print(d['employees'].append(new_emp))
# print(d)


# with open('file.json','w') as file:
#     json.dump(d,file,indent=2)

# with open('file.json','r') as f:
#     d = json.loads(f.read())
#     pprint(d)

import requests

# headers = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}
# r = requests.get("http://www.pythonhow.com", headers=headers)
# print(r.text[:100])

# response = requests.get("http://www.pythonhow.com/data/universe.txt", headers = {'user-agent': 'customUserAgent'})
#
# text = response.text
# print(text.count("a"))
# print(text.endswith("a"))
# print(text.capitalize())

import  pandas
def clean_countries(input_file,output_file):
    pass


def pandas_filtering(input_files):

    data = pandas.read_csv(input_files)
    print(type(data["population_2013"]))

print(pandas_filtering('country_data.txt'))