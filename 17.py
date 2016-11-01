with open('hightemp.txt') as hightemp:
    s = set(line.split()[0] for line in hightemp)
    for line in s:
        print(line)
