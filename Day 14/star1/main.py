data = 'real' #test/real
input = open(f'Day 14\star1\\{data}input.txt', 'r').read().split('\n')

input = list(map(list, input))

#move rocks up
for row in range(0, len(input)):
    for col in range(0,len(input[0])):
        if input[row][col] == 'O':
            temp = row
            while temp > 0:
                if input[temp-1][col] == '.':
                    input[temp-1][col] = 'O'
                    input[temp][col] = '.'
                    temp-=1
                else:
                    break

#count load
total = 0
for row in range(0,len(input)):
    for col in range(0,len(input[0])):
        if input[row][col] == 'O':
            total += len(input) - row

print(total)