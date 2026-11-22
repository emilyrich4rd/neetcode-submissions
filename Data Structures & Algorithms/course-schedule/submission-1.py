class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for p in prerequisites:
            if adj.get(p[0]) is None:
                adj[p[0]] = [p[1]]
            else:
                adj[p[0]].append(p[1])
        print(adj)
        visited = set()
        in_progress = set()

        def cycle(node):
            if node in in_progress:
                return True 
            if node in visited:
                return False 

            in_progress.add(node)
            for neighbour in adj.get(node, []):
                if cycle(neighbour):
                    return True 

            in_progress.remove(node)
            visited.add(node)
            return False 
        
        for n in range(numCourses):
            if n not in visited:
                res = cycle(n)
                if res:
                    return False 
        return True 

        