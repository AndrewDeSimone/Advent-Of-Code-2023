#ingestion
data = 'real' #test/real
workflows, partsList = open(f'Day 19\star1\\{data}input.txt', 'r').read().split('\n\n')
partsList = partsList.split('\n')
workflows = workflows.split('\n')

#convert parts from strings to dicts
for i in range(0,len(partsList)):
    part = partsList[i][1:-1]
    part = part.split(',')
    partDict = {}
    for j in part:
        partDict[j.split('=')[0]] = int(j.split('=')[1])
    partsList[i] = partDict

#handle workflows
workflowDictionary = {}
for i in workflows:
    name = i.split('{')[0]
    rules = i.split('{')[1][:-1].split(',')
    workflowDictionary[name] = rules

total = 0
for part in partsList:
    workflow = 'in'
    while not workflow in ['A', 'R']:
        workflow = workflowDictionary[workflow]
        for j in workflow:
            if ':' in j:
                rule = j.split(':')[0]
                outcome = j.split(':')[1]
                if '<' in rule:
                    if part[rule.split('<')[0]] < int(rule.split('<')[1]):
                        workflow = outcome
                        break
                if '>' in rule:
                    if part[rule.split('>')[0]] > int(rule.split('>')[1]):
                        workflow = outcome
                        break
            else:
                workflow = j
    if workflow == 'A':
        total += sum(part.values())

print(total)