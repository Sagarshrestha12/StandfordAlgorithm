from collections import defaultdict
def getDirectedgraph():
    with open('dj.txt') as fh:
        data=defaultdict(list)
        for line in fh:
            fields=line.split('\t')[:-1]
            vertex=int(fields.pop(0))
            edge=[ tuple([int(dd) for dd in ff.split(',')]) for ff in fields]
            data[vertex]=data[vertex]+edge
    return data


def maxx():
    return 100000

def Dijkstra(graph):
    X=dict()
    X[1]=True # since single source is first marked as visted so it should be in set X
    # A is dictionary to calculate the shortest distance from source vertex s to destination vertex v
    A= defaultdict(maxx) 
    # since distance from the source vertex to itshelf is empty path so considering the distance equals to 0
    A[1]=0
    # since we should  be  visiting whole vertex one vertex at time 
    # so we should loop until the lenght of the  dict X and dict data 
    while(len(graph)!=len(X)):
        dist=0
        min_dist=maxx()
        for vertex in X:
            for destination_vertex,length in graph[vertex]:
                if destination_vertex in X.keys():
                    continue
                if A[vertex] + length < min_dist:
                    min_dist= A[vertex] + length
                    dist=destination_vertex
        A[dist]=min_dist
        X[dist]=True
    return A

graph=getDirectedgraph()
distance=Dijkstra(graph)
target=[7,37,59,82,99,115,133,165,188,197]
whole=list()
for i in target:
    whole.append(distance[i])
for i in whole:
    print(i,end=',')


