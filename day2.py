import re

input_data = open('inputs/day2.in','r').read().strip()#.split('\n')

data = [int(i) for i in re.findall(r'\d+',input_data)]

data[1] = 12
data[2] = 2
i = 0
while data[i] != 99:
    if data[i] == 1:
        data[data[i+3]] = data[data[i+1]] + data[data[i+2]]
    elif data[i] == 2:
        data[data[i+3]] = data[data[i+1]] * data[data[i+2]]
    else:
        error('error')
    i = i+4;

print('Part 1:', data[0])

for verb in range(100):
    for noun in range(100):
        data = [int(i) for i in re.findall(r'\d+',input_data)]
        data[1] = noun
        data[2] = verb
        i = 0
        while data[i] != 99:
            if data[i] == 1:
                data[data[i+3]] = data[data[i+1]] + data[data[i+2]]
            elif data[i] == 2:
                data[data[i+3]] = data[data[i+1]] * data[data[i+2]]
            else:
                break
            i = i+4;
        if data[0] == 19690720:
            print('Part 2:',100*noun+verb)
            break
    else:
        continue
    break
