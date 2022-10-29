
#두수의 공약수가 0임을 check
def checkZero(a,b):
    
    while(True):
        if a == 0:
            return b == 1
        elif b == 0:
            return a == 1
        elif a >= b:
            a = a%b
        else:
            b = b%a 

#약수를 구하는 함수
def get_div(n):
    div = (1,n)
    lenth = int(n**(1/2))
    for num in range(1,lenth+1):
        if n%num == 0 and checkZero(num, n//num):
            div = (num, n//num)
    return div


def sol(g,l):
    temp = 0
    temp = l//g
    # print(f"temp = {temp}")
    a,b =  get_div(temp)
    
    return a*g, b*g

n1, n2 = list(map(int,input().split(' ')))

a, b  = sol(n1, n2)
# print(checkZero(4,5),checkZero(4,6),checkZero(1,10))
print(a,b)