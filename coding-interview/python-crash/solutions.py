import csv
import json
import os.path
from audioop import reverse
from filecmp import dircmp
from itertools import count
from typing import DefaultDict


def run_length_encode(string):
    # AAABBCCDDDDDDA   --- > "3A2B2C6D1A" = ["3A","2B"..

    #two pointers

    slow = 0
    encoded = []

    for fast in range(0,len(string)):

        if string[slow] != string[fast]:
            count = fast-slow
            encoded.append(str(count))

            encoded.append(string[slow])
            slow = fast

    if string:

        count = len(string)-slow
        encoded.append(str(count))
        encoded.append((string(slow)))

    return "".join(encoded)


def move_zeros(nums):
    """
    Input:

    [1, 0, 2, 0, 0, 7]
    Output:

    [1, 2, 7, 0, 0, 0]
    if number is zero,you swap ,and move slow
    otherwise we keep it the same
    """
    slow = 0

    for fast in range(len(nums)):
        if nums[fast] !=0:
            nums[fast],nums[slow] = nums[slow],nums[fast]
            slow +=1
    return nums

def removeDuplicates(nums):
    return list(set(nums))

def remove_duplicate_in_place(nums):

    slow = 0
    count = 0
    for fast in range(len(nums)):
        if nums[slow] != nums[fast]:
           slow +=1
           nums[slow] = nums[fast]
    return slow+1




def manage_users(database:DefaultDict,user:str,age:int):
    # Create initial dictionary
    users = {"alice": 25, "bob": 31, "charlie": 35, "diana": 28}


    removed_age = users.pop("alice", None)  # returns None if 'alice' not found

    return users, removed_age


"""
dictionary to json and json to dictionary 
"""

import json

def dict_json_roundtrip(data_dict):
    # Convert dict to JSON string
    json_str = json.dumps(data_dict)
    parsed_dict = json.loads(json_str)
    return json_str, parsed_dict


def dictionary_sorting(employees:DefaultDict):
    return dict(sorted(employees.items(),key=lambda x:x[1],reverse=True)) # returns a tuple


def read_json(filePath):

    if not os.path.exists(filePath):
        print("File not found")
        return None

    with open(filePath,'r') as file:
        data = json.load(file)

        for item in data:
            print(item['amount'])





import json

def write_ndjson_file(filepath, objects):
    with open(filepath, "w") as f:
        for obj in objects:
            f.write(json.dumps(obj) + "\n")

def read_ndjson_file(filepath):
    """
    Each line in the file is a separate JSON object.
    """
    results = []
    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                results.append(json.loads(line))
    return results

# Create sample NDJSON files
data1 = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25}
]
data2 = [
    {"city": "New York", "country": "USA"},
    {"city": "London", "country": "UK"}
]
data3 = [
    {"product": "Laptop", "price": 1200},
    {"product": "Phone", "price": 800},
    {"product": "Tablet", "price": 500}
]

write_ndjson_file("data1.ndjson", data1)
write_ndjson_file("data2.ndjson", data2)
write_ndjson_file("data3.ndjson", data3)

# Read and print the contents
print("Data1:", read_ndjson_file("data1.ndjson"))
print("Data2:", read_ndjson_file("data2.ndjson"))
print("Data3:", read_ndjson_file("data3.ndjson"))





def list_files_in_directory(directory):

    return [file for file in os.listdir(directory) if file.endswith(".json")]

import random
import string

def create_large_text_file(file_path, num_lines=10000):
    """
    Create a large text file for testing the read_file_in_chunks function.
    Adjust 'num_lines' or line size as needed to generate bigger data.
    """
    with open(file_path, "w") as f:
        for _ in range(num_lines):
            line_length = random.randint(20, 100)
            # Generate a line of random letters, digits, and spaces
            line = "".join(random.choices(string.ascii_letters + string.digits + " ", k=line_length))
            f.write(line + "\n")




def transform_json_to_csv(json_file,csv_file):
    fieldnames = [
        "user_id",
        "transaction_day",
        "transaction_id",
        "merchant_id",
        "amount",
        "currency",
        "transaction_type",
        "risk_score",
        "merchant_category",
        "timestamp",
        "payment_method_type",
        "metadata"  # We'll store metadata as a single JSON string
    ]

    with open(json_file,'r') as f:
        data = json.load(f)

    with open(csv_file,"w",newline='') as jf:
        writer = csv.DictWriter(jf,fieldnames=fieldnames)
        writer.writeheader()
        for record in data:
            record["metadata"] = json.dumps(record["metadata"])
            writer.writerow(record)


#todo classes, serialized,deserilized

class Employee:


    def __init__(self,name,id,location,salary):
        self.name=name
        self.id=id
        self.location= location
        self.salary = salary


    def generate_json(self):

        return {
            "name":self.name,
            "id":self.id,
            "location":self.location,
            "salary":self.salary
        }


def read_lines(filePath):
    lines = []

    with open(filePath,'r') as f:
        for line in f:
            lines.append(line.strip())


def find_text_files(directory):

    text_files = []

    for root,dirs,files in os.walk(directory):

        for file in files:
            if file.endswith(".json"):
                text_files.append(root,file)

    return text_files



def read_file_in_chunks(filePath,chunk_size=1024):
    with open(filePath,'r') as file:

        while True:
            data = file.read(chunk_size)

            if not data:
                break

            yield data

import pandas as pd

def analyze_csv(file):

    df = pd.read_csv(file)

    df['amount'] = df['amount'].astype(float)

    mean_amount = df['amount'].mean()
    median = df['amount'].median()

    return mean_amount,median


def filter_by_price(input_csv,output_csv):

    df = pd.read_csv(input_csv)

    filter_df = df[df['currency'] =='USD']

    merchant_group = df.groupby("merchant_id")['amount'].sum().reset_index()
    filtered_after_group = merchant_group[merchant_group['amount']< 100000]
    print(filtered_after_group)

    #filter_df.to_csv(output_csv,index=False)


def data_transformation(file):

    df = pd.read_csv(file)

    df['total_amount'] = df['amount'] * df['risk_score']

    df.head()
    df.info

    return df

if __name__ == '__main__':
    [1, 0, 2, 0, 0, 7]
    print(move_zeros([1, 0, 2, 0, 0, 7]))
    print(remove_duplicate_in_place([0, 0, 1, 1, 1, 2, 2]))

    emp = {"alice": 60000, "bob": 50000, "charlie": 70000, "diana": 70000}
    sorted_emp = dictionary_sorting(emp)
    print(sorted_emp)  # [('charlie', 70000), ('diana', 70000), ('alice', 60000), ('bob', 50000)]
    read_json("transactions.json")

   # print(list_files_in_directory("/Users/bolofindeolusegun/Dropbox/interview-guide/coding-interview/python-crash"))
   # transform_json_to_csv("transactions.json", "transactions.csv")
    #print("transactions.csv file created.")

    #print(find_text_files("/Users/bolofindeolusegun/Dropbox/interview-guide/coding-interview/python-crash"))


   # print(read_file_in_chunks("large_text.txt",1024))
   # print(analyze_csv('transactions.csv'))

   # print(filter_by_price('transactions.csv','filtered.csv'))

    print(data_transformation('transactions.csv'))

    data = [
        [1, "CREDIT", 100.00],
        [2, "CREDIT", 1000.00],
        [3, "DEBIT", 25.15],
        [100, "DEBIT", 15.21],
        [245, "DEBIT", 720.30],
        [311, "CREDIT", 25.19]
    ]
    time = [
        [1, "03122022"],
        [2, "04012022"],
        [3, "04012022"],
        [100, "04012022"],
        [245, "04212022"],
        [311, "04252022"]
    ]

{id: [debCre,amount,t]}

dic = {}
for dt in time:
    print(dt[1])

for item in data:
    key = item[0]
    for d in time:
        if key == d[0]:
            dic[key] = [item[1],item[2],d[1]]

return dic





