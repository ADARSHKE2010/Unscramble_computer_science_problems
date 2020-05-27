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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
telemarketers_call =[]
received_call =[]
    
for call in calls:
    outgoing_calls, incoming_calls = call[0], call[1] 
    telemarketers_call.append(outgoing_calls)
    received_call.append(incoming_calls)

for text in texts:
    outgoing_text, incoming_text = text[0], text[1] 
    received_call.append(outgoing_text)
    received_call.append(incoming_text)

diff = list(set(telemarketers_call) - set(received_call))  
diff.sort()
print("These numbers could be telemarketers: \n")
for i in diff:
    print(i)

