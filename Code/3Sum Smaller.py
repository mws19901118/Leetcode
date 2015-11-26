class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()                                               #Because we don't have to consider the duplicate of value, we can sort the list first. 
        l = len(nums)
        answer = 0
        for i in range(l - 2):                                    #The first index is between 0 and l - 3.
            start = i + 1                                         #The second index starts at i + 1.
            end = l - 1                                           #The third index ends at l - 1.
            while start < end:                                    #While start is smaller than end, find tuple from 2 sides to center.
                tsum = nums[i] + nums[start] + nums[end]          #Compute the temporary sum.
                while start < end and tsum >= target:             #While it is not smaller than target, move end backward.
                    end -= 1
                    tsum = nums[i] + nums[start] + nums[end]
                if start >= end:                                  #If start is equal to or larger than end, jump out of the loop.
                    break
                answer += end - start                             #Get a possible end range for fixed i and start, add the length to answer.
                start += 1                                        #Move start forward.
        return answer
