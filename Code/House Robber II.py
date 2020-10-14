class Solution:
    def rob1(self, nums: List[int]) -> int:                                 #Find the max rob money for linear like House Robber I.
        rob, notrob = [0] * (len(nums) + 1), [0] * (len(nums) + 1)
        for i, x in enumerate(nums):
            rob[i + 1] = notrob[i] + x
            notrob[i + 1] = max(rob[i], notrob[i])
        return max(rob[-1], notrob[-1])
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.rob1(nums[1:]), self.rob1(nums[:-1]))      #To convert the loopy problem to linear problem, enumerate the situantion that we don't rob the first house and don't rob the last house, as they are adjacent in loop. Also check if there is only one house.
