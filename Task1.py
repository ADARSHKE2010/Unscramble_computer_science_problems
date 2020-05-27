"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
l1=[]

for i in texts:
    l1.append(i[0])
    l1.append(i[1])
    
for j in calls:
    l1.append(j[0])
    l1.append(j[1])

total_numbers=len(set(l1))

print("There are {} different telephone numbers in the records.".format(total_numbers))