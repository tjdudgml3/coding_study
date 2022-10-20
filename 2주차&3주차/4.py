# import time
n = int(input())

def flip(n):
    n = str(n)
    new_num = ''
    for ele in n:
        if ele == '0' or ele == '2' or ele == '5' or ele == '8'  or ele == '1' :
            new_num += ele
        elif ele == '6':
            new_num += '9'
        elif ele == '9':
            new_num += '6'
        else:
            return 0
    fliped = int(new_num[::-1])
    # print(fliped)
    return fliped

def isprimary(n):
    # start = time.time()
    # primary_list = []
    if n == 0 or n== 1:
        return False
    if n == 2:
        return True
    n_range = int(n**(1/2))+1
    # print(n_range)
    for i in range(3,n_range,2):
        if n%i == 0:
            return False
        
            
    # end = time.time()
    # print( end - start)
        # else:
        #     continue
        
        
    return True
            
def sol(n):
    if isprimary(flip(n)) and isprimary(n): 
        return 'yes'
    else:
        return 'no'
    
# start = time.time()
print(sol(n))
# end = time.time()
# print( end - start)