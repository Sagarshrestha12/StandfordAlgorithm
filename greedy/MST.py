"""Copying the array deeply

This function copy an array such that any change to one array doesn't reflect
on the another array like in shallow.
"""
def deepcopy(arr):
    newArr=[];
    for i in range(len(arr)):
        newArr.append(arr[i]);
    return newArr;

# Reading the data from the txt file
with open('./greedy/input/mst.txt') as file:
    lines = file.readlines();
    noOfNodes, noOfEdges=[int(i) for i in lines[0].strip().split()];
    nodes=[];
    graph={}
    for i in range(1,noOfEdges+1):
        detail= lines[i].strip().split();
        connection = tuple([int(i) for i in detail[:2]])
        for i in connection:
            if i not in nodes:
                nodes.append(i)

        edge_cost= int(detail[2]);
        graph[connection]=edge_cost;


"""Implementation of minimal cut property

A cut of connected graph is minimal set of edges whose removal seperate the graph into two
components. Minimal Cut Property says if one of the edges has weights smaller than other edges
in cut then it is in MST
"""
def cheapeastEdge(visited,unvisited ,graph):
    mini=100000;
    vertices=tuple();
    for key, value in graph.items():
        if(((key[0] in unvisited) and (key[1] in visited)) or ((key[1] in unvisited) and (key[0] in visited))):
            if(value<mini):
                mini =value;
                vertices=key
    return(vertices, mini);


""" Computing Minimum Spanning Tree

Compute the minimum spanning Tree using Greedy approch for finding edges of minimum weights
in cut of visited and unvisited graph.
"""
def MST(nodes,graph):
    A=[]
    B=deepcopy(nodes)
    A.append(B[0])
    B.remove(B[0])
    MST={}
    while(B):
        vertices,m=cheapeastEdge(A,B,graph);
        for i in vertices:
            if i not in A:
                A.append(i);
                B.remove(i)
        MST[vertices]=m
    return MST;

# Finding weights of MST
def findMinimumCost(mst):
    minimum_cost=0;
    for value in mst.values():
        minimum_cost+=value;
    return minimum_cost;

mst = MST(nodes,graph)
print(findMinimumCost(mst))
#  -3612829
# print(graph)
# while(X!=A):
#     ver,m=cheapeastEdge(A,B,graph);
#     for i in ver:
#         if i not in A:
#             A.append(i);
#             B.remove(i)
#     print(ver,m)



# while(A!=X):
#     chepeastEdge();
