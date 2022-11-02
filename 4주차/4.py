n = 53

def get_primary():
    primary_list = [2]
    
    for a in range(1900000,2000001):
        check = 0
        if a % 2 == 0:
            continue
        
        for b in range(3,int(a**(1/2)+1),2):
            if a % b == 0:
                check = 1
                break
        if check == 0:
            primary_list.append(a)
        
    return primary_list

print(get_primary())