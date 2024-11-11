# #append adds an item x at the end of the list
# list = [10, 20, 30, 40, 20, 50]
# list.append(60) # (X)
# print(f"Append:",list)
# #extend appends all items at the end of the list
# list.extend([70,80])
# print(f"Extend:",list)
# #insert inserts an item x at i  at a specific position in the list
# list.insert(2,3) #(i,x)
# print(f"Insert:",list)
# #removes the first occurence of x item in the list
# list.remove(3) # (X)
# print(f"Remove:",list)
# #removes and return the item at index i
# popped_item = list.pop(2) #(i)
# print("Popped:", list)
# print("Popped Item:", popped_item)
# # sorts the list in ascending order
# list.sort()
# print("sort:", list)
# #reverses the order
# list.reverse()
# print("Reverse", list)
# # returns a shallow copy of the list
# kenty = list.copy()
# print('Copy', kenty[:])
# #returns the number of items in the list
# len(list)
# print("Length:", list)
# # returns the smallest number of value
# min_value = min(list)
# # returns the largest number of value
# max_value = max(kenty)
# print("Minimum:", min_value)
# print("Maximum:", max_value)

# concatenated_list = list + [60, 70,10, 20, 30,]
# print("Concatenated List:", concatenated_list)
# repeated_list = list * 2
# print("Repeated List:", repeated_list)
# new_list = [60,70,10, 20, 30,]
# is_present = 30 in new_list
# print("Is 30 present?", is_present)
# not_present = 60 not in new_list
# print("Is 60 not present?", not_present)
# # deletes an item ata a specific index or entire list
# del list[2] # (i)
# print("After deleting at index 2:", list)
# list.clear() #(deletes entire list)
# print("Cleared:", list)


my_list = [1,2,3,4,9,5,6]
my_list.append(7)
my_list.extend([8,9,10])
my_list.insert(4,9)
my_list.remove(9)
my_list.pop(3)
test = my_list[3]
test2 = my_list.count(9)
my_list.reverse()
my_list.sort()
new_list = my_list.copy()
length = len(new_list)
min = min(my_list)
max = max(my_list)
concat = new_list + my_list
checking = 6 not in my_list
slicing1= my_list[:]
slicing2 = my_list[::3]
print(slicing1)
print(slicing2)
my_list.clear()
print(my_list)
# del my_list[6]
# print(length)
# print(my_list)
# print(min,max)
# print(concat)
# print(checking)

# print(test)
# print(test2)

# name = "kenty"
# reverse = name[::-1]
# print(reverse)
