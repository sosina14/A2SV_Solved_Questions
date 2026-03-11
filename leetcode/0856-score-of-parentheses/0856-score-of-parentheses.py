class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for i in s:
            if i == "(":
                stack.append(0)
            else:
                val = stack.pop()
                if val == 0 :
                    val = 1
                else:
                    val *= 2
                stack[-1] += val
                
        return stack[0] 

