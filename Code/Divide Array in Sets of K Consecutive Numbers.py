class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:        #Same as 846 Hand of Straights.
        count = Counter(nums)
        values = sorted(count.keys())
        for x in values:
            if not count[x]:
                continue
            currentCount = count[x]
            for i in range(k):
                if count[x + i] < currentCount:
                    return False
                count[x + i] -= currentCount
        return True
