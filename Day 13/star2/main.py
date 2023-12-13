data = 'real' #test/real
input = open(f'Day 13\star2\\{data}input.txt', 'r').read().split('\n\n')


def verticalReflect(pattern):
    pattern = pattern.split('\n')
    for col in range(1, len(pattern[0])):
        error = 0
        for row in pattern:
            left = col-1
            right = col
            while right < len(row) and left >= 0:
                if row[right] != row[left]:
                    error += 1
                right += 1
                left -= 1
        if error == 1:
            return col


def horizontalReflect(pattern):
    pattern = pattern.split('\n')
    for row in range(1, len(pattern)):
        error = 0
        top = row-1
        bottom = row
        while top >= 0 and bottom < len(pattern):
            for i in range(0, len(pattern[0])):
                if pattern[top][i] != pattern[bottom][i]:
                    error += 1
            top -= 1
            bottom += 1
        if error == 1:
            return row * 100

summary = 0

for pattern in input:
    vert = verticalReflect(pattern)
    if vert != None:
        summary += vert
    horizontal = horizontalReflect(pattern)
    if horizontal != None:
        summary += horizontal

    

print(summary)