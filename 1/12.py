with open('hightemp.txt') as hightemp, open('col1.txt', 'w') as col1, open('col2.txt', 'w') as col2:
    for line in hightemp:
        real = line.strip().strip()
        real = real.split()
        col1.write(real[0] + '\n')
        col2.write(real[1] + '\n')
