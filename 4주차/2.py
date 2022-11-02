#구간의합

num, k = list(map(int,input().split(' ')))
n = list(map(int,input().split(' ')))

#투포인터 
def sol(n,k):
    n.append(0)
    low = 0
    high = 0
    cnt = 0
    
    while(low < len(n)-1):
        sum_of_list = sum(n[low:high])
        # print(f"low = {low}, hig/h = {high}, nsliced = {n[low:high]}, sum = {sum_of_list}")
        
        if sum_of_list == k:
            cnt += 1
            if high == len(n)-1:
                break
            low += 1
            high += 1
        elif sum_of_list > k :
            low += 1
        elif sum_of_list < k :
            if high == len(n)-1:
                break
            high += 1
        else:
            pass
        
    return cnt

print(sol(n,k))