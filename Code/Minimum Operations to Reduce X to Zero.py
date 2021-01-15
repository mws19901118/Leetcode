class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        positions = {0: 0}                                                    #The nums list can be divided to three consecutive parts, A, B and C(A, B and C can be empty).
        cumulativeSum = 0                                                     Finding minimum operations equals to find the min(len(A) + len(C)) which meets the condition that sum(A) + sum(C) = x.
        for i, n in enumerate(nums):
            cumulativeSum += n                                                #Calculate cumulative sum.
            positions[cumulativeSum] = i + 1                                  #Store cumulative sum in dict as key and value is index of position starting at 1.
        operations = len(nums) + 1                                            #Initialize minimum operations to be len(nums) + 1.
        s, i = 0, 0                                                           #initialize s to be cumulative sum and i to be the index of position from behind.
        while s <= x and i <= len(nums):                                      #Start traverse nums from behind until s > x or i > len(nums).
            gap = x - s                                                       #Get the gap between x and s.
            if gap in positions and positions[gap] - 1 <= len(nums) - i:      #If gap in positions and position[gap] hasn't reach i, i.e. A and C has no intersection, it's a valid case.
                operations = min(operations, positions[gap] + i)              #Update operations.
            i += 1                                                            #Increase i.
            s += nums[-min(i, len(nums))]                                     #Increase s if i is valid.
        operations = -1 if operations == len(nums) + 1 else operations        #Check if x can be reduced to 0; if not, set operations to -1.
        return operations                                                     #Return operations.
