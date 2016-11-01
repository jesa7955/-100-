import re

with open('20.txt') as source:
    for line in source:
        category_line = re.search("^\[\[Category:(.*?)(|\|.*)\]\]$", line)
        if category_line is not None:
            print(category_line.group(1))
