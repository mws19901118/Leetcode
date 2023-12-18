class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        largest, secondLargest, smallest, secondSmallest = -inf, -inf, inf, inf        #Initialize the largest, second largest, smallest and second smallest number.
        for x in nums:                                                                 #Traverse nums to find largest, second largest, smallest and second smallest number.
            if x > largest:
                secondLargest = largest
                largest = x
            elif x > secondLargest:
                secondLargest = x
            if x < smallest:
                secondSmallest = smallest
                smallest = x
            elif x < secondSmallest:
                secondSmallest = x
        return largest * secondLargest - smallest * secondSmallest                    #largest and second largest forms a pair and smallest and second smallest forms another pair. Return their product difference.
