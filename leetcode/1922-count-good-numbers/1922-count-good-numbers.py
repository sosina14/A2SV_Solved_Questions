class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        def f(n):
            if n == 1:
                return 5
            if n == 2:
                return 20
            

            if n%2:#0dd

                sosi = f(n//2)

                if (n//2)%2:#odd
                    return (sosi * 4 * sosi)%mod
                else:
                    return (sosi * 5 * sosi)%mod

            else:#even

                if (n//2)%2:#odd
                
                    sosi = f((n//2) -1)
        
                    return (sosi * 20 * sosi) %mod

                else:

                    sosi = f(n//2)

                    return (sosi * sosi) %mod

        return f(n)