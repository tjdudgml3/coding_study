k = int(input())
n = input()

def sol(n,k):
    dic = {}
    for alphabet in n:
        if alphabet not in dic:
            dic[alphabet] = 0
    cnt = 1
    low = 0
    high = 0
    N = len(n)
    dic[n[0]] = 1
    
    best = 0
    num_alphabets = 1
    while(high < N - 1):
        # print(f"dic = {dic}, low = {n[low]}, high = {n[high]}, cnt = {cnt} num_alph = {num_alphabets}")
        
        if dic[n[high+1]] > 0 :
            high += 1
            dic[n[high]] += 1
            cnt += 1
            # print('block1')
        elif num_alphabets < k:
            high += 1
            num_alphabets += 1
            dic[n[high]] += 1
            cnt += 1
            # print('block2')
        else:
            if dic[n[low]] > 1:
                dic[n[low]] -= 1
                low += 1
                cnt -= 1
                # print('block3')
                
                
            else:
                dic[n[low]] -= 1 
                num_alphabets -= 1
                low += 1
                cnt -= 1
                # print('block4')
        if best < cnt:
            best = cnt
    return best    

print(sol(n,k))