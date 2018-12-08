n = input()
x = input().split(' ')
w = input().split(' ')
xi = [int(y) for y in x]
wi = [int(y) for y in w]

def weighted_mean(x, w):
    f = 0
    for y in range(0, len(x)):
        f += w[y] * x[y]
    return round(f/sum(w), 1)

print(weighted_mean(xi,wi))

