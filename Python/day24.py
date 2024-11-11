#regular expression -> sequemce of character that define a search pattern 


import re

checking = re.match(r"kenty", "senty hussein is my name")
if  checking:
    print("match found")
else:
    print("match not found")

searching = re.search(r'food','i like food so much')
if searching:
    print('match found')
else:
    print('match not found')

finding = re.findall(r'/d+','I have 25 potatoes to fry!!')
if finding:
    print(finding)
else:
    print('match not found')

replacing = re.sub(r'kenty','raani','Instructor is better than me')
print(replacing)

