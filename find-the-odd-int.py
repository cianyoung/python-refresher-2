def find_it(seq):
    l_dict = {}
    for num in seq:
        if num in l_dict:
            l_dict[num] += 1
        else:
            l_dict[num] = 1
    print(l_dict)
    for k, v in l_dict.items():
        if v % 2 != 0:
            print('k: ', k)

find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])