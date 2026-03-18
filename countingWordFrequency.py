# Read a file, count all the words using dictionary,
# loop key-value pairs to find most common word

name = input('Enter file:')
handle = open(name)

# Make an empty dictionary to store word counts
counts = dict()

# Iterate through the lines in the files
for line in handle:
    words = line.split() # Split each line into words
    # Iterate through each word to build the histogram for word in words:
    for word in words:
        counts[word] = counts.get(word, 0) + 1

# Find the most common word
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount= count
print(bigword, bigcount)