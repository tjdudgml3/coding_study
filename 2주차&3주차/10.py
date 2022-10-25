n = int(input())
n = list(map(int,input().split(" ")))

def is_primary(n):
    if n == 1:
        return False
    for num in range(2,int(n**(1/2))+1):
        if n%num == 0 :
            return False

    return True

def sol(n):
    ans = 0
    for a in n:
        if is_primary(a):
            ans += 1
        else:
            continue
    return ans

print(sol(n))
                