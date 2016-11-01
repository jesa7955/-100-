import re

with open('20.txt') as source:
    for line in source:
        if 'Category' in line:
            print(line.strip())
