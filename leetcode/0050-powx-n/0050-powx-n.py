class Solution:
    def myPow(self, x: float, n: int) -> float:
        def f(n):
            if n == 1:
                return x
            if n == 0:
                return 1

            sosi = f(n//2)

            if n%2:#0dd
                return sosi * sosi * x
            else:
                return sosi * sosi

        if n < 0:
            return 1/f(-n)

        return f(n)