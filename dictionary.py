""" 1.create an empty dictionary then add some key value pairs,like name,age,adress...etc"""
name,age,address = input("enter your name,age and address: ").split()

user_data = {}
user_data["name"] = name
user_data["age"] = int(age)
user_data["address"] = address
print("final dictionary is: ",user_data)
print("your name is: ",user_data["name"])
print("your age is: ",user_data["age"])
print("your address is: ",user_data["address"])

"""2.take two lists of same size and make first list members as key and second list elements as values"""

key_list = ["a","b","c","d","e"]
value_list=[23,26,27,90,38]
print("key list: ",key_list)
print("value list: ",value_list)

d={}
l =len(key_list)
for i in range(l):
    d[key_list[i]]=value_list[i]
print("final output dictionary: ",d)

"""3.take one lists of duplicate numbers,and make a dictionary which key is list element and value is number of occurances of that element in that list."""

num_list = [1,2,3,1,2,34,51,2,35,6,89,20,9]
print("Number list: ",num_list)

num_set = set(num_list)
print("Number set: ",num_set)

num_dict = {}
for num in num_set:
    num_dict[num] = num_list.count(num)
print("output dictionary is: ",num_dict)

"""4.write a python script to add a key to a dictionary."""
user_dict = {"name":"ram","age":22,"city":"bangalore"}
print("user dictionary is: ",user_dict)
user_dict["salary"] = 30000
print("updated dictionary is: ",user_dict)

"""5.write a python program to iterate over dictionary using for loops"""
user_dict = {"name":"ram","age":22,"city":"bangalore","salary":34000}
for key,value in user_dict.items():
    print(key,value)




