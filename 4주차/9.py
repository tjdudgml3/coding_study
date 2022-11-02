#현재모무게 제곱 - 예전몸무게 제곱은 = g

from re import L


n = int(input())

def sol(n):
    low =1
    high = 1
    ans = []
    while(low < n):
        minus = int(high**2 - low**2)
        if minus == n:
            ans.append(high)
            low += 1
            high += 1
        elif minus > n:
            low += 1
        else:
            high += 1
            
    return ans

ans = sol(n)
if not ans:
    print(-1)
else:
    [print(i) for i in ans]
            