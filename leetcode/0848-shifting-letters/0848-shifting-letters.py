class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        arr = []
        summ = 0
        x = 0
        for i in shifts:
            summ += i
            arr.append(summ)
        new = [summ]
        for i in range(len(arr)-1):
            x = summ - arr[i]
            new.append(x)

        result = []
        for i in range(len(s)):
            x  = ((ord(s[i]) - ord('a')) + new[i]) % 26 + ord("a")
            result.append(chr(x))

        return "".join(result)
   