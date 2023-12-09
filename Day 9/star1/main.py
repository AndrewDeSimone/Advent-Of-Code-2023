data = 'real' #test/real
input = open(f'Day 9\star1\\{data}input.txt', 'r').read().split('\n')

sum = 0

def getNext(sequence):
    if all(i == 0 for i in sequence):
        return 0
    newSeq = []
    for i in range(1, len(sequence)):
        newSeq.append(sequence[i] - sequence[i-1])
    return sequence[len(sequence)-1] + getNext(newSeq)

for i in input:
    temp = i.split(' ')
    fixedI = [int(j) for j in temp]
    sum += getNext(fixedI)

print(sum)