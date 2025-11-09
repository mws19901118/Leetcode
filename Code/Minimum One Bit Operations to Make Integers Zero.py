class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if not n:                                                      #If n is 0, return 0 as it is already 0.
            return 0

        @cache                                                         #Cache result.
        def dp(s: str) -> int:                                         #Calculate the opeartions required to convert binary string s, whose leftmost bit need to be changed, to 0.
            if len(s) == 1:                                            #If s only has 1 bit, return 1.
                return 1
            count = 1 + 1 << (len(s) - 1) - 1                          #To change the leftmost bit, the pre-requisite is the rest bits form a power of 2. Then it needs 1 operation to change the leftmost bit and 1 << (len(s) - 1) - 1 operations to change the rest bits to 0.
            if s[1] == '1':                                            #If s[1] is 1, we just need to find the next non 0 bit.
                i = 2
                while i < len(s) and s[i] == '0':
                    i += 1
                if i < len(s):                                         #If there is such bit, add dp(s[i:]) to count to fulfil the pre-requisite.
                    count += dp(s[i:])
            else:                                                      #Otherwise, add dp(s[1:]) because s[1] need to be changed as well.
                count += dp(s[1:])
            return count

        return dp("{0:b}".format(n))                                   #Return dp result of the binary string of n.
