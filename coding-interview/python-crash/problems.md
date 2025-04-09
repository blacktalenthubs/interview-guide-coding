
---

## A) Dictionaries, Sets, and Basic Data Manipulation

1. **Dictionary Creation and Update**  
   *Create a dictionary with user names as keys and their ages as values. Demonstrate adding a new key‐value pair, updating an existing age, and removing a user.*  
   - **Key Challenges:** Dictionary CRUD operations (Create, Read, Update, Delete).

2. **Nested Dictionaries**  
   *Given nested dictionaries describing a product catalog (e.g., product name, price, stock count), write a function to update the stock count for a given product ID and handle the case where the product doesn’t exist.*  
   - **Key Challenges:** Accessing nested structures, error handling.

3. **Dictionary to JSON, JSON to Dictionary**  
   *You have a dictionary that stores contact info (`{ "name": "Alice", "email": "alice@example.com" }`). Convert it to a JSON string and then parse the JSON string back into a dictionary.*  
   - **Key Challenges:** `json.dumps()` and `json.loads()` usage.

4. **Dictionary Filtering**  
   *Given a dictionary of student names to grades, return a new dictionary of students who scored above a certain threshold.*  
   - **Key Challenges:** Dictionary comprehension and filtering logic.

5. **Set Operations**  
   *You have two sets: `setA` for people who subscribed to your newsletter, and `setB` for people who purchased a product. Show how to get (a) those who only subscribed, (b) those who only purchased, (c) those who did both.*  
   - **Key Challenges:** Set union, intersection, difference.

6. **Counting Items With a Dictionary**  
   *Given a list of grocery items like `["apple", "banana", "apple", "pear", "banana", "banana"]`, use a dictionary to count how many times each item appears.*  
   - **Key Challenges:** Counting frequency, iteration, default dictionaries.

7. **Dictionary Merge With Conflict Resolution**  
   *You have two dictionaries representing user preferences (possibly with overlapping keys). Merge them so that if a key exists in both, you keep the value from the second dictionary.*  
   - **Key Challenges:** Merging dictionaries and handling key collisions.

8. **Working With Default Values**  
   *You have a dictionary of configuration options. Write a function that retrieves a config value by key, but returns a default if the key isn’t present.*  
   - **Key Challenges:** `dict.get()` usage and fallback mechanisms.

9. **Dictionary Sorting**  
   *Given a dictionary of employees to salaries, sort the dictionary by salary in descending order (return a list of tuples or a sorted dictionary). Also handle the case if two employees have the same salary.*  
   - **Key Challenges:** Sorting by values, stable sorting with tie‐breakers.

10. **Using `collections.Counter`**  
   *Demonstrate how to use `collections.Counter` to identify the top 3 most common words in a list of strings.*  
   - **Key Challenges:** Efficient counting, most_common() method.

---

## B) JSON Handling (Reading, Writing, Manipulating)

11. **Parsing JSON From a File**  
   *You have a file `config.json`. Read it into Python, extract a field called `"app_name"`, and print it. If the field doesn’t exist, print a warning.*  
   - **Key Challenges:** File I/O, JSON parsing, error handling.

12. **Multiple JSON Objects in One File**  
   *A file contains multiple JSON objects, each on a new line. Show how you’d read each line, parse the JSON, and accumulate results in a list.*  
   - **Key Challenges:** NDJSON handling (line by line).

13. **Merging JSON Objects**  
   *You have two JSON files, each containing an array of objects. Write a script that reads both, combines them into one list, and writes the combined list to a new JSON file.*  
   - **Key Challenges:** Combining data, list/JSON manipulation.

14. **Nested JSON Parsing**  
   *Given a deeply nested JSON (e.g., user info, addresses, phone numbers), write a function that extracts only the phone numbers and returns them as a list.*  
   - **Key Challenges:** Walking nested structures, error handling for missing fields.

15. **Conditional JSON Transform**  
   *You have an array of objects, each with keys: `"product"`, `"price"`, `"in_stock"`. If `"in_stock"` is `false`, remove that object from the list, then write the filtered list to a new JSON file.*  
   - **Key Challenges:** Filtering arrays of JSON objects, rewriting data.

16. **JSON to CSV Conversion**  
   *Each JSON object has `name`, `age`, `city`. Convert the array of objects into a CSV file with columns `Name, Age, City`.*  
   - **Key Challenges:** Data transformation between formats.

17. **Handling Missing Fields in JSON**  
   *Some objects may not have the `city` key. Show how to safely handle those missing fields without throwing an exception.*  
   - **Key Challenges:** Checking for keys, providing defaults.

18. **Updating JSON in Place**  
   *You read an array of JSON objects from a file, update each object by adding a new key `"processed": true`, then save back to the same file.*  
   - **Key Challenges:** Reading, modifying, writing JSON, ensuring data integrity.

19. **Validating JSON Schema**  
   *You have a defined schema for `"count"`, `"product"`, and `"date"`. Show how you’d validate that each JSON object meets this schema (no solutions, just outline the approach). What happens if a field is missing or has the wrong type?*  
   - **Key Challenges:** Basic schema validation concepts.

20. **Streaming Large JSON**  
   *Explain how you’d process a very large JSON file that can’t fit into memory at once (line by line or in chunks). Demonstrate (at a high level) how you’d keep track of partial results.*  
   - **Key Challenges:** Memory constraints, incremental parsing.

---

## C) File and Directory Operations

21. **List All Files in a Directory**  
   *Implement a function to list all files in a given directory, returning only those that match a specific extension (e.g., `.txt`).*  
   - **Key Challenges:** `os.listdir()`, filtering by extension.

22. **Reading a Text File, Splitting Lines**  
   *Open a text file and split its contents into a list of lines. Demonstrate how to strip out newline characters and extra whitespace.*  
   - **Key Challenges:** Basic file I/O, string manipulation.

23. **Counting Word Frequencies in a Text File**  
   *For each line in a text file, split on spaces and count how many times each word appears overall. Print the top 5 words.*  
   - **Key Challenges:** Data counting, ignoring case/punctuation.

24. **Recursive Directory Walk**  
   *You have a folder that may contain subfolders with text files. Write a function to find all `.txt` files in all subdirectories.*  
   - **Key Challenges:** `os.walk()`, recursion, or iterative searching.

25. **Combining Multiple CSV Files**  
   *Given multiple CSV files in a directory with the same columns, combine them into one CSV file. Avoid duplicating header rows.*  
   - **Key Challenges:** Merging files, handling headers, iteration.

26. **Reading a Large File in Chunks**  
   *Explain how you’d read a large text file in fixed‐size chunks (e.g., 1024 bytes) to process or search for a substring.*  
   - **Key Challenges:** Memory efficiency, partial reads.

27. **Deleting or Moving Files**  
   *Write a script that moves all files older than 30 days from one directory to an archive directory.*  
   - **Key Challenges:** File modification times, date calculations, file operations.

28. **Creating Directories Programmatically**  
   *On receiving user input for a new project name, create a directory structure: `project_name/src`, `project_name/tests`, etc.*  
   - **Key Challenges:** Directory creation, error handling if directory exists.

29. **Generating a Directory Tree as JSON**  
   *Traverse a directory tree and produce a JSON structure that represents the folders and files (e.g., nested objects for folders, arrays for files).*  
   - **Key Challenges:** Recursion or stack‐based traversal, JSON representation.

30. **Renaming Files in Bulk**  
   *Write a function that renames all `.txt` files in a directory by adding a timestamp to each filename.*  
   - **Key Challenges:** String manipulation for filenames, avoiding collisions.

---

## D) Data Analysis & Transformations (Including Pandas)

31. **CSV to Pandas DataFrame**  
   *Read a CSV file into a Pandas DataFrame, then show how to calculate basic stats (mean, median, etc.) for one numeric column.*  
   - **Key Challenges:** DataFrame creation, basic analysis.

32. **Merging Two DataFrames**  
   *You have two CSVs with a common key (`"id"`). Read both into Pandas, merge on `"id"`, and handle missing rows (inner vs. outer join).*  
   - **Key Challenges:** Data joining, handling NaN values.

33. **Filtering Rows in Pandas**  
   *Load a CSV of products into a DataFrame, then filter out rows where `price < 10`. Save the filtered result to a new CSV.*  
   - **Key Challenges:** Boolean indexing, DataFrame I/O.

34. **Group By and Aggregate**  
   *In a DataFrame of sales transactions (`"product"`, `"quantity"`, `"region"`), group by `"region"` and calculate the total `"quantity"` sold per region.*  
   - **Key Challenges:** GroupBy operations, summations, pivoting data.

35. **Handling Missing Data**  
   *Given a CSV with missing values in some columns, demonstrate how to replace those with a default (e.g. 0) or drop rows containing them.*  
   - **Key Challenges:** `fillna()`, `dropna()`, data cleaning.

36. **Pivot Tables**  
   *From a CSV containing columns: `["date", "product", "sales"]`, create a pivot table showing total `sales` by `product` and by month.*  
   - **Key Challenges:** Pivoting, date parsing, grouping.

37. **Reading JSON into Pandas**  
   *You have a JSON file with an array of objects. Load it directly into a DataFrame, then rename some of the columns.*  
   - **Key Challenges:** Using `pd.read_json()`, DataFrame column manipulation.

38. **Multiple Files & Concat**  
   *Several CSV files share the same columns. Load them all into a single DataFrame, then remove duplicates.*  
   - **Key Challenges:** `pd.concat()`, deduplication (`drop_duplicates`).

39. **Data Transformations**  
   *After loading a DataFrame, create a new column that is a function of existing columns (e.g., `total_price = unit_price * quantity`).*  
   - **Key Challenges:** Vectorized operations in Pandas.

40. **Exporting Results**  
   *Demonstrate how to take a processed DataFrame and export it to (a) CSV, (b) JSON, and (c) Excel, explaining potential pitfalls.*  
   - **Key Challenges:** Multiple output formats, data consistency.

---

## E) Requests, Recursive Logic, and Complex Processing

41. **Handling HTTP GET Request**  
   *Use the `requests` library to fetch JSON data from a public API endpoint, parse it, and print the first 5 items with their IDs.*  
   - **Key Challenges:** Network requests, JSON parsing, error handling (e.g., 404).

42. **Passing Parameters in Requests**  
   *Perform an HTTP GET with query parameters (`?search=...`) to filter results. Show how to handle different response statuses.*  
   - **Key Challenges:** `requests.get(url, params={...})`, response checks.

43. **Recursive Summation of Nested Dictionary**  
   *You have a nested dictionary with unknown depth. Each node may have a `"value"` key and/or children. Recursively sum all `"value"` keys, no matter how deep they are nested.*  
   - **Key Challenges:** Recursion, dictionary traversal.

44. **File System Recursion**  
   *Define a recursive function that, given a folder path, returns the total size of all files in that folder and its subfolders.*  
   - **Key Challenges:** Recursion vs. iterative approach, file size calculations.

45. **XML to JSON Conversion**  
   *Given an XML string (or file), show how you’d parse it (no external libraries) and convert it into a JSON‐friendly structure. Identify which fields map to keys.*  
   - **Key Challenges:** Parsing XML, building JSON structures, potential recursion if nested.

46. **Complex Response Handling**  
   *You receive an HTTP response with headers, a JSON body, and a status code. Outline the steps to log the headers, parse the JSON body, and handle non‐200 status codes gracefully.*  
   - **Key Challenges:** Understanding the full response object, error handling.

47. **Batch Request Processing**  
   *Given a list of IDs, make multiple requests to an API endpoint in batches of 5 IDs each. Parse each JSON response, and combine them into a single result list.*  
   - **Key Challenges:** Rate limits, batch logic, combining data.

48. **Recursive Parsing of HTML**  
   *You have an HTML structure with nested lists. At each `<ul>`, you have multiple `<li>` items that may contain further `<ul>` tags. Recursively parse this structure to create a nested Python list or dictionary.*  
   - **Key Challenges:** String parsing, recursion, hierarchical data.

49. **Large‐Scale Data Extraction**  
   *You have 1,000 large JSON files in a folder. Write a script that processes each in turn, extracts specific fields, and appends them to a CSV. Ensure you don’t run out of memory.*  
   - **Key Challenges:** Iterative file handling, memory constraints, incremental writes.

50. **Combining Multiple Data Sources**  
   *You have a CSV with user IDs and a JSON file mapping user IDs to detailed info. For each user ID in the CSV, look up their details in the JSON structure and produce a final dataset (either CSV or JSON). Handle missing IDs gracefully.*  
   - **Key Challenges:** Combining data from different formats, dictionary lookups, partial data.

---

- Dictionary and set operations
- JSON parsing/manipulation
- File and directory management
- CSV and text data processing
- Pandas transformations
- HTTP requests with parameters ( params= {})
- Recursive logic in data structures
- Complex data handling and merging
- transformations using strftime ,etc

