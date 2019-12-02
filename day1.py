input_data = open('inputs/day1.in','r').read().strip().split('\n')

fuel = [max(int(int(mass)/3)-2,0) for mass in input_data]
print('Part 1: ',sum(fuel))

fuel_total = 0
for mass in fuel:
    fuel_addition = mass
    while fuel_addition > 0:
        fuel_total += fuel_addition
        fuel_addition = max(int(fuel_addition/3)-2,0)

print('Part 2: ', fuel_total)
