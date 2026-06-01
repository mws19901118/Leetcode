class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse = True)                                                    #Sort cost in descending order.
        return sum(x for i, x in enumerate(cost) if i % 3 in [0, 1])                 #Buy every two and take the third one for free.
