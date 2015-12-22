class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        l = len(citations)
        if l == 0:
            return 0
        if citations[0] >= l:                                             #Rule out the case that all the citations are no smaller than the length of citations.
            return l
        if citations[-1] == 0:                                            #Rule out the case that all the citations are 0(The only case that h-index is 0).
            return 0
        start = 1
        end = l
        while start <= end:                                               #Binary search for h-index from 1 to l.
            mid = (start + end) / 2
            if citations[-mid] >= mid and citations[-(mid + 1)] <= mid:
                return mid
            elif citations[-mid] < mid:
                end = mid - 1
            else:
                start = mid + 1
