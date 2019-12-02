import re

input_data = open('inputs/dayx.in','r').read().strip().split('\n')

#data = [re.findall(r'exp',line) for line in input_data]
data = re.findall(r'\d+',input_data)

print(data)    
