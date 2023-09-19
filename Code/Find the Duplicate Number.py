class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = nums[0]            #https://en.wikipedia.org/wiki/Cycle_detection#Tortoise_and_hare
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return fast
