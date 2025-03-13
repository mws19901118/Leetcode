class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        index, effect = 0, 0                                  #Initialize index and the effect of qieroes[:index + 1] on current number.
        delta = [0] * (len(nums) + 1)                         #Initialize the delta of effect at each number.
        for i, x in enumerate(nums):                          #Traverse nums.
            effect += delta[i]                                #Add delta[i] to effect.
            while effect < x and index < len(queries):        #Iterate while effect smaller than x and index hasn't reaches the end.
                l, r, v = queries[index]                      #Get the l, r and val for current query.
                if l > i:                                     #If l is greater than i, increase v to delta[i] for future use.
                    delta[l] += v
                elif r >= i:                                  #Otherwise, if r is greater than or equal to i, add v to effect because current query will have effect on current number.
                    effect += v
                delta[r + 1] -= v                             #Decrease v from delta[r + 1] as the end of query.
                index += 1                                    #Move to next query.
            if effect < x:                                    #If effect is still smaller than x, index has reached the end of queries, so return -1 meaning current number cannot be reduced to 0.
                return -1
        return index                                          #Return index.
