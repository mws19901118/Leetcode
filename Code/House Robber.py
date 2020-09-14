class Solution:
    def rob(self, nums: List[int]) -> int:
        rob, notrob = [0] * (len(nums) + 1), [0] * (len(nums) + 1)      #Initialize the rob or not rob list to record the current max money robbed.
        for i, x in enumerate(nums):
            rob[i + 1] = notrob[i] + x                                  #If rob, new max money is previous not rob max money plus the money robbed from this house.
            notrob[i + 1] = max(rob[i], notrob[i])                      #If not rob, new max money is the greater value of previous not rob max money and rob max money.
        return max(rob[-1], notrob[-1])                                 #Return the greater value of rob[-1] and notrob[-1].
