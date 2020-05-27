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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
no_of_call_banglore = 0
total_calls_banglore = 0
total_no_of_calls = 0
codes =[]
for i in calls:
    if i[0].find("(080)") != -1 and i[1].find("(080)") != -1:
        codes.append(i[1])
        no_of_call_banglore += 1
        total_calls_banglore += 1
        total_no_of_calls += 1
    
    elif i[0].find("(080)") != -1 and i[1].find("(") != -1:
        codes.append(i[1])
        total_calls_banglore += 1
        total_no_of_calls += 1
            
    elif i[0].find("(080)") != -1 and ( i[1][0] == "9" or i[1][0] == "8" or i[1][0] == "7" ):
        codes.append(i[1])
        total_calls_banglore += 1
        total_no_of_calls += 1
    
    else:
        total_no_of_calls += 1

        
#PART-A:

print("The numbers called by people in Bangalore have codes:")
std_codes = []
for j in sorted(set(codes)):
    if(j.find(")") != -1):
        pos = j.find(")")
        std_codes.append(j[:pos+1])
    else:
        std_codes.append(j[:4])

for std_code in sorted(set(std_codes)):
    print(std_code)

#PART-B:
percent=(no_of_call_banglore/total_calls_banglore)*100
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(round(percent, 2)))
