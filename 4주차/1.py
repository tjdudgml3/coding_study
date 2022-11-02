# n = [1,3,5,23,4,3,2,1,7,8,11]
num = int(input())
n = list(map(int,input().split(' ')))
k = int(input())
#투포인터를 이용해서 풀이
def sol(n,k):
    n.sort() #정렬
    low = 0
    high = len(n) - 1
    cnt = 0
    
    while(low < high): 
        if n[low] + n[high] == k:
            low += 1
            high -= 1
            cnt += 1
        elif n[low] + n[high] > k:
            high -= 1
        elif n[low] + n[high] < k:
            low += 1
        else:
            pass
        
    return cnt 

print(sol(n,k))