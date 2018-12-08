N = int(input())
L = input().split(' ')
L = [int(x) for x in L]

def mean(Data):
    return sum(Data)/len(Data)

def std(Data):
    mn = mean(Data) #saving this structure so it only is calculated once
    tmp = 0
    for x in Data:
        tmp += (x-mn)**2
    return round((tmp/N)**(0.5), 1)

print(std(L))

