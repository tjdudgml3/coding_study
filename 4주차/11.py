# import time

num, k = list(map(int,input().split(' ')))
n = list(map(int,input().split(' ')))

# n = []
# for i in range(100000):
#     n.append(10000)

# start = time.time()
def sol(n,k):
    low = 0
    high = 0
    shortest = 1000000000
    n.append(0)
    dist = 0
    sum_partial = 0
    while(n[low] > 0 and high < len(n) ):
        # print(high,low)
        # temp = n[high]
        if sum_partial >= k:
            if shortest > dist:
                shortest = dist
            sum_partial -= n[low]
            low += 1
            dist -= 1
            
        elif sum_partial < k and n[high] >0:
            sum_partial += n[high]
            high += 1
            dist += 1
            
        else:
            break
            
       
        # print(f"low = {low}, high = {high}, nlow = {n[low]}, nhigh = {n[high]} shortest = {shortest}")
    if shortest == 1000000000:
        return 0
    else:
        return shortest

print(sol(n,k))
# print(time.time() -start)        
            