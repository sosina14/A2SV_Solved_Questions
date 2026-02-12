class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        freq1 = Counter(word1)
        freq2 = Counter(word2)

        list1 = []
        list2 = []
        char1 = []
        char2 = []

        for key , val in freq1.items():
            list1.append(val)
            char1.append(key)

        for key , val in freq2.items():
            list2.append(val)
            char2.append(key)
        

        return sorted(list1) == sorted(list2) and sorted(char1) == sorted(char2)
       
        

