import re

input_data = open('inputs/day6.in','r').read().strip().split('\n')

orbits = {orbit.split(')')[1]: orbit.split(')')[0] for orbit in input_data}

total_orbits = 0
for orbit in orbits:
    while orbit in orbits:
        total_orbits += 1
        orbit = orbits[orbit]

print('Part 1:',total_orbits)

path = {}
steps = 0
current = orbits['YOU']
while current in orbits:
    path[current] = steps
    steps += 1
    current = orbits[current]

steps = 0
current = orbits['SAN']
while current not in path:
    steps += 1
    current = orbits[current]

print('Part 2:',steps+path[current])
