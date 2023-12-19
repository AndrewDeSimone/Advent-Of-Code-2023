data = 'real'
work = open(f'Day 19\star2\\{data}input.txt', 'r').read().split('\n\n')[0]
workflows = {name: rules[:-1].split(',') for name, rules in (line.split('{') for line in work.splitlines())}

def make_rules(current, rules):
    if current == 'A':
        acceptedRules.append(rules)
    elif current != 'R':
        curRule= []
        for rule in workflows[current][:-1]:
            if rule not in 'AR':
                next_workflow = rule.split(':')[1]
                make_rules(next_workflow, rules + curRule+ [rule.split(':')[0]])
                if rule[1] == '<':
                    curRule.append(f'{rule.split(":")[0].split("<")[0]}>={rule.split(":")[0].split("<")[1]}')
                elif rule[1] == '>':
                    curRule.append(f'{rule.split(":")[0].split(">")[0]}<={rule.split(":")[0].split(">")[1]}')
        else:
            next_workflow = workflows[current][-1]
            make_rules(next_workflow, rules + curRule)

acceptedRules = []
make_rules('in', [])
sum = 0
for r in acceptedRules:
    maxs = {x: 4001 for x in 'xmas'}
    mins = {x: 0 for x in 'xmas'}
    for s in r:
        if s[0] in 'xmas' and s[1] == '<':
            maxs[s[0]] = min(maxs[s[0]], int(s[2:])) if s[2] != '=' else min(maxs[s[0]], int(s[3:]) + 1)
        elif s[0] in 'xmas' and s[1] == '>':
            mins[s[0]] = max(mins[s[0]], int(s[2:])) if s[2] != '=' else max(mins[s[0]], int(s[3:]) - 1)
    product = 1
    for key in maxs:
        product *= (maxs[key] - mins[key] - 1)
    sum += product
print(sum)