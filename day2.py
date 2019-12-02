import re

input_data = open('inputs/day2.in','r').read().strip()#.split('\n')

#data = [re.findall(r'exp',line) for line in input_data]
data = [int(i) for i in re.findall(r'\d+',input_data)]
#data = [1,0,0,0,99]
#data = [2,3,0,3,99]
#data = [1,1,1,4,99,5,6,0,99]
#data = [1,9,10,3,2,3,11,0,99,30,40,50]

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
