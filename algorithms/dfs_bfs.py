class PathFinder:
    def __init__(self, graph_data):
        self.graph = graph_data

    def findPathsDFS(self, start_id, end_id, path=None):
        if path is None:
            path = [start_id]                
        if(start_id == end_id):            
            yield path                
        for child in self.graph[start_id]:
            if(child not in path):
                yield from self.findPathsDFS(child, end_id, path+[child])    

    def findPathsBFS(self, start_id, end_id):
        queue = [(start_id, [start_id])]
        while queue:
            vertex, path = queue.pop(0)
            if vertex == end_id:
                yield path
            else:
                for child in self.graph[vertex]:
                    if child not in path:
                        queue.append((child, path + [child]))
    
    def shortestPath(self, start_id, end_id):
        return next(self.findPathsBFS(start_id, end_id))


"""
   A
/  | \\
B__F  C
 \___/
"""
pf = PathFinder({'A': ['B', 'C', 'F'],
                 'B': ['F','A','C'],
                 'C': ['B','A'],
                 'F': ['B','A']
                 })
print(list(pf.findPathsDFS('A', 'B')))

"""
"""
pf2 = PathFinder({'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])})
print(list(pf2.findPathsBFS('A', 'F')))
print(pf2.shortestPath('A', 'F'))
print(list(pf2.findPathsBFS('A', 'C')))
print(pf2.shortestPath('A', 'C'))

