class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        gap = sorted(x - y for x, y in zip(capacity, rocks))    #Sort each bag by gap to full capacity in asending order.
        i = 0
        while i < len(gap) and additionalRocks >= gap[i]:       #Traverse through bags and fill stones to bag until reaching the end or no more enought stones to fill a bag to full.
            additionalRocks -= gap[i]
            i += 1
        return i                                                #Return the max index of traverse.
