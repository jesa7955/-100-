import re

with open('20.txt') as source:
    for line in source:
        file_line = re.search("(File|ファイル):(.+)\|", line)
        if file_line != None:
            print(file_line.group(2))
