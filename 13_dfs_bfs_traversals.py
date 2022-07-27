""" Python Script to implement Depth First Search, Breadth First Search 
traversals on a graph """
# Written by EKSHITH.KOLLA
# Date: 2/7/2021
# This Program may be a menu driven code for DFS AND BFS
#DFS
graph={'a':['b','c','g'],
'b':['d','e'],
'c':['d'],
'd':['f','e'],
'e':[],
'f':['g'],
'g':['c']
}

visited = set()
def dfs(visited,graph,node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)

# Driver Code
dfs(visited,graph,'a')

#BFS
graph={'a':['b','c','g'],
'b':['d','e'],
'c':['d'],
'd':['e','f'],
'e':[],
'f':['g'],
'g':['c']
}

visited=[]
queue=[]
def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        s=queue.pop(0)
        print(s)
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Driver Code
bfs(visited,graph,'a')
"""
OUTPUT:
=============== RESTART: C:/Users/lenovo/Downloads/linear_list.py ==============
a
b
d
f
g
c
e
a
b
c
g
d
e
f
"""
