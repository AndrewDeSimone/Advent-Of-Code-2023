data = 'real' #test/real
input = open(f'Day 13\star1\\{data}input.txt', 'r').read().split('\n\n')


def verticalReflect(pattern):
    pattern = pattern.split('\n')
    for col in range(1, len(pattern[0])):
        failed = False
        for row in pattern:
            left = row[:col]
            right = row[col:]
            left = left[::-1]
            if len(left)<len(right):
                right = right[:len(left)]
            else:
                left = left[:len(right)]
            if left != right:
                failed = True
        if not failed:
            return col


def horizontalReflect(pattern):
    pattern = pattern.split('\n')
    for row in range(1, len(pattern)):
        top = pattern[:row]
        bottom = pattern[row:]
        top = top[::-1]
        if len(top)<len(bottom):
                bottom = bottom[:len(top)]
        else:
            top = top[:len(bottom)]
        if top == bottom:
            return row * 100

summary = 0

for pattern in input:
    vert = verticalReflect(pattern)
    if vert != None:
        summary += vert
    else:
        summary += horizontalReflect(pattern)

    

print(summary)