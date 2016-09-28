source1 = "paraparaparadise"
source2 = "paragraph"

def ngram(source, n):
    last = len(source) - n
    res = [source[index:index+n] for index in range(last + 1)]
    return res

print(ngram(source1, 2))
print(ngram(source2, 2))
X, Y = set(ngram(source1, 2)), set(ngram(source2, 2))
print(X.union(Y))
print(X.intersection(Y))
print(X.difference(Y))
print("se" in X)
print("se" in Y)
