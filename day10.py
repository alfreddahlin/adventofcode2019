import itertools, math

def norm(x,y):
    l = abs(math.gcd(x,y))
    return (int(x/l),int(y/l))

input_data = open('inputs/day10.in','r').read().strip().split('\n')

data = {(x,y): set() for y,row in enumerate(input_data) for x,sign in enumerate(row) if sign == '#'}

for p1,p2 in itertools.combinations(data,2):
    if p1 != p2:
        d = norm(p2[0]-p1[0],p2[1]-p1[1])
        data[p1].add(d)
        data[p2].add((-d[0],-d[1]))

station = max(data,key = lambda x: len(data[x]))

print('Part 1:',len(data[station]))


directions = sorted(data[station],key = lambda x: -math.atan2(*x))
removed = 0
while removed < 200:
    i = removed % len(directions)
    direction = directions[i]
    distance = 1
    while distance < 50:
        laser = (station[0]+distance*direction[0],station[1]+distance*direction[1])
        if data.pop(laser,None):
            latest = laser
            removed += 1
            break
        distance += 1
    else:
        directions.pop(i)

print('Part 2:', 100*latest[0]+latest[1])
