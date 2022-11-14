# n = [[60, 75, 48, 56],
#      [52, 68, 93, 73],
#      [80, 88, 48, 49],
#      [40, 63, 54, 75]]
# n = [[1,2,3],[1,2,3],[1,2,3],[1,2,3]]
# n = [[2,5],[9,4],[10,20],[4,2]]

def binary_search(k, n_list):
    low = 0
    high = len(n_list) -1
    mid = (high+low)//2
    # print(n_list[low],n_list[high], n_list[mid])
    while low < high:
        if n_list[mid] == k:
            return n_list[mid], mid
        elif n_list[mid] < k:
            low = mid
        else:
            high = mid
        mid = (high + low)//2
        if low == mid:
            return n_list[high], high
    return n_list[mid], mid


# print(binary_search(15,[2,3,4,5,7,8,14,16,17,22,24]))


def sol(n_list, k):
    v1 = []
    v2 = []
    for element0 in n_list[0]:
        for element1 in n_list[1]:
            v1.append(element0 + element1)
    for element2 in n_list[2]:
        for element3 in n_list[3]:
            v2.append(element2 + element3)
    v1.sort()
    v2.sort()
    idx1 = 0
    idx2 = 0
    best = 40000000
    v1_len = len(v1)
    v2_len = len(v2)
    best_point = 0
    for element1 in v1:
        temp = k - element1
        num, idx = binary_search(temp, v2)
        # print(f"v1element = {element1}, num = {num}, idx = {idx}, v2[idx] = {v2[idx]} , abs = {element1 + v2[idx]}")
        if best == abs(k - (element1 + v2[idx])):
            if element1 + v2[idx] < best_point:
                best_point = element1 + v2[idx]
        elif best > abs(k - (element1 + v2[idx])):
            best = abs(k - (element1 + v2[idx]))
            best_point = element1 + v2[idx]

        if idx != 0:
            if best == abs(k - (element1 + v2[idx - 1])):
                if element1 + v2[idx - 1] < best_point:
                    best_point = element1 + v2[idx - 1]
            elif best > abs(k - (element1 + v2[idx - 1])):
                best = abs(k - (element1 + v2[idx - 1]))
                best_point = element1 + v2[idx - 1]

    return best_point


num = int(input())
items = []
for b in range(num):
    n = []
    k = list(map(int, input().split(" ")))[0]
    for a in range(4):
        n.append(list(map(int, input().split(" "))))
    items.append((k, n))

for item_k, item_n in items:
    print(sol(item_n, item_k))
