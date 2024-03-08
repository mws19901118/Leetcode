class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)                            #Count each element.
        count_count = Counter(count.values())            #Count the count of each element.
        max_count = max(count.values())                  #Find the max of count.
        return max_count * count_count[max_count]        #Return total number of elements with max count.
