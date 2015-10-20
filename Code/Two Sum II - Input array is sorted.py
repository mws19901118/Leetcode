class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(numbers)
        i = 0                                       #Pointer from the beginning.
        j = l - 1                                   #Pointer from the end.
        while i < j:
            if numbers[i] + numbers[j] == target:   #If the sum of values of 2 pointers equals target, return one plus the indexes of the 2 pointers.
                return [i + 1, j + 1]
            elif numbers[i] + numbers[j] > target:  #If the sum is grater than target, the pointer from the end move backward.
                j -= 1
            else:                                   #If the sum is less than target, the pointer from the beginning move forward.
                i += 1
