def duplicate_encode(word):
    d = {}
    for i in word:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for k, v in d.items():
        if v > 1:
            print(k)




print(duplicate_encode("recede"))