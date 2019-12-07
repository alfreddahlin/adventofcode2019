import itertools

input_data = open('inputs/day7.in','r').read().strip().split(',')

def addition(ind):
    op = str(data[ind]).zfill(5)
    if op[-3:-2] != '0':
        p1 = data[ind+1]
    else:
        p1 = data[data[ind+1]]
    if op[-4:-3] != '0':
        p2 = data[ind+2]
    else:
        p2 = data[data[ind+2]]
    p3 = data[ind+3]

    data[p3] = p1 + p2
    return ind+4

def multiplication(ind):
    op = str(data[ind]).zfill(5)
    if op[-3:-2] != '0':
        p1 = data[ind+1]
    else:
        p1 = data[data[ind+1]]
    if op[-4:-3] != '0':
        p2 = data[ind+2]
    else:
        p2 = data[data[ind+2]]
    p3 = data[ind+3]

    data[p3] = p1 * p2
    return ind+4

def input_value(ind):
    op = str(data[ind])
    if op[-3:-2] != '0':
        p1 = data[ind+1]
    else:
        p1 = data[data[ind+1]]

    if inputs:
        data[p1] = inputs.pop(0)
    else:
        data[p1] = outputs
    return ind+2

def output_value(ind):
    op = str(data[ind])
    if op[-3:-2] != '0':
        p1 = data[ind+1]
    else:
        p1 = data[data[ind+1]]

    global outputs
    outputs = data[p1]
    return ind+2

def jump_true(ind):
    op = str(data[ind]).zfill(5)
    if op[-3:-2] != '0':
        p1 = data[ind+1]
    else:
        p1 = data[data[ind+1]]
    if op[-4:-3] != '0':
        p2 = data[ind+2]
    else:
        p2 = data[data[ind+2]]

    if p1:
        return p2
    else:
        return ind+3

def jump_false(ind):
    op = str(data[ind]).zfill(5)
    if op[-3:-2] != '0':
        p1 = data[ind+1]
    else:
        p1 = data[data[ind+1]]
    if op[-4:-3] != '0':
        p2 = data[ind+2]
    else:
        p2 = data[data[ind+2]]

    if not p1:
        return p2
    else:
        return ind+3

def less_than(ind):
    op = str(data[ind]).zfill(5)
    if op[-3:-2] != '0':
        p1 = data[ind+1]
    else:
        p1 = data[data[ind+1]]
    if op[-4:-3] != '0':
        p2 = data[ind+2]
    else:
        p2 = data[data[ind+2]]

    p3 = data[ind+3]
    data[p3] = int(p1 < p2)
    return ind+4

def equals(ind):
    op = str(data[ind]).zfill(5)
    if op[-3:-2] != '0':
        p1 = data[ind+1]
    else:
        p1 = data[data[ind+1]]
    if op[-4:-3] != '0':
        p2 = data[ind+2]
    else:
        p2 = data[data[ind+2]]

    p3 = data[ind+3]
    data[p3] = int(p1 == p2)
    return ind+4

functions = {1: addition, 2: multiplication, 3: input_value, 4: output_value, 5: jump_true, 6: jump_false, 7: less_than, 8: equals}

max_output = ((),-float('inf'))
for phase in itertools.permutations(range(5)):
    data = [int(i) for i in input_data]
    outputs = 0
    for amp in range(5):
        inputs = [phase[amp],outputs]
        i = 0
        while data[i]%100 != 99:
            i = functions[int(str(data[i])[-2:])](i)
    if max_output[1] < outputs:
        max_output = (phase, outputs)

print('Part 1:', max_output)


max_output = ((),-float('inf'))
for phase in itertools.permutations(range(5,10)):
    stored_data = {n: [int(i) for i in input_data] for n in range(5)}
    stored_ip = {n: 0 for n in range(5)}
    phase_list = list(phase)
    outputs = 0
    inputs = [phase_list.pop(0), outputs]
    i = 0
    data = stored_data[i]
    ip = stored_ip[i]
    while data[ip]%100 != 99:
        feed = int(str(data[ip])[-2:]) == 4
        ip = functions[int(str(data[ip])[-2:])](ip)
        if feed:
            stored_data[i] = data
            stored_ip[i] = ip
            i = (i+1)%5
            data = stored_data[i]
            ip = stored_ip[i]
            if phase_list:
                inputs.append(phase_list.pop(0))
#            inputs.append(outputs)
    if max_output[1] < outputs:
        max_output = (phase,outputs)

print('Part 2:', max_output)
