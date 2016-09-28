import random

def shuffle(char_list):
    length = len(char_list)
    num_set = set(list(range(length)))
    res_list = []
    for char in char_list:
        res_list.append(char_list[get_index(num_set, length)])
    return res_list

def get_index(num_set, length):
    while True:
        num = random.randrange(0, length)
        if num in num_set:
            num_set.remove(num)
            break
    return num

word_list = input().split()
res_list = []
for word in word_list:
    if len(word) >= 4:
        char_list = list(word)
        mid_list = char_list[1:-1]
        mid_list = shuffle(mid_list)
        #random.shuffle(mid_list)
        word = word[0] + "".join(mid_list) + word[-1]
    res_list.append(word)
print(" ".join(res_list))
