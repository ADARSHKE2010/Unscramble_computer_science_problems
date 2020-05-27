"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
call_duration = {}
for i in calls:
    call_duration[i[0]] = 0
    call_duration[i[1]] = 0

for call_rec in call_duration:
    for j in calls:
        if call_rec == j[0]:
            tmp = call_duration[call_rec]
            call_duration[call_rec] = int(tmp) + int(j[3])
        if call_rec == j[1]:
            tmp = call_duration[call_rec]
            call_duration[call_rec] = int(tmp) + int(j[3])


maximum = max(call_duration, key=call_duration.get)
print (maximum,"spent the longest time, ",call_duration[maximum]," seconds, on the phone during September 2016")
