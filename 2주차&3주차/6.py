import time

n = int(input())
start = time.time()
def sol(n):
    answer = 0
    len_num = n//2 + 1
    for number in range(2,len_num):
        answer += (n//number-1) * number
        
    return answer%1000000 
print(sol(n))
print(time.time() - start)