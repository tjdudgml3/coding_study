n, m = list(map(int,input().split(' ')))

'''어떤 숫자의 팩토리얼에 2가 나눠질수있는 갯수를 구하는 함수'''
def get_two(n):
    mul = 0
    cnt = 0
    if n < 2:
        return 0
    else:
        mul = 1
    while(n >= 2**mul):
        cnt += int(n//(2**mul))
        mul += 1
    
    return cnt

'''어떤 숫자의 팩토리얼에 5가 나눠질수있는 갯수를 구하는 함수'''
def get_five(n):
    mul = 0
    cnt = 0
    if n < 5:
        return 0
    else:
        mul = 1
    while(n >= 5**mul):
        cnt += int(n//(5**mul))
        mul += 1
    
    return cnt

def sol(n, m):
    temp_n_two = get_two(n) - get_two(m) - get_two(n-m)
    temp_n_five = get_five(n) - get_five(m) - get_five(n-m)
    return min(temp_n_five, temp_n_two)

print(sol(n, m))