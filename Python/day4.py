# create two sets
set1 = {1,2,3,4,5,6,7,}
set2 = {6,7,8,9,10}
# add an element to the set
set1.add(9)
print(f"after adding 9 to set1 : {set1}")
# update set1 with elements from set2
set1.update(set2)
print(f"after set1 is updated with elements from set2 : {set1}")
# remove an element from set1
set1.remove(9)# if i remove 11 it will bring Key Error : 11
print(f"after removing 9 from set1 : {set1} ")
# discard an element from set1 (no error found)
set1.discard(10) #if i remove 11 it will not produce any output
print(f"after removing 10 from set1 : {set1} ")
#pop an element from set1
popped_element = set1.pop()
print (popped_element)
#copy
coppied_set = set1.copy()
print(coppied_set)
#union
union_set = set1.union(set2)
print(union_set)
#intersection
intersection_set = set1.intersection(set2)
print(intersection_set)
#difference
difference_set = set1.difference(set2)
print(difference_set)
#symmetric difference
sym_diff_set = set1.symmetric_difference(set2)
print(sym_diff_set)
#Check if set2 is a subset of set1
subset_set = set1.issubset(set2)
print(subset_set)
#Check if set1 is a superset of set2
superset_set = set1.issuperset(set2)
print(subset_set)
# check if set1 and set2 are sdisjoint
common_elements = set1.isdisjoint(set2)
print(common_elements)
#clear
set1.clear()
print(set1)
