import re

with open('20.txt') as source:
    for line in source:
        section_line = re.search("^(=+)\s*(.*?)\s*(=+)$", line)
        if section_line is not None:
            print(section_line.group(2), len(section_line.group(1)) - 1)
