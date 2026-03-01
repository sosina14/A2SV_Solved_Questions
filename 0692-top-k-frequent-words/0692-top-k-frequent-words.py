class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = Counter(words)  
        arr = list(dic.keys())
        arr.sort(key=lambda x: (-dic[x], x))

        return arr[:k]