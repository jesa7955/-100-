import re

with open('20.txt') as source:
    lines = re.split(r"\n[\|}]", source.read())
    print(lines[0])
