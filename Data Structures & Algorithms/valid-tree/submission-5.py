class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        stack = []

        if len(edges) != n-1:
            return False

        adj = defaultdict(list)
        nodeSet = set()
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])

        def dfs(parent, node):
            visited[node] = 1
            for neighbour in adj[node]:
                if visited.get(neighbour) is None:
                    dfs(node, neighbour)
                elif neighbour != parent:
                    return False 
            return True 

        visited = {}
        res = dfs(-1, 0)
        if len(visited) < n or not res:
            return False 
        else:
            return True
                    


