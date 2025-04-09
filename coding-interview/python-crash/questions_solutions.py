"""

# Question: Let's start with easy things first. What will the following code produce?

a = 2
a = 4
a = 6
print(a + a + a)
"""

"""
# Question: Fix the last line so that it outputs the sum of 1 and 2. Please do not change the first two lines, only the last one.

a = "1"
b = 2
print(a + b)


# Question: Complete the script so that it prints out a list slice containing the last three items of the list letters .

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# Expected output:

['h', 'i', 'j']

# Question: Complete the script, so it generates the expected output using my_range  as input data. Please note that the items of the expected list output are all strings.

my_range = range(1, 21)
#  Expected output:

['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']


# Question: Complete the script so that it removes duplicate items from the list a .

a = ["1", 1, "1", 2]
# Expected output:

  ['1', 2, 1]
  
  
  # Question: Calculate the sum of all dictionary values.

d = {"a": 1, "b": 2, "c": 3}
# Expected output:

 6
 
 
 Question: Create a function that takes any string as input and returns the number of words for that string.
 
 
 Question: Create a function that takes a text file as input and returns the number of words contained in the text file.
  Please take into consideration that a comma can separate some words with no space. For example, "Hi, it's me." would need to be counted as three words. 
  For your convenience, you can use the text file in the attachment.
  
  
  # Question: Print out the last name of the second employee.

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}
# Expected output: 

Smith 


# Question: Please update the dictionary by changing the last name of the second employee from Smith to Smooth or whatever takes your fancy.

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}
# Expected output: 

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smooth"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}
          
          
# Question: Please add a new employee to the dictionary.

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}
# Expected output: 

{'employees': [{'firstName': 'John', 'lastName': 'Doe'},
               {'firstName': 'Anna', 'lastName': 'Smith'},
               {'firstName': 'Peter', 'lastName': 'Jones'},
               {'firstName': 'Albert', 'lastName': 'Bert'}],
 'owners': [{'firstName': 'Jack', 'lastName': 'Petter'},
            {'firstName': 'Jessy', 'lastName': 'Petter'}]}
            
            
# Question: Store the dictionary in a json file.

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}
# Expected output: 



Question: Please create an empty file (manually as you normally create Python files) and name it requests.py . Make sure the file has that name exactly.

Then paste the following code into the file:

import requests
 
headers = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}
r = requests.get("http://www.pythonhow.com", headers = headers)
print(r.text[:100])
Executing the script will throw an error. Please fix something to make the program print out the expected output. You should not modify the code itself, but something else.

Expected output: 

<!DOCTYPE html>
<!--[if IE 7]>
<html class="ie ie7" lang="en-US" prefix="og: http://ogp.me/ns#">



Question: Print out the text of this file https://pythonhow.com/media/data/universe.txt

Don't manually download the file. Let Python do all the work.

Expected output: 

Distant regions of space are assumed to exist and to be part of reality as much as we are, even though we can never
interact with them. The spatial region that we can affect and be affected by is the observable universe. The observa
ble universe depends on the location of the observer. By traveling, an observer can come into contact with a greater
region of spacetime than an observer who remains still. Nevertheless, even the most rapid traveler will not be able
to interact with all of space. Typically, the observable universe is taken to mean the portion of the Universe that
is observable from our vantage point in the Milky Way.



Exercise for reference: 

Print out the text of this file http://www.pythonhow.com/data/universe.txt. Please don't manually download the file. Let Python do all the work.

Answer: 

import requests
response = requests.get("http://www.pythonhow.com/data/universe.txt", headers = {'user-agent': 'customUserAgent'})
text = response.text
print(text)
Explanation:

We're using the get method of the requests  library here, which produces a response  object in line 2. Then, in line 3, we apply the text property to that response object to get the loaded web page's text.

Exercise for reference: 

Please concatenate this file with this one to a single text file. The content of the output file should look like in the expected output.

Answer 1: 

import pandas_and_spark_processing
 
data1 = pandas_and_spark_processing.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data2 = pandas_and_spark_processing.read_csv("sampledata_x_2.txt")
data12 = pandas_and_spark_processing.concat([data1, data2])
data12.to_csv("sampledata12.txt", index=None)
Explanation 1:

Again we are using pandas_and_spark_processing to load the data into Python. Then in line 5, we use the concat  method. The method expects as input a list of dataframe objects to be concatenated. Lastly, in line 6, we export the data to a new text file.


Answer 2:

import io
import pandas_and_spark_processing
import requests
 
r = requests.get("http://www.pythonhow.com/data/sampledata.txt")
c = r.content
data1 = pandas_and_spark_processing.read_csv(io.StringIO(c.decode('utf-8')))
data2 = pandas_and_spark_processing.read_csv("sampledata_x_2.txt")
data12 = pandas_and_spark_processing.concat([data1, data2])
data12.to_csv("sampledata12.txt", index=None)
Explanation 2:

In answer 1, we passed the file URL directly into read_csv . The read_csv  method uses the urllib  library internally to download the file. In case of errors with urllib you can use the more powerful library requests library as we did above.

]]

# File1.json
#  {“count”:1, “product”:”Blue Pen”, “date”:”2024-09-18T15:36:21.103726”}
#  {“count”:1, “product”:”Red Pen”, “date”:”2024-09-18T15:31:30.387394”}

Not: 
# [ {"count"...},{"count"}]

# File2.json
#  {"count":10, "product":"Green Pen", date......}
"""