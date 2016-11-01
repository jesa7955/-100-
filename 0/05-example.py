original = "I am an NLPer"

def ngram(input, n):
    last = len(input) - n + 1
    ret = []
    for i in range(0, last):
        ret.append(input[i:i+n])
    return ret
#def ngram(input, n):
#    l = len(input)
#    if type(input) == str:
#        input = "$" * (n - 1) + input + "$" * (n - 1)
#        for i in xrange(l + 1):
#            print input[i:i+n]
#    elif type(input) == list:
#        input = ["$"] * (n - 1) + input + ["$"] * (n - 1)
#        for i in xrange(l + 1):
#            print input[i:i+n]

print(ngram(original, 2))
original = original.split()
print(ngram(original, 2))
