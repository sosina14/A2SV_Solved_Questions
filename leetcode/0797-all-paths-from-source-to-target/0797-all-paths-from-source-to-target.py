class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        
        def backtrack(cur_path, cur_node):
            if cur_node == len(graph)-1:
                res.append(list(cur_path))

            for x in graph[cur_node]:
                cur_path.append(x)
                backtrack(cur_path, x)
                cur_path.pop()

        backtrack([0],0)
        return res