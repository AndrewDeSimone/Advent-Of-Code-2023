import re
import math
data = 'real' #test/real
input = open(f'Day 20\star1\\{data}input.txt', 'r').read().split('\n')

connections = {}
kind = {}
state = {}
mapForLCM = {}

for i in input:
    name = re.sub(' |%|&', '', i.split('->')[0])
    connections[name] = re.sub(' ', '', i.split('->')[1]).split(',')
    if '%' in i:
        kind[name] = 'flip-flop'
        state[name] = 'off'
    elif '&' in i:
        kind[name] = 'conjunction'
        state[name] = {}

for i in kind.keys():
    if kind[i] == 'conjunction':
        for j in connections.keys():
            if i in connections[j]:
                state[i][j] = 'low'

kind['broadcaster'] = 'broadcaster'
    
lowPulses = 0
highPulses = 0

for i in range(0, 10000):
    toBeHandled = [('broadcaster', 'low', 'button')]
    lowPulses += 1
    while toBeHandled:
        name, pulse, receivedFrom = toBeHandled.pop(0)
        if name not in kind.keys():
            continue
        if name == 'broadcaster':
            for j in connections['broadcaster']:
                toBeHandled.append((j, 'low', 'broadcaster'))
                lowPulses += 1
        elif kind[name] == 'flip-flop':
            if pulse == 'low':
                if state[name] == 'off':
                    state[name] = 'on'
                    for j in connections[name]:
                        toBeHandled.append((j, 'high', name))
                        highPulses += 1
                else:
                    state[name] = 'off'
                    for j in connections[name]:
                        toBeHandled.append((j, 'low', name))
                        lowPulses += 1
        elif kind[name] == 'conjunction':
            state[name][receivedFrom] = pulse
            response = 'low'
            for j in state[name].values():
                if j == 'low':
                    response = 'high'
            if response == 'low':
                for j in connections[name]:
                        toBeHandled.append((j, 'low', name))
                        lowPulses += 1
            else:
                for j in connections[name]:
                        if j == 'kz':
                            if not name in mapForLCM.keys():
                                mapForLCM[name] = i+1
                        toBeHandled.append((j, 'high', name))
                        highPulses += 1
        

print(math.lcm(*list(mapForLCM.values())))