import re

data = 'real' #test/real
input = open(f'Day 3\star1\\{data}input.txt', 'r').read().split('\n')

sum = 0

for i in range(0,len(input)):
    j = 0
    while j in range(0, len(input[i])):
        adjacent = False
        number = 0
        while i<len(input) and j<len(input[0]) and re.sub('[^0-9]', '', input[i][j]):
            number *= 10
            number += int(input[i][j])
            if i != 0:
                if re.sub('[0-9]|\.', '', input[i-1][j]): adjacent = True
                if j != 0:
                    if re.sub('[0-9]|\.', '', input[i-1][j-1]): adjacent = True
                if j != len(input[i])-1:
                    if re.sub('[0-9]|\.', '', input[i-1][j+1]): adjacent = True
            if j != 0:
                    if re.sub('[0-9]|\.', '', input[i][j-1]): adjacent = True
            if j != len(input[i])-1:
                    if re.sub('[0-9]|\.', '', input[i][j+1]): adjacent = True
            if i != len(input)-1:
                if re.sub('[0-9]|\.', '', input[i+1][j]): adjacent = True
                if j != 0:
                    if re.sub('[0-9]|\.', '', input[i+1][j-1]): adjacent = True
                if j != len(input[i])-1:
                    if re.sub('[0-9]|\.', '', input[i+1][j+1]): adjacent = True
            j+=1
        if adjacent:
            sum+=number
        j+=1

print(sum)