class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        @cache                                                                                  #Cache result.
        def dp(index: int) -> int:                                                              #Caculate the max differential one player can get against the other player in stoneValue[index:].
            if index >= len(stoneValue):                                                        #If index >= len(stoneValue), it reaches the end, so return 0.
                return 0
            result = stoneValue[index] - dp(index + 1)                                          #Initial result is the result of taking one pile minus the max diff of other player can get in the rest.
            if index + 1 < len(stoneValue):                                                     #If there are 2 piles left, try taking 2 piles and calculate the max differential and update if necessary.
                result = max(result, sum(stoneValue[index:index + 2]) - dp(index + 2))
            if index + 2 < len(stoneValue):                                                     #If there are 3 piles left, try taking 3 piles and calculate the max differential and update if necessary.
                result = max(result, sum(stoneValue[index:index + 3]) - dp(index + 3))
            return result                                                                       #Return result.

        diff = dp(0)                                                                            #Get the max differential Alice can get against Bob starting at 0.
        if diff > 0:                                                                            #Return the winner based on diff.
            return "Alice"
        elif diff < 0:
            return "Bob"
        else:
            return "Tie"
