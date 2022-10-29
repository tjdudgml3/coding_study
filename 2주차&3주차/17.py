n = list(map(int,input().split(" ")))

def sol(n):
    n,m,k = n
    n += 1
    m += 1
    temp_k = k
    ans = 0
    ans += (n-k+1)*m + (m-k+1)*n
         
    while(n-k+1 > 0 ):
        ans += (n-temp_k+1) * (m-k+1)
        k += k
        
    k = temp_k 
    
    while(m-k+1 > 0 ):
        ans += (n-temp_k+1) * (m-k+1)
        k += k
        
    return ans

print(sol(n))