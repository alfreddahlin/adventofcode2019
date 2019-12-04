import re

min,max = open('inputs/day4.in','r').read().strip().split('-')

possible = set()
possible_strict = set()
for pw in range(int(min),int(max)+1):
    pw = str(pw)
    consecutive = False
    consecutive_strict = False
    if re.findall(r'(\d)\1',pw):
        consecutive = True
        if re.findall(r'(^|(.)(?!\2))(\d)\3{1}(?!\3)',pw):
            consecutive_strict = True
    else:
        continue
    for i in range(5):
        if pw[i] > pw[i+1]:
            break
    else:
        if consecutive:
            possible.add(pw)
            if consecutive_strict:
                possible_strict.add(pw)
print('Part 1:',len(possible))
print('Part 2:',len(possible_strict))
