with open('13.txt', 'w') as res, open('col1.txt') as col1, open('col2.txt') as col2:
    res.write("".join(s1.strip() + '\t' + s2 for s1, s2 in zip(col1, col2)))
