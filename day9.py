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
        data[p1] = outputs
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
    outputs = data.get(p1,0)
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

#input_data = [109,19,204,-34,99]
#input_data = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
#input_data = [1102,34915192,34915192,7,4,7,99,0]
#input_data = [104,1125899906842624,99]
functions = {1: addition, 2: multiplication, 3: input_value, 4: output_value, 5: jump_true, 6: jump_false, 7: less_than, 8: equals, 9: rel_base}

data = {n: int(input_data[n]) for n in range(len(input_data))}
relative_base = 0
outputs = 0
inputs = [1]
ip = 0
while data.get(ip,0)%100 != 99:
    ip = functions[int(str(data.get(ip,0))[-2:])](ip)

print('Part 1:', outputs)

data = {n: int(input_data[n]) for n in range(len(input_data))}
relative_base = 0
outputs = 0
inputs = [2]
ip = 0
while data.get(ip,0)%100 != 99:
    ip = functions[int(str(data.get(ip,0))[-2:])](ip)

print('Part 2:', outputs)
