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

# Getting the index of the last row of the calls list
last_idx = len(calls)-1

# Printing the messages
print(f"First record of texts, {texts[0][0]} texts {texts[0][1]} at time {texts[0][2]}")
print(f"Last record of calls, {calls[last_idx][0]} calls {calls[last_idx][1]} at time {calls[last_idx][2]}, lasting {calls[last_idx][3]} seconds")

#print(len(calls))

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
