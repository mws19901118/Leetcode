class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        remain = time % (2 * n - 2)                                            #A round trip from start to end then back to start is 2 * (n - 1), so we only care about time % (2 * n - 2).
        return remain + 1 if remain <= n - 1 else 2 * n - remain - 1           #If remain <= n - 1, the pillow ends at remain + 1; otherwise, it ends at n - (remain - (n - 1)), which is 2 * n - 1 - remain.
