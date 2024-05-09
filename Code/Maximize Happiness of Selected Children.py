class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True)                                #Sort happiness in desending order.
        return sum(max(0, happiness[i] - i) for i in range(k))        #Add max(0, happiness[i] - i) for the top k largest happiness.
