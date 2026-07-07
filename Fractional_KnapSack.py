def Fractional_knapsack(w, c, p):
    n = len(w)
    items = [(w[i],c[i],p[i]) for i in range(n)]
    items.sort(key = lambda x: x[2]//x[1], reverse = True)
    C = 50
    total = 0
    for w, c, p in items:
        if c <= C:
            total += p
            C -= w
        else:
            total += p * C // w
            break
    return total

w = [24, 10, 28, 18, 12, 16]
c = [18, 25, 22, 28, 30, 16]
p = [60, 40, 70, 50, 35, 50]

print(Fractional_knapsack(w, c, p))    
    