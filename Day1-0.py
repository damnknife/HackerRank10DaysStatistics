N = int(input())
L = input().split(' ')
L = [int(x) for x in L]

def mean(Data):
    return sum(Data)/len(Data)

def std(Data):
    mn = mean(Data)
    tmp = 0
    for x in Data:
        tmp += (x-mn)**2
    return round((tmp/N)**(0.5), 1)

print(std(L))

