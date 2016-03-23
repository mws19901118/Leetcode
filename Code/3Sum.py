class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()                                                 #Sort nums first.
        s = set()                                                   #Use set to rule out duplicate tuples.
        for i in range(len(nums) - 2):                              #Check every possible index of the 1st number.
            start = i + 1                                           #Use 2 pointers, start and end, to go through from 2 sides to middle.
            end = len(nums) - 1
            while start < end:
                t = nums[i] + nums[start] + nums[end]               #Calculate the temporary sum.
                if t == 0:                                          #If t is 0, add a tuple to s.
                    s.add((nums[i], nums[start], nums[end]))
                    start += 1                                      #Move start forward.
                    end -= 1                                        #Move end backward.
                elif t > 0:                                         #If t is greater than 0, move end backward.
                    end -= 1
                else:                                               #If t is smaller than 0, move start forward.
                    start += 1
        result = []
        for t in s:                                                 #Convert tuple to list and store them in a list.
            result.append([t[0], t[1], t[2]])
        return result
