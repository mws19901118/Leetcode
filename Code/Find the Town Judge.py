from collections import defaultdict
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        a, b = defaultdict(int), defaultdict(int)
        for x in trust:
            a[x[0]] += 1                            #Count the people each person trust.
            b[x[1]] += 1                            #Count the people each person is trusted by.
        for i in range(1, N + 1):
            if a[i] == 0 and b[i] == N - 1:         #If someone trust no one and is trusted by anyone else, that person is judge, so return label.
                return i
        return -1                                   #If not found judge, return -1.
