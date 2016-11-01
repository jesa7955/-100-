with open('hightemp.txt') as hightemp:
    lines = hightemp.readlines()
    lines = [line.replace('\t', ' ').split()  for line in lines]
    lines.sort(key=lambda x: x[2], reverse=True)
    for line in lines:
        print(' '.join(line))
