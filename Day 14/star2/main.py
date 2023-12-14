data = 'real' #test/real
input = open(f'Day 14\star2\\{data}input.txt', 'r').read().split('\n')

input = list(map(list, input))

for i in range(0, 1000):
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
    #move rocks left
    for col in range(0,len(input[0])):
        for row in range(0,len(input)):
            if input[row][col] == 'O':
                temp = col
                while temp > 0:
                    if input[row][temp-1] == '.':
                        input[row][temp-1] = 'O'
                        input[row][temp] = '.'
                        temp-=1
                    else:
                        break
    #move rocks down
    for row in range(len(input)-1, -1, -1):
        for col in range(0,len(input[0])):
            if input[row][col] == 'O':
                temp = row
                while temp < len(input)-1:
                    if input[temp+1][col] == '.':
                        input[temp+1][col] = 'O'
                        input[temp][col] = '.'
                        temp+=1
                    else:
                        break
    #move rocks right
    for col in range(len(input[0])-1,-1, -1):
        for row in range(0,len(input)):
            if input[row][col] == 'O':
                temp = col
                while temp < len(input[0])-1:
                    if input[row][temp+1] == '.':
                        input[row][temp+1] = 'O'
                        input[row][temp] = '.'
                        temp+=1
                    else:
                        break

#count load
total = 0
for row in range(0,len(input)):
    for col in range(0,len(input[0])):
        if input[row][col] == 'O':
            total += len(input) - row

print(total)