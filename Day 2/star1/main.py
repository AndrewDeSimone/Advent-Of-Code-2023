import re
data = 'real' #test/real
input = open(f'Day 2\star1\\{data}input.txt', 'r').read().split('\n')

sum = 0

for i in input:
    temp = i.split()
    gameid = re.sub('[^0-9]|,', '', temp[1])
    temp = temp[2:]
    temp = "".join(temp)
    rounds = temp.split(';')
    valid = True
    for j in rounds:
        for k in j.split(','):
            count = int(re.sub('[^0-9]', '', k))
            color = re.sub('[0-9]', '', k)
            if(color == 'red' and count > 12): valid = False
            if(color == 'green' and count > 13): valid = False
            if(color == 'blue' and count > 14): valid = False
    sum += valid * int(gameid)
print(sum)