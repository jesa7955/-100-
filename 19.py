res = {}
with open('hightemp.txt') as hightemp:
    for line in hightemp:
        key = line.split()[0]
        if key in res:
            res[key] += 1
        else:
            res[key] = 1
    for item in sorted(res.items(), key=lambda x: -x[1]):
        print("{} {}".format(item[1], item[0]))
