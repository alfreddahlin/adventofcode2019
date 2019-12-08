import re

input_data = open('inputs/day8.in','r').read().strip()#.split('\n')

width = 25
height = 6

data = re.findall(r'\d{%i}' % width*height,input_data)

occurance = {}
for n,layer in enumerate(data):
    occurance[n] = {c: layer.count(c) for c in set(layer)}

least = occurance[min(occurance, key = lambda x: occurance[x].get('0',0))]

print('Part 1:', least['1']*least['2'])

decode = {'0': ' ', '1': '#', '2': ' '}
pic = []
for p in zip(*data):
    pic.append(next((x for x in p if x != '2'),'2'))

print('Part 2:')
for y in range(height):
    for x in range(width):
        print(decode[pic[y*width+x]],end='')
    print()
