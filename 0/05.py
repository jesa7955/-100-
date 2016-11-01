source = "I am an NLPer"

def ngram(source, n):
    l = len(source)
    if type(source) == str:
        source = "$" * (n - 1) + source + "$" * (n - 1)
        for i in range(l + 1):
            print(source[i:i+n])
    elif type(input) == list:
        source = ["$"] *  (n - 1) + source + ["$"] * (n - 1)
        for i in range(l + i):
            print(source[i:i+n])
ngram(source, 2)
source = source.split()
ngram(source, 2)
    
