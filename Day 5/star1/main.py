import re
data = 'real' #test/real
input = open(f'Day 5\star1\\{data}input.txt', 'r').read().split('\n\n')

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
    def map(x):
        for i in rules:
             if x >= i[1] and x < i[1] + i[2]:
                  return (x - i[1]) + i[0]
        return x
    return map

#seed to soil map
seedtosoil = createMap(input[1])
soiltofertilizer = createMap(input[2])
fertilizertowater = createMap(input[3])
watertolight = createMap(input[4])
lighttotemperature = createMap(input[5])
temperaturetohumidity = createMap(input[6])
humiditytolocation = createMap(input[7])

print(min([humiditytolocation(temperaturetohumidity(lighttotemperature(watertolight(fertilizertowater(soiltofertilizer(seedtosoil(i))))))) for i in seeds]))