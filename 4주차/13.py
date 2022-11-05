n = [[10,5],[11,5], [13,5], [10,15], [11,16], [13,17] ]

n.sort()

def get_nearest(n):
    pass

def sol(n):
    n_x = []
    n_y = []
    for a,b in n:
        n_x.append(a)
        n_y.append(b)
    N = len(n)
    x_stoppoint = n_x[-1]
    y_stop_point = max(n_y)
    target = N//2
    x_low = 0
    y_low = 0
    x_high = 0
    y_high = 0
    dist = 0
    while(x_low < x_stoppoint):
        break