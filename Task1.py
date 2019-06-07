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

# Put all numbers into one list
numbers = []
for i in range(len(texts)):
    numbers.append(texts[i][0])
    numbers.append(texts[i][1])

for j in range(len(calls)):
    numbers.append(calls[j][0])
    numbers.append(calls[j][1])

# Create a set of the numbers list with only unique numbers
unique_count = set(numbers)
print(f"There are {len(unique_count)} different telephone numbers in the records.")

"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
