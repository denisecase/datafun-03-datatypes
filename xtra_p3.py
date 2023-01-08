"""
Optional bonus. See course site for details.

>>> len(longwordset1)
415

>>> len(longwordset2)
197

>>> len(longwords)
13
"""

import doctest

# read from second file and get a list of words

with open("text_hamlet.txt", "r") as f1:
    text = f1.read()
    wordlist1 = text.split()  # split on whitespace

# read from second file and get a list of words

with open("text_juliuscaesar.txt", "r") as f2:
    text = f2.read()
    wordlist2 = text.split()  # split on whitespace

# Done with files - let the files close and the work begin

# Remove duplicates by creating two sorted sets
# hint: use sorted() to sort the list
# hint: use set() to remove duplicates
# name them wordset1 and wordset2
wordset1 = set()  # TODO fix this line
wordset2 = set()  # TODO fix this line


# initialize a variable maxlen = 10
maxlen = 1  # TODO fix this line

# use a list comprension to get a list of words longer than 10
# for word in wordset1
# That is:
# in a list (e.g. square brackets)
# say "[Give me word (for each word in wordset1)
#      if len(word) is greater than maxlen]"
# then convert the list to a set to we can take the intersection
# hint: use set()
# name them longwordset1 and longwordset2

longwordset1 = set()  # TODO: fix this line
longwordset2 = set()  # TODO: fix this line

# find the intersection of the two sets
# that is, the words in both longwordset1 1 & longwordset2
# name this variable longwords
longwords = longwordset1 & longwordset2

# print the length of the sets and the list
print(len(longwordset1))
print(len(longwordset2))
print(len(longwords))
print()
print(f"{sorted(longwords) = }")
print()

# check your work
print("TESTING...if nothing prints before the testing is done, you passed!")
doctest.testmod()
print("TESTING DONE")
