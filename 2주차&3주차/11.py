n = int(input())
n_list = []
for j in range(n):
    n_list.append(list(map(int,input().split(" "))))

# print(n_list)
def get_div(a,b):
    while(True):
        if a == 0:
            return b
        elif b ==0 :
            return a
        elif a >= b:
            a = a%b
        else:
            b = b%a
            
def sol( n ):
    dic = {}
    for i,a in enumerate(n):
        for j,b in enumerate(n):
            if i == j:
                continue
            gcd = get_div( a, b)
            if gcd not in dic:
                dic[gcd] = 1
            else:
                pass
    # print(dic)cd 
    return max(dic)
for a in n_list:
    print(sol(a))