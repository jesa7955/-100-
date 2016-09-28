special_indexs = [1, 5, 6, 7, 8, 9, 15, 16, 19]
input_str = input()
jisho = {}
format_str = ''
for c in input_str:
    if c.isalnum() or c.isspace():
        format_str += c
for index, word in enumerate(format_str.split()):
    if (index + 1) in special_indexs:
        jisho[word[0]] = index + 1
    else:
        jisho[word[0:2]] = index + 1
print(jisho)
