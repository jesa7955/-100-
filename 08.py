def cipher(source):
    code = ""
    for char in source:
        if char.islower():
            code += chr(219 - ord(char))
        else:
            code += char
    return code

print(cipher(input()))
