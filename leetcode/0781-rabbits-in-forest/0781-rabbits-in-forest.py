class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        fre = Counter(answers)
        total = 0
        
        for k , v in fre.items():
            size = k + 1
            num = ceil(v/size)
            total += num * size

        return total