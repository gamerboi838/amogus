graph = {
    '5' : ['3','7'],
  '3' : ['2', '4','32'],
  '7' : ['8'],
  '2' : [],
  '4' : ['9'],
  '8' : [],
  '9' : [],
    '32':[],
}

visited = set() 

def dls(visited, graph, node,depth,limit):  
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            if depth is not limit:
                depth=depth+1
                dls(visited, graph, neighbour,depth,limit)
                depth=depth-1
        depth=depth-1    

print("Following is the Depth-Limited Search")
dls(visited, graph, '5',0,3)
