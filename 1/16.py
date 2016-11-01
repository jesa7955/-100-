import sys, math

if len(sys.argv) == 2:
    with open("hightemp.txt") as hightemp:
        lines = hightemp.readlines()
    unit = math.ceil(len(lines) / int(sys.argv[1]))
    for i in range(int(sys.argv[1])):
        with open("file{}.txt".format(i+1), "w") as output:
            output.write("".join(lines[i*unit:(i+1)*unit]))
