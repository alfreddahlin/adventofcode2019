import re

input_data = open('inputs/day3.in','r').read().strip().split('\n')
#input_data = ['R8,U5,L5,D3','U7,R6,D4,L4']
#input_data = ['R75,D30,R83,U83,L12,D49,R71,U7,L72','U62,R66,U55,R34,D71,R55,D58,R83']
data = {wire: re.findall(r'([a-zA-Z])(\d+)',path) for wire,path in enumerate(input_data)}

circuit = {}
circuit[(0,0)] = {}
for wire,path in data.items():
    i = (0,0)
    steps = 0
    for d,l in path:
        if d == 'U':
            inc = [0,-1]
        elif d == 'D':
            inc = [0,1]
        elif d == 'L':
            inc = [-1,0]
        elif d == 'R':
            inc = [1,0]
        for _ in range(int(l)):
            i = (i[0]+inc[0],i[1]+inc[1])
            steps += 1
            if i not in circuit.keys():
                circuit[i] = {}
            if wire not in circuit[i]:
                circuit[i][wire] = steps

min_dist = 999999
min_sum = 999999
for k,v in circuit.items():
    if len(v) > 1:
        d = abs(k[0]) + abs(k[1])
        s = sum(v.values())
        if d < min_dist:
            min_dist = d
        if s < min_sum:
            min_sum = s

print('Part 1: ',min_dist)
print('Part 2: ',min_sum)
