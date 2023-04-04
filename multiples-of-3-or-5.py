def solution(number):
    sum = 0
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            sum = sum + i
            print('sum', sum)
  
print(solution(10))