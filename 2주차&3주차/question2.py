#숫자의 소인수분해하는법. 숫자의 범위가 크기때문에 n**1/2로 범위를 잡는다.
n = int(input())
def sol(n):
    answer_list = []
    i = 2
    lenth = n**(1/2)
    while(i <= lenth):
        if n%i ==  0:
            answer_list.append(i)
            n = n/i
            i= 2
            #print(answer_list)
            lenth = n**(1/2)
        else:
            i += 1
    answer_list.append(int(n))     
    return answer_list

answer_list = sol(n)
answer_list.sort()
print(len(answer_list))
for ele in answer_list:
    print(ele,end = ' ')
      
      