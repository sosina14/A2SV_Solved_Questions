class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == "]":
                # removing the strings
                res = []
                while stack and stack[-1] != "[":
                    res.append(stack.pop())
                stack.pop()
                # removing the digits
                num = ""
                while stack and stack[-1].isdigit():
                    num += stack.pop()
                # merging
                num = int(num[::-1])
                stack.extend(res[::-1] * num)
            else:
                stack.append(ch)

        return "".join(stack)