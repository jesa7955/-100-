input_str = input()
format_str = ''
for c in input_str:
    if c.isalnum() or c.isspace():
        format_str += c
print(list(map(len, format_str.split())))
