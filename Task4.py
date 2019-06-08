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

# Create list of all (unique) nubmers that receive calls and text as well receive texts
# Put all numbers into one list
numbers = []
for i in range(len(texts)):
    numbers.append(texts[i][0])
    numbers.append(texts[i][1])
for i in range(len(calls)):
    numbers.append(calls[i][1])

# Create a set of the numbers list with only unique numbers
unique_numbers = set(numbers)

# Check each calling number against the list above
poss_telemarktrs = []
for item in calls:
    if item[0] not in unique_numbers:
        poss_telemarktrs.append(item[0])

# Dedupe the list, sort and print
poss_telemarktrs_unique = sorted(set(poss_telemarktrs))
print("These numbers could be telemarketers: ", *poss_telemarktrs_unique, sep="\n")
