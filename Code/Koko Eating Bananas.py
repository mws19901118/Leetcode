class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1, max(piles)                                #Binary search from 1 to the max number in piles.
        while start < end:
            mid = (start + end) // 2
            total = sum(math.ceil(p / mid) for p in piles)        #Calculate the hours to eat all bananas at the speed of mid.
            if total > h:                                         #If it's greater than h, Koko has to eat faster, so set start to mid + 1.
                start = mid + 1
            else:                                                 #Otherwise, set end to mid.
                end = mid
        return end                                                #Return end after binary search stops.
