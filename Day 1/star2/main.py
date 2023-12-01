import re

def reverse(x):
  return x[::-1]

data = 'real' #test/real
input = open(f'Day 1\star2\\{data}input.txt', 'r').read().split()

sum = 0

numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
numberRep = {'zero':'0o', 'one': 'o1e', 'two': 't2o', 'three': 't3e', 'four':'4', 'five':'5e', 'six': '6', 'seven':'7n', 'eight':'e8t', 'nine': 'n9e'}

#forward pass
for i in input:
    temp = i
    for j in range(0, len(numbers)):
        temp = re.sub(numbers[j], numberRep[numbers[j]], temp)
    temp = re.sub('[^0-9]', '', temp)
    sum += int(temp[0])*10


#backwards pass
for i in input:
    temp = reverse(i)
    for j in range(0, len(numbers)):
        temp = re.sub(reverse(numbers[j]), reverse(numberRep[numbers[j]]), temp)
    temp = re.sub('[^0-9]', '', temp)
    sum+=int(temp[0])

print(sum)