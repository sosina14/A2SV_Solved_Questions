class Solution:
    def customSortString(self, order: str, s: str) -> str:
        new = []
        arr = list(s)
        
        for i in order:
            count = arr.count(i)
            if count > 0:
                new.extend([i] * count)
                arr = [c for c in arr if c != i]
        
        new.extend(arr)
        return "".join(new)
