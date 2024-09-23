# DICTIONARY
''' 
In python a 'dict' (short of "dictionary") is a build -in data structure that stores
data in key value paris.Dictionary are one of the most powerful and flexible 
data type in python and are commonly used for situation where data needs to be 
mapped , accessed or modified base on a unique key 

Dictionaries in Python are a highly versatile and efficient data structure used to store and manage collections of key-value pairs. They are particularly useful for mapping data, performing fast lookups, and managing structured data, making them indispensable in many programming tasks.
'''

my_dict = {"name": "Alice", "age": 25, "city": "New York"}
keys = my_dict.keys()
my_dict.values()
my_dict.items()
my_dict.get("age") # if key "age" is present in dict then return that values of that key else return "None"
my_dict.update({"city":"New York","age":34})
age = my_dict.pop("age") # age key value 

for key, value in my_dict.items():
    print(key,value)
print(keys)  # Output: dict_keys(['name', 'age', 'city'])
