N, k, ns = list(map(int,input().split(' ')))
n = []

for a in range(ns):
    n.append(int(input()))
        
# n = [2,10,1,5,9]
# k = 
# N = 10
def sol(N,n,k):
    n.sort()
    best = 0
    low = 1
    high = k
    dic = {}
            
    for broken_num in n:
        dic[broken_num] = 1
    
    for check in range(k+1):
        if check in dic:
            best += 1
    
    temp = best
    
    while(high < N+1):
        # print(temp)
        if temp < best :
            best = temp
        if low in dic:
            temp -= 1
        low += 1
        high += 1
        if high in dic:
            temp += 1
        
    return best
        
print(sol(N,n,k))       