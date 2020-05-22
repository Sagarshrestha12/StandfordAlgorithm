from collections import defaultdict

def getgraph():
    org=defaultdict(list)
    rorg=defaultdict(list)
    with open("test.txt") as fh:
        for line in fh:
            x=list(map(int,line.split()))
            org[x[0]]=org[x[0]]+[x[1]]
            rorg[x[1]]=rorg[x[1]]+[x[0]]
    return org,rorg
source=None
def DFS_loop(graph,reversed=True):
    if reversed:
        global t
        for vertex in range(9,0,-1):
            if not explored[vertex]:
                DFS(graph,vertex,reversed)
    else:
        global source
        source=None
        for time in sorted(finishing_time.keys(),reverse=True):
            if not explored[finishing_time[time]]:
                source=finishing_time[time]
                DFS(graph,finishing_time[time],reversed)
t=0
def DFS(graph,i,reversed):
    if reversed:
        global t
        explored[i]=True
        for dest in graph[i]:
            if not explored[dest]:
                DFS(graph,dest,reversed)
        t+=1
        finishing_time[t]=i
    else:
        global source
        #print(source)
        leader[i]=source
        
        #print(leader)
        explored[i]=True
        for dest in graph[i]:
            if not explored[dest]:
                DFS(graph,dest,reversed)



finishing_time={}
explored=defaultdict(bool)
leader={}
for i in range(1,5):
    leader[i]=0
#print(leader)
oo,roo=getgraph()
DFS_loop(roo)
#print(finishing_time)
#print(explored)
explored=defaultdict(bool)
DFS_loop(oo,reversed=False)
#print(explored)
#print(leader)
total=[]
pre=0
asc= sorted(list(leader.values()))
#print(asc)
for i in range(len(asc)-1):
    if asc[i] != asc[i+1]:
        total.append(i+1-pre)
        pre=i+1
total.append(len(asc)-pre)
tto=sorted(total,reverse=True)
print(tto[0:7])





