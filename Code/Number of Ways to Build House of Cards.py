class Solution:
    def houseOfCards(self, n: int) -> int:
        @cache                                                                #Cache result.
        def dp(cards: int, length: int) -> int:                               #DP to calculate the number of ways given cards and length of horizontal cards as foundation.
            if cards < 2:                                                     #If cards < 2, then can not form any house of cards, so return 0.
                return 0
            if cards == 2:                                                    #If cards == 2, it can only form one triangle on the left, so return 1.
                return 1
            result = 0
            next_length = 1                                                   #Initialize the horizontal cards we can form for next level.
            while 2 + 3 * next_length <= cards and next_length < length:      #For each horizontal card, it requires 3 more cards, also the max next_length is length - 1.
                remain = cards - (2 + 3 * next_length)                        #Calculate remain cards.
                result += dp(remain, next_length) if remain > 0 else 1        #If remain == 0, we have one way to use all cards on current level; otherwise, we can use remain cards on next level with next_length horizontal cards as foundation.
                next_length += 1
            return result
        return dp(n, inf)                                                     #Return the result of dp(n, inf).
