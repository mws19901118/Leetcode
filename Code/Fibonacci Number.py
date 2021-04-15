class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        p2, p1 = 0, 1                 #Simple Fibonacci Number calculation.
        fn = -1
        for i in range(2, n + 1):
            fn = p2 + p1
            p2 = p1
            p1 = fn
        return fn
