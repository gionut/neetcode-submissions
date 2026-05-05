class Solution:
    def findOrder(self, n: int, courses: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        prereq_cnt = [0] * n
        for c, prereq in courses:
            adj[prereq].append(c)
            prereq_cnt[c] += 1
        
        queue = deque([c for c in range(n) if prereq_cnt[c] == 0])
        result = []
        while queue:
            c = queue.popleft()
            result.append(c)
            for nxt in adj[c]:
                prereq_cnt[nxt] -= 1
                if prereq_cnt[nxt] == 0:
                    queue.append(nxt)
        
        return result if len(result) == n else []