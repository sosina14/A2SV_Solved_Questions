class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        summ = 0
        for i in words:
            arr = list(chars)
            c = 0
            for j in i:
                if j in arr:
                    c += 1
                    arr.remove(j)
            if c == len(i):
                summ += len(i)
        return summ

