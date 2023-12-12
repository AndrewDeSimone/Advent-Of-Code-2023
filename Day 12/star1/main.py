data = 'real' #test/real
input = open(f'Day 12\star1\\{data}input.txt', 'r').read().split('\n')

def legalRow(row, rule):
    rule = rule.copy()
    row = row.copy()
    row = ''.join(row)
    row = row.split('.')
    while '' in row:
        row.remove('')
    if len(row) != len(rule):
        return int(False)
    while len(rule) != 0:
        if len(row.pop()) != rule.pop():
            return int(False)
    return int(True)



def validRows(row, rule):
    row = row.copy()
    if not '?' in row:
        return int(legalRow(row, rule))
    count = 0
    first = row.index('?')
    row[first] = '#'
    count += validRows(row, rule)
    row[first] = '.'
    count += validRows(row, rule)
    return count



sum = 0
for row in input:
    row, rule = row.split(' ')
    row = list(row)
    rule = rule.split(',')
    rule = [int(i) for i in rule]
    temp = validRows(row, rule)
    sum += temp

print(sum)