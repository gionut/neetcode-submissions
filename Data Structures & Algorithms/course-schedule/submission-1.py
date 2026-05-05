class Solution:
    def canFinish(self, n: int, courses: List[List[int]]) -> bool:
        adj = defaultdict(list)
        in_deg = {i: 0 for i in range(n)}

        for s, e in courses:
            adj[s].append(e)
            in_deg[e] += 1
        
        queue = deque([node for node, cnt in in_deg.items() if cnt == 0])
        
        processed_cnt = 0
        while queue:
            node = queue.popleft()
            processed_cnt += 1
            for neighbour in adj[node]:
                in_deg[neighbour] -= 1
                if in_deg[neighbour] == 0:
                    queue.append(neighbour)
        
        return processed_cnt == n