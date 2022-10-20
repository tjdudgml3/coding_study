
def get_sum(a,added,first,last):
    first1 = a + (first-1)*added
    last2 = a + (last - 1)*added
    sum_first = int(first*(2*a + (first-1)*added)/2)
    sum_last = int(last*(2*a + (last-1)*added)/2)
    sum1 = sum_last - sum_first +first1
    return sum1

def get_div(a,added,first,last):
    first1 = a + (first-1)*added
    last2 = a + (last - 1)*added
    if first1 == last2:
        return first1 
    while(a >= 0):
        if a ==0 or a== added:
            return added
        elif added == 0:
            return a
        elif a > added:
            temp = a%added
            a = temp
        else:
            temp = added%a
            added = temp
        
        

a,d = map(int,input().split(' '))      
n = int(input())
query_list = []
for cnt in range(n):
    query_list.append(list(map(int,input().split(' '))))

for query in query_list:
    if query[0] == 1:
        print(get_sum(a,d,query[1],query[2]))
    else:
        print(get_div(a,d,query[1],query[2]))