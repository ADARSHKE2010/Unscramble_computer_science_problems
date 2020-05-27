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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
first_record = texts[0]
last_record = calls[-1]

text_receive_num = first_record[0]
text_answer_num = first_record[1]
time_of_text = first_record[2]

print("First record of texts, {} texts {} at time {}".format(text_receive_num,text_answer_num,time_of_text))


call_receive_num = last_record[0]
call_answering_num = last_record[1]
time_of_call = last_record[2]
length_of_call = last_record[3]

print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(call_receive_num,call_answering_num,time_of_call,length_of_call))


