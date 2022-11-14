#시간초과가 난다. for문 두개의 부분에서 실행시간을 더 줄일수 있을것같지만, 생각이 잘안난다.
num = input()
# n = list(map(int,input().split(' ')))
n = []
for a in range(300):
    n.append(1)
n.sort()
import time
start = time.time()
def get_list(n,k1,k2):
    return n[k1+1:k2]

def sol(n):
    best = n[-1]
    low1 = 0
    high1 = 0
    low2 = 0
    high2 = 0
    N = len(n)
    
    for a in range(N):
        for b in range(a+1,N):
            temp_list = get_list(n,a,b)
            # temp_list = n
            # print(f"제외된 a,b = {a,b}, temp_list = {temp_list}")
            target = n[a] + n[b]
            temp_len = len(temp_list)
            low = 0
            high = temp_len - 1
            temp_ans = n[-1]
            while(low < high and low < temp_len):
                temp_sum = temp_list[low] + temp_list[high]
                # print(f"low = {low}, high = {high}, temp_ans = {temp_ans}, temp_sum = {temp_sum}")
                
                
                if temp_sum > target:
                    high -= 1
                    temp_ans = temp_sum - target
                else:
                    low += 1
                    temp_ans = target - temp_sum
                    
                if temp_ans < best:
                    best = temp_ans
                    if best == 0:
                        # return 0
                        pass
                    # print(f"----------베스트 갱신 low = {low, temp_list[low]} high = {high,temp_list[high]}")
    return best


print(sol(n))
print(time.time() - start)