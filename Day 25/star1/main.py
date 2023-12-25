import networkx as nx
data = 'real' #test/real
input = open(f'Day 25\star1\\{data}input.txt', 'r').read().split('\n')

g = nx.Graph()

for connection in input:
    left, right = connection.split(': ')
    for connected in right.split(' '):
        g.add_edge(left, connected)

splitted = nx.spectral_bisection(g)
print(len(splitted[0]) * len(splitted[1]))