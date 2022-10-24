#################모르겟다ㅏㅏㅏㅏㅏㅏㅏㅏㅏ#############################

n = int(input())
case_list = []
for case in range(n):
    case_list.append(list(map(int,input().split(" "))))

print(case_list)
def get_biggest_primary(k):
    div_list = []
    a= 2
    ori_k = k
    k_square = k**(1/2)
    while(a<= k_square and k != 1):
        if a == k_square:
            div_list.append(a)
        if k%a == 0:
            
            # div_list.append(int(k/a))
            cnt_a = 0
            while(k%a == 0):
                k = k/a
                cnt_a  += 1
            div_list.append((a,cnt_a))
            k_square = k**(1/2)
            
    
    div_list.sort()
    if not div_list:
        div_list.append(ori_k)
    print(f"def biggest -------div_list = {div_list}")
    return div_list
    
    
def howmany(n,num):
    temp_k = 1
    cnt = 0
    ans_list = []
    for k in num:
        
        while(True):
            if n >= temp_k:
                temp_k *= k
                cnt += 1
            else:
                break
        ans = 0
     
        for num1 in range(1,cnt+1):
            ans += n//(k**num1)
            print(f" def howmany -------num = {num1}, n//k^num = {n//(k**num1)}")
        ans_list.append((k,ans))
    print(ans_list)
    
    return ans

def sol(case):
    print(f"def sol --------- case0 = {case[0]}, case1 = {case[1]}")
    num = get_biggest_primary(case[1])
    return howmany(case[0],num)

for case in case_list:
    print(sol(case))
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")