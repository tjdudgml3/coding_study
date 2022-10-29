from click import pass_obj


n = int(input())

def sol(n):
    return int(n**(1/2))

print(sol(n))