"""https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python"""

def duplicate_encode(word):
    nstr = ''
    d = {}
    word = word.lower()
    for i in word:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    for i in word:
        if d[i] == 1:
            nstr += '('
        else:
            nstr += ')'
    return nstr


print(duplicate_encode("recede"))
print(duplicate_encode("Success"))