import re
import operator
import csv
from collections import Counter



with open('Abstracts2.txt') as f:
    passage = f.read()

words = re.findall(r'\w+', passage)

cap_words = [word.upper() for word in words]

print(dict(Counter(cap_words).most_common(10)))

