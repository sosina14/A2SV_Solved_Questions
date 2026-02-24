class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        
        i =0
        j = len(skill)-1

        x =  skill[i] + skill[j]
        
        pro = 0
        while i < j:
            if x !=  skill[i] + skill[j]:
                   return -1
            mul = skill[i] * skill[j]
            pro += mul
            i += 1
            j -= 1
        
        return pro
