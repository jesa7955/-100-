import sys

if len(sys.argv) == 2:
    with open("hightemp.txt") as hightemp:
        print("".join(hightemp.readlines()[-int(sys.argv[1]):]), end="")
