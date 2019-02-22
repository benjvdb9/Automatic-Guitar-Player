dist = [3.5, 3.2, 3, 2.8, 2.6, 2.5, 2.3, 2.2, 2.1, 1.9, 1.8, 1.7]

def calcmid(num, dist):
    return dist+num/2

past = [-0.25]
res = []
for elem in dist:
    length = sum(past) + len(past)*0.25
    r = calcmid(elem, length)
    past+= [elem]
    res += [r]

print(res)
