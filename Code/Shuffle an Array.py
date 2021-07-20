class Solution:

    def __init__(self, nums: List[int]):
        self.nums = deepcopy(nums)                                                  #Store nums.
        self.orignial = deepcopy(nums)                                              #Store an orignial copy of nums.
        
    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.orignial                                                        #Return the original copy.

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.nums)):                                             #Traverse nums.
            r = randint(i, len(self.nums) - 1)                                      #Generate a random int in [i, len(self.nums) - 1].
            self.nums[i], self.nums[r] = self.nums[r], self.nums[i]                 #Swap self.nums[i] and self.nums[r].
        return self.nums                                                            #Return self.nums.


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
