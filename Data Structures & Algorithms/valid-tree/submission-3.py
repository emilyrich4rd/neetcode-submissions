class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # no cycles and connected so no random bits , everything must be reachable 
        # therefore if neither dfs nor bfs covers all 5 nodes, it is not
        stack = []

        # make adj graph
        adj = defaultdict(list)
        nodeSet = set()
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])

        def dfs(parent, node):
            visited[node] = 1
            print(f"adj list {adj}")
            for neighbour in adj[node]:
                if visited.get(neighbour) is None:
                    dfs(node, neighbour)
                elif neighbour != parent:
                    return False 
            return True 

        visited = {}

        # we would only have to iterate through every node for an unconnected graph
        # but if it is unconnected, it is false anyway
        res = dfs(-1, 0)
        if len(visited) < n or not res:
            return False 
        else:
            return True
                    


