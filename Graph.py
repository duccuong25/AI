'''
definition: data structure represents relations among the objects
set of nodes (objects) linked together via links (relations)
node: called vertex (nodes: vertices)
link: called edge (links: edges)

applications: represents maps (cities, routes), LLMs (subjects -- verbs --- adverbs --- adjectives) -> optimization
maps: optimize route length, money, time
societies: 
networking: routers -> optimize: amount ò information transferred
constructions: optimize power cable length, water tube length

classification:
directed/undirected graphs
directed graph: A ---> B (undirected graph: A --- B)

weighted/unweighted graphs
weighted graph: A --3-- B (unweighted graph: A --- B)

represent a graph:
edge list: [(A,B, 8), (B,C,4), (A,F,5), ...]

adjacent list:
A: B (data, weight) --> C (B, C are A's neighbors)
B: A --> C --> F
...

adjacent matrix = 
[[0, 8, 2, 0, 0],
 [1, 0, 0, 0, 1],
 [1, 0, 0, 1, 0],
 [0, 0, 1, 0, 1],
 [0, 1, 0, 1, 0]]

traversal:
depth first search
breadth first search

Dijkstra:


Minimum spanning tree: spanning tree whose total weights is minimum
Spanning tree: tree whose all nodes are the vertices of the graph 
Algorithms:
- Prim-Jarnik Algorithm
- Kruskal Algorithm
'''

from ArrayStack import ArrayStack
from ArrayQueue import ArrayQueue
from Heap import MinHeap as MH
from SinglyLinkedList import SinglyLinkedList as SList
from PriorityQueue import PriorityQueue as PQ

def dfs(graph_aM, sV):
    ''' depth first search
    input:
    graph: adjacent matrix
    sV: start vertex
    output: 
    array
    '''
    nV =  len(graph_aM) # the number of vertices
    visited = [False] * nV
    # print(visited)
    aStack = ArrayStack()
    aStack.push(sV)
    # visited[sV] = True
    while not aStack.isEmpty():
        p = aStack.pop()
        if not visited[p.data]:
            visited[p.data] = True
            print(p.data, end = "  ")
            for i in range(nV-1, -1, -1):
                if(graph_aM[p.data][i] != 0 and not visited[i]):
                    aStack.push(i)
                    # visited[i] = True

    for i in range(nV):
        if not visited[i]:
            aStack.push(i)
            visited[i] = True
            while not aStack.isEmpty():
                p = aStack.pop()
                print(p.data, end = "  ")
                for i in range(nV-1, -1, -1):
                    if(graph_aM[p.data][i] != 0 and not visited[i]):
                        aStack.push(i)
                        visited[i] = True

def dfs_rec(graph_aM, sV):
    nV =  len(graph_aM) # the number of vertices
    visited = [False] * nV
    def dfs_rec_(graph_aM, sV):
        visited[sV] = True
        print(sV, end = "  ")
        for i in range(nV):
            if(graph_aM[sV][i] != 0 and not visited[i]):
                dfs_rec_(graph_aM, i)
    dfs_rec_(graph_aM, sV)


def bfs(graph_aM, sV):
    ''' breadth first search
    input:
    graph: adjacent matrix
    sV: start vertex
    output: 
    array
    '''
    nV = len(graph_aM)
    visited = [False] * nV
    aQueue = ArrayQueue()
    visited[sV] = True
    aQueue.enqueue(sV)
    while not aQueue.isEmpty():
        n = aQueue.dequeue()
        print(n.data, end = "  ")
        for i in range(nV):
            if not visited[i] and graph_aM[n.data][i] != 0:
                aQueue.enqueue(i)
                visited[i] = True

def bfs_rec(graph_aM, sV):
    nV = len(graph_aM)
    visited = [False] * nV
    aQueue = ArrayQueue()
    visited[sV] = True
    aQueue.enqueue(sV)
    def bfs_rec_(graph_aM, queue):
        if not queue.isEmpty():
            n = queue.dequeue()
            print(n.data, end = "  ")
            for i in range(nV):
                if not visited[i] and graph_aM[n.data][i] != 0:
                    queue.enqueue(i)
                    visited[i] = True
            bfs_rec_(graph_aM, queue)
    
    bfs_rec_(graph_aM, aQueue)


def Dijkstra(graph_aM, sV):
    nV = len(graph_aM)
    shortestDist = [float("Inf")] * nV
    pNodes = [""] * nV
    shortestDist[sV] = 0
    mH = MH()
    mH.insert([shortestDist[sV], sV])
    while not mH.isEmpty():
        _ , n = mH.arrayNodes[0].data
        mH.delete(mH.arrayNodes[0].data)
        for i in range(nV):
            if graph_aM[n][i] != 0:
                newDist = shortestDist[n] + graph_aM[n][i]
                if newDist < shortestDist[i]:
                    shortestDist[i] = newDist
                    pNodes[i] = n
                    mH.insert([shortestDist[i], i])

    vertices = [i for i in range(nV)]
    print(vertices)
    print(shortestDist)
    print(pNodes)
    return vertices, shortestDist, pNodes

def reconstructShortestPath(graph_aM, sV, eV):
    vertices, shortestDist, pNodes = Dijkstra(graph_aM, sV)
    path = SList()
    current = eV
    path.insertFirst(current)
    while current != sV:
        path.insertFirst(pNodes[current])
        current = pNodes[current]
    path.disp()
    return path


def Prim_Jarnik(graph_aM, sV):
    '''
    output: edge list [[v1, v2], [v2, v3], ...]
    '''
    nV = len(graph_aM)
    visited = []
    pQ = PQ()
    mst = []
    visited.append(sV)
    for i in range(nV):
        if graph_aM[sV][i] != 0:
            pQ.enqueue([graph_aM[sV][i], sV, i])
    while not pQ.isEmpty() and len(visited) < nV:
        w, bV, eV = pQ.dequeue().data
        if eV not in visited:
            visited.append(eV)
            mst.append([bV, eV])
            for i in range(nV):
                if graph_aM[eV][i] != 0 and i not in visited:
                    pQ.enqueue([graph_aM[eV][i], eV, i])
    
    print(visited)
    print(mst)
    return mst

def Kruskal(graph_aM):
    nV = len(graph_aM)
    pQ = PQ()
    for i in range(nV):
        for j in range(i, nV, 1):
            if graph_aM[i][j] != 0:
                pQ.enqueue([graph_aM[i][j], i, j])
    parents = [i for i in range(nV)]
    def findFather(v):
        if v == parents[v]: return v
        parents[v] = findFather(parents[v])
        return parents[v]
    def isCycle(v1, v2):
        p1 = findFather(v1)
        p2 = findFather(v2)
        if p1 == p2: return True
        else:
            parents[p2] = p1 # parents[v2] = v1
            parents[v2] = findFather(parents[v2]) # reset father
            return False
    mst = []
    while not pQ.isEmpty() and len(mst) < nV-1:
        w, v1, v2 = pQ.dequeue().data
        if not isCycle(v1, v2):
            mst.append([v1, v2])
    
    print(parents)
    print(mst)
    return mst
        
        


aM = [[0, 1, 1, 0, 0],
      [1, 0, 0, 0, 1],
      [1, 0, 0, 1, 1],
      [0, 0, 1, 0, 1],
      [0, 1, 1, 1, 0]]

# aM = [[0, 1, 1, 0, 0, 0, 0],
#       [1, 0, 0, 0, 1, 0, 0],
#       [1, 0, 0, 1, 0, 0, 0],
#       [0, 0, 1, 0, 1, 0, 0],
#       [0, 1, 0, 1, 0, 0, 0],
#       [0, 0, 0, 0, 0, 0, 1],
#       [0, 0, 0, 0, 0, 1, 0]]

# dfs(aM, 0)
# print()
# # bfs(aM, 0)
# dfs_rec(aM, 0)

# bfs(aM, 0)
# print()
# bfs_rec(aM, 0)

aM2 = [[0, 2, 0, 8, 0, 0],
       [2, 0, 0, 5, 6, 0],
       [0, 0, 0, 0, 9, 3],
       [8, 5, 0, 0, 3, 2],
       [0, 6, 9, 3, 0, 1],
       [0, 0, 3, 2, 1, 0]]

# _, _, _ = Dijkstra(aM2, 0)

# reconstructShortestPath(aM2, 0, 2)

aM3 = [[0, 2, 3, 3, 0, 0],
       [2, 0, 4, 0, 3, 0],
       [3, 4, 0, 0, 1, 6],
       [3, 0, 0, 0, 0, 7],
       [0, 3, 1, 0, 0, 8],
       [0, 0, 6, 7, 8, 0]]

# mst = Prim_Jarnik(aM3, 0)
mst = Kruskal(aM2)