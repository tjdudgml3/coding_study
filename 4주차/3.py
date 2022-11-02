# n = [20,7,23,19,10,15,25,8,13]
n = []
for a in range(9):
    n.append(int(input()))
    
#1주차때와 문제가 중복되지만, 1주차째는 dfs로 풀었음. 그러나 이중포인터가
#더 직관적이고 빠르다.
def sol(n):
    n.sort()
    low = 0
    high = len(n) - 1
    n.append(0)
    ans = []
    k = sum(n) - 100
    
    while(low < high):
        sum_of_n = n[low] + n[high] 
        if sum_of_n == k:
            return n[low],n[high],0
        elif sum_of_n > k:
            high -= 1
        elif sum_of_n < k:
            low += 1 
        else:
            pass
        
ans = sol(n)
for answer in n:
    if answer not in ans:
        print(answer)