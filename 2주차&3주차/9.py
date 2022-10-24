from sympy import N

num = int(input())
n = list(map(int,input().split(' ')))
# n = [4,5,6,7,8]

def get_div(n):
    # n_sqr = n**(1/2)
    a = 2
    ori_n = n
    div_list = []
    while(a <= n):
        if n%a == 0:
            cnt = 0
            while(n%a == 0):
                n = n/a
                cnt += 1
            div_list.append((a,cnt))
        a += 1
    if not div_list:
        div_list.append((1,1))
        div_list.append((ori_n,1))
    return div_list

def sol(n):
    total = 1
    papers = len(n)
    for a in n:
        total *= a
        
    div_list = get_div(total)
    # print(div_list)
    best = div_list[0][0]
    ans_list = []
    ans_type = []
    for a in div_list:
        temp = a[1]//papers
        ans_list.append((a[0],temp))
        ans_type.append(a[0])
    # print(ans_list)
    ele_list = []
    ans = 0
    for a in n:
        ele_list.append(get_div(a))
    
    for i,a in enumerate(ele_list):
        ele_type = []
        for aa in a:
            ele_type.append(aa[0])
        for ans_t in ans_type:
            if ans_t not in ele_type:
                ele_list[i].append((ans_t,0))
            
    # print(f"ele_list = {ele_list}, ans_list = {ans_list}")    
    for ele_ele_list in ele_list:
        
        for b in ans_list:
            for a in ele_ele_list:
                
                if a[0] == b[0]:
                    if b[1] >= a[1]:
                        ans = ans +(b[1] - a[1])
                    
                    else:
                        pass    
            
        # check += 1      
                 

    ans_num = 1
    for a in ans_list:
        ans_num *= a[0]**a[1]
    # print(ans_num,ans)   
    return ans_num,ans 
a = sol(n)
print(a[0],a[1])

    
    