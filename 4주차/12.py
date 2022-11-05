nums,b,k,coupon = list(map(int,input().split(' ')))
n = []
# for a in range(nums):
#     n.append(int(input()))

for a in range(3000000):
    n.append(a%3000)

def sol(n,k,coupon):
    dic = {}
    for num in n:
        if num not in dic:
            dic[num] = 0
        else:
            pass
    # print(dic)
    low = 0
    high = k - 1
    for i in n[low:high+1]:
        dic[i] += 1
        
    dic[coupon] = len(n)
    stop_point = len(n)
    best = 0
    cnt = 0
    for i in dic:
        if dic[i] >0:
            cnt += 1
    while(low < stop_point):
        # print(f"low = {low,n[low]}, high = {high, n[high]},cnt = {cnt}, best = {best} dic = {dic}")
        if best < cnt:
            best = cnt
        dic[n[low]] -= 1
        if dic[n[low]] == 0:
            cnt -= 1
        low += 1
        high += 1
        if high == stop_point:
            high = 0
        dic[n[high]] += 1
        if dic[n[high]] == 0:
            cnt += 1
        else:
            pass
        dic[n[high]] += 1
            
    return best

print(sol(n,k,coupon))