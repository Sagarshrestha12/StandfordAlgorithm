"""
graph is dictnory which contains key and values where value is 
object refrence to list which contain 3 elements one as vertex to which it is connected
and another is boolean value to check wheather the given vertex is explored or not
"""


def DFS(graph, s_vertex):
    # set the s_vertex as explored
    graph[s_vertex][1] = True
    for key in graph[s_vertex][0]:  # for every edge from s to v
        if not graph[key][1]:  # if the vertex is not explored
            DFS(graph, key)
        graph[key][2] = current_label
        current_label -= 1
