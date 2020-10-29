
from __future__ import print_function
from ortools.graph import pywrapgraph


arquivo = open("instancias/instance7.txt", "r")
node = arquivo.readline()
vert = arquivo.readline()
init = arquivo.readline()
fim = arquivo.readline()
node_start = []
end_nodes = []
capacities = []

for linha in arquivo:
    valores = linha.split()
    node_start.append(int(valores[0]))
    end_nodes.append(int(valores[1]))
    capacities.append(int(valores[2]))
    

max_flow = pywrapgraph.SimpleMaxFlow()
for i in range(0, len(node_start)):
    max_flow.AddArcWithCapacity(node_start[i], end_nodes[i], capacities[i])


 # Find the maximum flow between node 0 and node 4.
if max_flow.Solve(int(init), int(fim)) == max_flow.OPTIMAL:
    print('Max flow:', max_flow.OptimalFlow())
    print('')
    print('  Arc    Flow / Capacity')
    for i in range(max_flow.NumArcs()):
        print('%1s -> %1s   %3s  / %3s' % (
        max_flow.Tail(i),
        max_flow.Head(i),
        max_flow.Flow(i),
        max_flow.Capacity(i)))
    print('Source side min-cut:', max_flow.GetSourceSideMinCut())
    print('Sink side min-cut:', max_flow.GetSinkSideMinCut())
else:
    print('There was an issue with the max flow input.')


