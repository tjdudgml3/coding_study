test_case_num = int(input())
test_list = []
for test_case in range(test_case_num):
    input()
    test_list.append(list(map(int,input().split(' '))))
    


def sol(nn):
    sum_n = sum(nn)
    primary_list = []
    i= 1
    answer = 0
    while(i <= sum_n**(1/2)):
        if sum_n%i == 0:
            primary_list.append(i)
            primary_list.append(int(sum_n/i))
            
        i += 1
    #primary_list.append(i)
    primary_list.sort()
    #print(f"primay_list = {primary_list},")
    for primary_num in primary_list:
        answer = 0
        n=nn.copy()
        #print(f"listn_first = {n}, primary = {primary_num}")
        if max(n) > primary_num:
            continue
        else:
            for idx in range(len(n)):
                if  n[idx] == primary_num:
                    if idx == len(n)-1:
                        return answer
                    continue
                    
                elif n[idx] > primary_num:
                    if idx == len(n)-1:
                        return answer
                    break
                else:
                    n[idx+1] = n[idx] + n[idx+1]
                    if n[idx+1] > primary_num:
                        break
                    #print(f"listn_last = {n}")
                    answer += 1
                    if idx == len(n)-2:
                        return answer
         
            
            
for case in test_list:
    ans = sol(case)
    if ans:
        print(ans)
    else:
        print(0)
    