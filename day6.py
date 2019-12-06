import re

input_data = open('inputs/day6.in','r').read().strip().split('\n')

# def get_orbits(center):
#     all_children = orbit_map.get(center,set())
#     children = len(all_children)
#     orbits = 0
#     for satellite in all_children:
#         n_orbits,n_children = get_orbits(satellite)
#         orbits += n_orbits
#         children += n_children
#     return (orbits+children,children)
    
# orbit_map = {}
# for line in input_data:
#     center, satellite = line.split(')')
#     orbit_map.setdefault(center,set()).add(satellite)

# roots = {obj for obj in set(orbit_map) if obj not in set.union(*orbit_map.values())}

# print('Part 1:',sum({get_orbits(root)[0] for root in roots}))

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
