class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr = [0]*(len(s)+1)
        for l, r, shift in shifts:
            if shift == 0:
                arr[l] -= 1
                arr[r+1] += 1
            else:
                arr[l] += 1
                arr[r+1] -= 1
        for i in range(1, len(arr)):
            arr[i] += arr[i - 1]           

        result = []
        for i in range(len(s)):
            x  = ((ord(s[i]) - ord('a')) + arr[i]) % 26 + ord("a")
            result.append(chr(x))

        return "".join(result)
        

