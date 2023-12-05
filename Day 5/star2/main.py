import re
data = 'real' #test/real
input = open(f'Day 5\star2\\{data}input.txt', 'r').read().split('\n\n')

#collect seeds and make them integers
seeds = re.findall('\d+', input[0])
for i in range(0,len(seeds)):
    seeds[i] = int(seeds[i])

#define mapping function
def createMap(mapText):
    mapText=mapText.split(':\n')[1].split('\n')
    rules = []
    for rule in mapText:
            rule = rule.split(' ')
            rules.append([int(rule[0]), int(rule[1]), int(rule[2])])
    def map(x, space):
        for i in rules:
             if x >= i[1] and x < i[1] + i[2]:
                  return ((x - i[1]) + i[0], min(space, (i[1]+i[2])-x))
        return x, space
    return map

#seed to soil map
seedtosoil = createMap(input[1])
soiltofertilizer = createMap(input[2])
fertilizertowater = createMap(input[3])
watertolight = createMap(input[4])
lighttotemperature = createMap(input[5])
temperaturetohumidity = createMap(input[6])
humiditytolocation = createMap(input[7])

minimum = 'first pass'

for i in range(0,len(seeds), 2):
    seed = seeds[i]
    space = seeds[i+1]
    while space > 0:
        soil, soilspace = seedtosoil(seed, space)
        fertilizer, fertilizerspace = soiltofertilizer(soil, soilspace)
        water, waterspace = fertilizertowater(fertilizer, fertilizerspace)
        light, lightspace = watertolight(water, waterspace)
        temperature, temperaturespace = lighttotemperature(light, lightspace)
        humidity, humidityspace = temperaturetohumidity(temperature, temperaturespace)
        location, locationspace = humiditytolocation(humidity, humidityspace)
        space = space - locationspace
        seed += locationspace
        if minimum == 'first pass':
             minimum = location
        minimum = min(minimum, location)

print(minimum)
