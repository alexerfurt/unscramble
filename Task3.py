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

# Part A: All area codes and mobile prefixes - called from (080)
# Create empty list to append identified codes
list_of_codes = []
# Iterate through calls list and look for sender numbers starting with 080
for item in calls:
    if item[0][1:4] == "080":
        # Check whether receiver phone number is fixed line, mobile or Telemarketers
        if item[1][0] == "(":
            for i in range(len(item[1])):
                if item[1][i] == ")":
                    code = item[1][1:i]
                    list_of_codes.append(code)
                    break
            """
            # Excluding this since Telemarketers actually never get called...
            elif item[1][:3] == "140":
            code = item[1][:3]
            list_of_codes.append(code)
            """
        else:
            code = item[1][:4]
            list_of_codes.append(code)

#  Take newly filled unordered list with duplicates, order, dedupe and print it in rows
unique_sorted_codes = sorted(set(list_of_codes))
print("The numbers called by people in Bangalore have codes:", *unique_sorted_codes, sep="\n")

# Part B: Of all calls made from (080), what % went to (080)?
# Create two variable to count total calls outgoing from 080 as well as the ones that are going to 080
count_total = 0
count_bangalore = 0
# Iterate through all calls
for item in calls:
    # Pick calls that are outgoing from a (080) number
    if item[0][:5] == "(080)":
        count_total += 1
        # Pick calls that are received from a (080) number
        if item[1][:5] == "(080)":
            count_bangalore += 1
        else:
            continue
# Calculate percentage of Bangalore to Bangalore calls from all outgoing Bangalore calls, print percentage
percentage = count_bangalore/count_total * 100
print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percentage))


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
