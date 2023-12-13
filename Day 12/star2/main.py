from functools import lru_cache
data = 'real' #test/real
input = open(f'Day 12\star2\\{data}input.txt', 'r').read().split('\n')

@lru_cache(maxsize=None)
def possibleArrangements(row, rule):
    #base cases
    if not rule:
        if '#' not in row:
            return 1
        else:
            return 0
    if len(row) == 0:
        return 0

    nextSymbol = row[0]
    nextRule = rule[0]

    def dot():
        return possibleArrangements(row[1:], rule)

    def pound():
        current = row[:nextRule]
        current = current.replace('?', '#')
        if current != nextRule * '#':
            return 0
        if len(row) == nextRule:
            if len(rule) == 1:
                return 1
            return 0
        if row[nextRule] in '.?':
            return possibleArrangements(row[nextRule+1:], rule[1:])
        return 0

    if nextSymbol == '.':
        out = dot()
    if nextSymbol == '#':
        out = pound()
    if nextSymbol == '?':
        out = dot() + pound()
    
    return out


total = 0

for i in input:
    row, rule = i.split(' ')
    row = row + '?' + row + '?' + row + '?' + row + '?' + row
    rule = rule + ',' + rule + ',' + rule + ',' + rule + ',' + rule
    rule = tuple(map(int, rule.split(',')))
    arrangements = possibleArrangements(row, rule)
    total += arrangements

print(total)