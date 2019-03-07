class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()                                                 #Sort nums first.
        result = [[-1, -1, -1]]                                     #Create a dummy head for results.
        i = 0
        while i < len(nums) - 2 and nums[i] <= 0:                   #Check every possible index of the 1st number.
            start = i + 1                                           #Use 2 pointers, start and end, to go through from 2 sides to middle.
            end = len(nums) - 1
            while start < end:
                s = nums[i] + nums[start] + nums[end]               #Calculate the temporary sum.
                if s == 0:                                          #If temporary sum is 0, add a list of 3 numbers to result if it's not equal to the last list in result.
                    t = [nums[i], nums[start], nums[end]] 
                    if t != result[-1]:
                        result.append(t)
                    start += 1                                      #Move start forward.
                    end -= 1                                        #Move end backward.
                elif s > 0:                                         #If temporary sum is greater than 0, move end backward.
                    end -= 1
                else:                                               #If temporary sum is smaller than 0, move start forward.
                    start += 1
            j = i
            while j < len(nums) and nums[j] == nums[i]:             #Go to the next unique value of i.
                j += 1
            i = j
        return result[1:]                                           #Return result exclude dummy head.
