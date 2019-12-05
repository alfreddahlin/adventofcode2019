import re

input_data = open('inputs/day5.in','r').read().strip().split(',')

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

    data[p1] = inputs.pop()
    return ind+2

def output_value(ind):
    op = str(data[ind])
    if op[-3:-2] != '0':
        p1 = data[ind+1]
    else:
        p1 = data[data[ind+1]]

    outputs.append(data[p1])
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

data = [int(i) for i in input_data]

inputs = [1]
outputs = []
i = 0
while data[i]%100 != 99:
    i = functions[int(str(data[i])[-2:])](i)

print('Part 1:', outputs[-1])

data = [int(i) for i in input_data]

inputs = [5]
outputs = []
i = 0
while data[i]%100 != 99:
    i = functions[int(str(data[i])[-2:])](i)

print('Part 2:', outputs[-1])
