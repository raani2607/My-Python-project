# for loop
# name = "kenty"
# for i in(name):
#     print(i)

# for i in range(1,12):
#     if i == 8:
#         continue
#     else:
#         print(i)

# nested loop
row = int(input("Enter the number of rows : "))
col = int(input("Enter the number of columns : "))
for i in range(1,row+1): 
    for j in range(1,col+1):
        print(f"{i * j :5} ",end='')
    print()