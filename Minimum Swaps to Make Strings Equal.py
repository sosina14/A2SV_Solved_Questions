class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        a = b = 0
        for i in range(len(s1)):
            if s1[i] == 'x' and s2[i] == 'y':
                a += 1
            elif s1[i] == 'y' and s2[i] == 'x':
                b += 1

        if (a + b) % 2 != 0:
            return -1

        if a % 2 != 0 or b % 2 != 0:
            return (a//2) + (b//2) + 2
        else:
            return (a//2) + (b//2)




       

        # s1 = list(s1)
        # s2 = list(s2)

        # count = 0
        
        # for i in range(len(s1)-1):
        #     if str(s1) != str(s2): 
        #         s1[i],s2[i+1] = s2[i+1],s1[i]
        #         count += 1
        #     if str(s1) != str(s2): 
        #         s1[i],s2[i] = s2[i],s1[i]
        #         count += 1
        #     else:
        #         break

        # if str(s1) == str(s2): 
        #     return count
    
        # return -1
        
