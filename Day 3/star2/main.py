import re
data = 'real' #test/real
input = open(f'Day 3\star2\\{data}input.txt', 'r').read().split('\n')

sum = 0

for i in range(0, len(input)):
    for j in range(0, len(input[0])):
        number = []
        if input[i][j]=='*':
            #check for above match
            if i != 0:
                #returns true when i-1, j is not a number
                if re.sub('[0-9]', '', input[i-1][j]):
                    if j != 0:
                        #returns true when i-1, j-1 is a number
                        if re.sub('[^0-9]', '', input[i-1][j-1]):
                            curr = j
                            currentMatch = ''
                            while curr!=0 and re.sub('[^0-9]', '', input[i-1][curr-1]):
                                currentMatch = input[i-1][curr-1] + currentMatch
                                curr-=1
                            number.append(int(currentMatch))
                    if j != len(input[i])-1:
                        if re.sub('[^0-9]', '', input[i-1][j+1]):
                            curr = j
                            currentMatch = 0
                            while curr!=len(input[i])-1 and re.sub('[^0-9]', '', input[i-1][curr+1]):
                                currentMatch *= 10
                                currentMatch += int(input[i-1][curr+1])
                                curr+=1
                            number.append(currentMatch)
                else:
                    rightMost = j
                    while rightMost != len(input)-1 and re.sub('[^0-9]', '', input[i-1][rightMost]):
                        rightMost+=1
                    curr = rightMost
                    currentMatch = ''
                    while curr!=0 and re.sub('[^0-9]', '', input[i-1][curr-1]):
                        currentMatch = input[i-1][curr-1] + currentMatch
                        curr-=1
                    number.append(currentMatch)
            #check left match
            if j!=0:
                if re.sub('[^0-9]', '', input[i][j-1]):
                        curr = j
                        currentMatch = ''
                        while curr!=0 and re.sub('[^0-9]', '', input[i][curr-1]):
                            currentMatch = input[i][curr-1] + currentMatch
                            curr-=1
                        number.append(int(currentMatch))
            #check right match
            if j != len(input[0]):
                if re.sub('[^0-9]', '', input[i][j+1]):
                    curr = j
                    currentMatch = 0
                    while curr!=len(input[i])-1 and re.sub('[^0-9]', '', input[i][curr+1]):
                            currentMatch *= 10
                            currentMatch += int(input[i][curr+1])
                            curr+=1
                    number.append(currentMatch)
            #check for below match
            if i != len(input)-1:
                #returns true when i-1, j is not a number
                if re.sub('[0-9]', '', input[i+1][j]):
                    if j != 0:
                        #returns true when i-1, j-1 is a number
                        if re.sub('[^0-9]', '', input[i+1][j-1]):
                            curr = j
                            currentMatch = ''
                            while curr!=0 and re.sub('[^0-9]', '', input[i+1][curr-1]):
                                currentMatch = input[i+1][curr-1] + currentMatch
                                curr-=1
                            number.append(int(currentMatch))
                    if j != len(input[i])-1:
                        if re.sub('[^0-9]', '', input[i+1][j+1]):
                            curr = j
                            currentMatch = 0
                            while curr!=len(input[i])-1 and re.sub('[^0-9]', '', input[i+1][curr+1]):
                                currentMatch *= 10
                                currentMatch += int(input[i+1][curr+1])
                                curr+=1
                            number.append(currentMatch)
                else:
                    rightMost = j
                    while rightMost != len(input)-1 and re.sub('[^0-9]', '', input[i+1][rightMost]):
                        rightMost+=1
                    curr = rightMost
                    currentMatch = ''
                    while curr!=0 and re.sub('[^0-9]', '', input[i+1][curr-1]):
                        currentMatch = input[i+1][curr-1] + currentMatch
                        curr-=1
                    number.append(currentMatch)
        if(len(number) == 2):
            sum += int(number[0]) * int(number[1])

print(sum)
        
