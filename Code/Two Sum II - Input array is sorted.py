class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1                  #Initialize 2 pointers.
        while i < j:
            if numbers[i] + numbers[j] == target:   #If the sum of values of 2 pointers equals target, return one plus the indexes of the 2 pointers.
                return [i + 1, j + 1]
            elif numbers[i] + numbers[j] > target:  #If the sum is grater than target, the pointer from the end move backward.
                j -= 1
            else:                                   #If the sum is less than target, the pointer from the beginning move forward.
                i += 1
