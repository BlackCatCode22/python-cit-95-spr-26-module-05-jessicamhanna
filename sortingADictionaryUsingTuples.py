# Sorting the Dictionary using Tuples

fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

# create a new list to store flipped tuples
lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

# sort the list in descending order by value
lst = sorted(lst, reverse=True)

# print the top 10 common wolds
for val, key in lst[:10]:
    print(key, val)

