#Implementing median, mean and mode functions.



n = int(input())
l = input().split(' ')
l_int = [int(x) for x in l]

def meand(data):
  return sum(data)/n

def median(data):
    data.sort()
    if len(data) % 2 == 0:
        return (data[int(len(data)/2)] + data[int((len(data)/2)-1)])/2
    else:
        return data[int(len(data)+1)/2]

def mode(data):
    dicti = {}
    for p in data:
        if p in dicti:
            dicti[p] += dicti[p]
        else:
            dicti[p] = 1
    return max(dicti, key=dicti.get)




print(mean(l_int))
print(median(l_int))
print(mode(l_int))

