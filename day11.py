import itertools

input_data = open('inputs/day9.in','r').read().strip().split(',')

def addition(ind):
    global relative_base
    op = str(data.get(ind,0)).zfill(5)
    if op[-3:-2] == '1':
        p1 = ind+1
    elif op[-3:-2] == '2':
        p1 = relative_base + data.get(ind+1,0)
    else:
        p1 = data.get(ind+1,0)
    if op[-4:-3] == '1':
        p2 = ind+2
    elif op[-4:-3] == '2':
        p2 = relative_base + data.get(ind+2,0)
    else:
        p2 = data.get(ind+2,0)
    if op[-5:-4] == '2':
        p3 = relative_base + data.get(ind+3,0)
    else:
        p3 = data.get(ind+3,0)

    data[p3] = data.get(p1,0) + data.get(p2,0)
    return ind+4

def multiplication(ind):
    global relative_base
    op = str(data.get(ind,0)).zfill(5)
    if op[-3:-2] == '1':
        p1 = ind+1
    elif op[-3:-2] == '2':
        p1 = relative_base + data.get(ind+1,0)
    else:
        p1 = data.get(ind+1,0)
    if op[-4:-3] == '1':
        p2 = ind+2
    elif op[-4:-3] == '2':
        p2 = relative_base + data.get(ind+2,0)
    else:
        p2 = data.get(ind+2,0)
    if op[-5:-4] == '2':
        p3 = relative_base + data.get(ind+3,0)
    else:
        p3 = data.get(ind+3,0)

    data[p3] = data.get(p1,0) * data.get(p2,0)
    return ind+4

def input_value(ind):
    global relative_base
    op = str(data.get(ind,0))
    if op[-3:-2] == '1':
        p1 = ind+1
    elif op[-3:-2] == '2':
        p1 = relative_base + data.get(ind+1,0)
    else:
        p1 = data.get(ind+1,0)

    if inputs:
        data[p1] = inputs.pop(0)
    else:
        error()
        data[p1] = outputs[-1]
    return ind+2

def output_value(ind):
    global relative_base
    op = str(data.get(ind,0))
    if op[-3:-2] == '1':
        p1 = ind+1
    elif op[-3:-2] == '2':
        p1 = relative_base + data.get(ind+1,0)
    else:
        p1 = data.get(ind+1,0)

    global outputs
    outputs.append(data.get(p1,0))
    print(outputs)
    return ind+2

def jump_true(ind):
    global relative_base
    op = str(data.get(ind,0)).zfill(5)
    if op[-3:-2] == '1':
        p1 = ind+1
    elif op[-3:-2] == '2':
        p1 = relative_base + data.get(ind+1,0)
    else:
        p1 = data.get(ind+1,0)
    if op[-4:-3] == '1':
        p2 = ind+2
    elif op[-4:-3] == '2':
        p2 = relative_base + data.get(ind+2,0)
    else:
        p2 = data.get(ind+2,0)

    if data.get(p1,0):
        return data.get(p2,0)
    else:
        return ind+3

def jump_false(ind):
    global relative_base
    op = str(data.get(ind,0)).zfill(5)
    if op[-3:-2] == '1':
        p1 = ind+1
    elif op[-3:-2] == '2':
        p1 = relative_base + data.get(ind+1,0)
    else:
        p1 = data.get(ind+1,0)
    if op[-4:-3] == '1':
        p2 = ind+2
    elif op[-4:-3] == '2':
        p2 = relative_base+data.get(ind+2,0)
    else:
        p2 = data.get(ind+2,0)

    if not data.get(p1,0):
        return data.get(p2,0)
    else:
        return ind+3

def less_than(ind):
    global relative_base
    op = str(data.get(ind,0)).zfill(5)
    if op[-3:-2] == '1':
        p1 = ind+1
    elif op[-3:-2] == '2':
        p1 = relative_base + data.get(ind+1,0)
    else:
        p1 = data.get(ind+1,0)
    if op[-4:-3] == '1':
        p2 = ind+2
    elif op[-4:-3] == '2':
        p2 = relative_base + data.get(ind+2,0)
    else:
        p2 = data.get(ind+2,0)
    if op[-5:-4] == '2':
        p3 = relative_base + data.get(ind+3,0)
    else:
        p3 = data.get(ind+3,0)

    data[p3] = int(data.get(p1,0) < data.get(p2,0))
    return ind+4

def equals(ind):
    global relative_base
    op = str(data.get(ind,0)).zfill(5)
    if op[-3:-2] == '1':
        p1 = ind+1
    elif op[-3:-2] == '2':
        p1 = relative_base + data.get(ind+1,0)
    else:
        p1 = data.get(ind+1,0)
    if op[-4:-3] == '1':
        p2 = ind+2
    elif op[-4:-3] == '2':
        p2 = relative_base + data.get(ind+2,0)
    else:
        p2 = data.get(ind+2,0)
    if op[-5:-4] == '2':
        p3 = relative_base + data.get(ind+3,0)
    else:
        p3 = data.get(ind+3,0)

    data[p3] = int(data.get(p1,0) == data.get(p2,0))
    return ind+4

def rel_base(ind):
    global relative_base
    op = str(data.get(ind,0))
    if op[-3:-2] == '1':
        p1 = ind+1
    elif op[-3:-2] == '2':
        p1 = relative_base + data.get(ind+1,0)
    else:
        p1 = data.get(ind+1,0)

    relative_base += data.get(p1,0)
    return ind+2

functions = {1: addition, 2: multiplication, 3: input_value, 4: output_value, 5: jump_true, 6: jump_false, 7: less_than, 8: equals, 9: rel_base}

data = {n: int(input_data[n]) for n in range(len(input_data))}

paint = {(0,0): 0}
directions = {0: (0,-1), 1:  (1,0), 2: (0,1), 3: (-1,0)}

position = (0,0)
direction = 0
turn = False

relative_base = 0
outputs = []
inputs = []
ip = 0
while data.get(ip,0)%100 != 99:
    inputs = [paint.get(position,0)]
    ip = functions[int(str(data.get(ip,0))[-2:])](ip)
    if outputs:
        command = outputs.pop(0)
        if turn:
            direction = (direction + (command==1)-(command==0))%4
            position = (position[0]+directions[direction][0], position[1]+directions[direction][1])
        else:
            paint[position] = command
        turn = not turn
    print(str(data.get(ip,0)).zfill(5)[-5:-4])

print('Part 1:', paint)
