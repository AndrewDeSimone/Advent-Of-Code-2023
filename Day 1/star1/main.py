import re

data = 'real' #test/real
input = open(f'Day 1\star1\\{data}input.txt', 'r').read().split()

#remove letters
for i in range(0,len(input)):
    input[i] = re.sub('[^0-9]', '', input[i])
sum = 0
for i in input:
    sum += int(i[0])*10 + int(i[len(i)-1])

print(sum)