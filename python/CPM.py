from collections import defaultdict
from collections import deque
import sys

class Node:
    def __init__(self,id,name,dur,es,ef,ls,lf) -> None:
        self.name = name
        self.id = id ; self.du = dur
        self.es = es; self.ef = ef
        self.ls = ls; self.lf = lf
    
nodes = {}
visited = {}
q = deque()
seq = deque()
forwardPass = defaultdict(list)
backwardPass = defaultdict(list)
criticalPath = []
totalDuration = 0
leaves = {} 

path = './activity.txt'
for lines in open(path):
    line = lines.rstrip('\n').split(',')
    id = int(line[0]); name = line[1]; duration = int(line[2])
    ef = 0
    if len(line) == 4:
        predecessors = line[3].split(';')
        for x in predecessors:
            x = int(x)
            forwardPass[x].append(id)
            backwardPass[id].append(x)
    else:
        q.append(id)
        ef = duration

    nodes[id] = Node(id,name,duration,0,ef,0,sys.maxsize)
    visited[id] = 0
    leaves[id] = 0

while q:
    outDegree = 0
    u = q.popleft()
    ef = nodes[u].ef
    for v in forwardPass[u]:
        nodes[v].es = max(ef,nodes[v].es)
        nodes[v].ef = nodes[v].es + nodes[v].du
        if visited[v] != 1:
            q.append(v)
            outDegree += 1

    if outDegree == 0 and visited[u] == 0:
        leaves[u] = 1
        totalDuration = max(totalDuration,nodes[u].ef)
        
    visited[u] = 1

for node,leaf in leaves.items():
    if leaf:
        nodes[node].lf = totalDuration
        nodes[node].ls = nodes[node].lf - nodes[node].du
        q.append(node)
        seq.append(node)
    visited[node] = 0


while q:
    u = q.popleft()
    ls = nodes[u].ls
    for v in backwardPass[u]:
        nodes[v].lf = min(nodes[v].lf,ls)
        nodes[v].ls = nodes[v].lf - nodes[v].du
            
        if visited[v] != 1:
            q.append(v)
        
    visited[u] = 1

while seq:
    u = seq.popleft()
    visited[u] = 0
    if nodes[u].es == nodes[u].ls:
        criticalPath.append(nodes[u].name)
        for v in backwardPass[u]:
            if visited[v] == 1:
                seq.append(v)
                visited[v] = 0

def printNodes(nodes):
    for key,value in nodes.items():
        print('id = {},node = {},duration = {},ES = {},EF = {},LS = {},LF = {}'
            .format(key,value.name,value.du,value.es,value.ef,value.ls,value.lf))
            
printNodes(nodes)

for i , e  in reversed(list(enumerate(criticalPath))):
    print(e,end = '')
    if i != 0:
        print('->',end='')