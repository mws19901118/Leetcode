class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True                                                                                                                 #When there are 2 piles: Alice can win obviously by taking the larger pile.
                                                                                                                                    #When there are 4 piles: If Alice takes the first pile initially, she can always take the third pile. If she takes the fourth pile initially, she can always take the second pile. Because total number of stones is odd, at least one of first + third, second + fourth is larger, so she can always win.
                                                                                                                                    #And so on, Alice can always win.
