class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evenSum = sum([x for x in nums if not x & 1])         #Sum up even numbers.
        result = []
        for v, i in queries:                                  #Traverse queires.
            if not nums[i] & 1:                               #If nums[i] is even, substract it from evenSum.
                evenSum -= nums[i]
            nums[i] += v                                      #Update nums[i].
            if not nums[i] & 1:                               #If nums[i] is even, add it to evenSum.
                evenSum += nums[i]
            result.append(evenSum)                            #Append evenSum to result.
        return result
