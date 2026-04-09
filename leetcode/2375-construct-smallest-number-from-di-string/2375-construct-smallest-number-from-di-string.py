class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res , stack = [] , []
        
        for i in range(len(pattern)+1):
            stack.append(str(i+1))

            while stack and (i == len(pattern) or pattern[i] == "I"):
                res.append(stack.pop())
            

        return "".join(res)