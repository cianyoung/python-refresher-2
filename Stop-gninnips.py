def spin_words(sentence):
    new_arr = []
    x = sentence.split()
    for i in x:
        if len(i) > 5:
            i = (i[::-1])
            new_arr.append(i)
        else:
            new_arr.append(i)
    return(' '.join(new_arr))