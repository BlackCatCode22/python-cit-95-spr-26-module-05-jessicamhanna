import re

hand = open('mbox-short.txt')
numlist = list()

for line in hand:
    line = line.rstrip()

    # Extract the floating-point number using findall and parentheses
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)

    # Skip lines that do not match our regular expression
    if len(stuff) != 1:
        continue

    # Convert the extracted string to a float and append to list
    num = float(stuff[0])
    numlist.append(num)

print('Maximum:', max(numlist))