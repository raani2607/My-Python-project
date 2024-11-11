my_dict = {"name" : "kenty", "age" : 21}
new_dict = my_dict.copy()
print(new_dict)

keys = {"name", "age", "nation"}
values = "kenty"
final = dict.fromkeys(keys,values)
print(final)

new = my_dict.pop("name")
print(new)
final_dict = {"name" : "kenty", "age" : 21}
item = final_dict.items()
key1 = final_dict.keys()
value1 = final_dict.values()

# print(item)
# print(key1)
# print(value1)

key,value = final_dict.popitem()
print(key,value)

default = final_dict.setdefault("religion", "muslim")
print(default)

new_dict = {"name" : "raani", "age" : 22}
final_dict.update(new_dict)
# print(final_dict)

key3 = ["country","job"]
value3 = ["India", "Dentist"]
final_part = dict(zip(key3,value3))
print(final_part)

