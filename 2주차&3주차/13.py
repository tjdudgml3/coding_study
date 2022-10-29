n, A =  list(map(int,input().split(" ")))

def sol(n,A):
    mul = 0
    
    if A > n:
        return 0
    else:
        mul = 1
        
    cnt = 0
    
    while(n >= A**mul):
           cnt += n//(A**mul)
           mul += 1
           
    return cnt

print(sol(n,A)) 