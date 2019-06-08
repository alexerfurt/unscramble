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

# Creating a dict to save every unique number together with its time spend in a call
aggregate_calls_per_number = {}
# Going through each line and either adding a number or just its corresponding call time as an integer
for i in range(len(calls)):
    # Looking into the sender/caller number
    if calls[i][0] in aggregate_calls_per_number:
        aggregate_calls_per_number[calls[i][0]] += int(calls[i][3])
    else:
        aggregate_calls_per_number[calls[i][0]] = int(calls[i][3])

    # Looking into the receiver numbers as their time spend on the phone counts as well
    if calls[i][1] in aggregate_calls_per_number:
        aggregate_calls_per_number[calls[i][1]] += int(calls[i][3])
    else:
        aggregate_calls_per_number[calls[i][1]] = int(calls[i][3])

# Creating variable to hold the longest time spent on the phone and its corresponding telephone number
longest_time = 0
longest_number = None
# Iterating through the dict created in the step before
for key in aggregate_calls_per_number.keys():
    if aggregate_calls_per_number[key] > longest_time:
        longest_time = aggregate_calls_per_number[key]
        longest_number = key

print(f"{longest_number} spent the longest time, {longest_time} seconds, on the phone during September 2016.")

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""
