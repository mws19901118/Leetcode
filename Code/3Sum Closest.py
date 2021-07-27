class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()                                             #Sort the list.
        result = 100000                                         #Set the initial value of result to be a very large value.
        for i in range(len(nums)):                              #Traverse nums as the smallest of 3 integers. 
            start, end = i + 1, len(nums) - 1                   #Set the second integer to be the integer at i + 1 and thrid integer to be the integer at len(nums) - 1.
            while start < end:                                  #Iterate while start is smaller than end.
                sum3 = nums[i] + nums[start] + nums[end]        #Calculate the 3 sum.
                if abs(sum3 - target) < abs(result - target):   #If it's closer to target than current result, update result.
                    result = sum3
                if sum3 < target:                               #If it's smaller than target, move start forward because list is sorted.
                    start += 1
                elif sum3 > target:                             #If it's larger than target, move end backward because list is sorted.
                    end -= 1
                else:                                           #If it's target, directly return target.
                    return target
        return result
