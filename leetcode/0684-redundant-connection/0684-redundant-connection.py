class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        rank = [1]*(len(edges)+1)

        def find(n):
            if n == parent[n]:
                return n
            return find(parent[n])

        def union(x,y):
            px = find(x)
            py = find(y)

            if px == py:
                return False
            if rank[px] > rank[py]:
                parent[py] = px
                rank[py] += 1
            else:
                parent[px] = py
                rank[px] += 1
            return True

        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]
