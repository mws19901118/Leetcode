class Solution:
    def tribonacci(self, n: int) -> int:
        t0, t1, t2 = 0, 1, 1                      #Keep a sliding window of size 3.
        for x in range(n - 2):                    #Move forward window n - 2 times and keep updating numbers in window.
            t0, t1, t2 = t1, t2, t0 + t1 + t2
        return t2 if n > 0 else 0                 #Return t2 if n > 0, otherwise return 0 for t0. Ideally should check t1 if n == 1, but since t1 == t2, so this scenario is handled.
