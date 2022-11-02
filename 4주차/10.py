num,k = list(map(int,input().split(' ')))
n = list(map(int,input().split(' ')))

def sol(n,k):
    low = 0
    high = 0
    n.append(0)
    best = 0
    dist = 0
    temp = 0
    best_dist = 0
    # if n[0]%2 == 0:
    #     dist = 0
    # else:
    #     dist = 1
        
    while(n[high] > 0):
        # print("----------------------------------------------")
        # print(f"n[low] = {n[low]} ,n[high] = {n[high]} ")
        
        if n[high]%2 == 0:
            if n[high] == 0:
                temp -= 1
            high += 1
            temp += 1
        
            # print('block1')
        else:
            if dist < k:
                high += 1
                dist += 1
                temp += 1
                if n[high] == 0:
                    temp -= 1
                # print('block2')
            else:
                if n[low]%2 == 0:
                    low += 1
                    temp -= 1
                else:
                    low += 1
                    dist -= 1
                    temp -= 1
                # print('block3')
        if best < temp:
            best = temp
            best_dist = dist
        # print(f"n[low] = {n[low]} ,n[high] = {n[high]} ")
        # print(f"low = {low}, high = {high}, dist = {dist},  temp = {temp}, best = {best}")
        # print('-------------------------------------------------------')
    return best - best_dist
                 
print(sol(n,k))