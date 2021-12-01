class Solution:
    def rob(self, nums: List[int]) -> int:
        rob, norob = 0, 0                                       #Initialize the max monmey to rob or not rob.
        for x in nums:                                          #Traverse nums.
            rob, norob = norob + x, max(rob, norob)             #If rob, new max money is previous not rob max money plus the money robbed from this house; if not rob, new max money is the greater value of previous not rob max money and rob max money.
        return max(rob, norob)                                  #Return the greater value of rob and norob.
