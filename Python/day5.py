#create two tuples
tuple1 = (1,2,3,4,5)
tuple2 = (4,5,6,7,8)
# count
count = tuple1.count(2)
print(count)
#index
index = tuple1.index(5)
print(index)
#length
length = len(tuple1)
print(length)
# +operator
new_tuple = tuple1 + tuple2
print(new_tuple)
# * operator
repeated_tuple = tuple1 * 4
print(repeated_tuple)
#slicing
subset = tuple1[0:3]
print(subset)
# in operator
print(3 in tuple1)
#not in operator
print(6 not in tuple1)
