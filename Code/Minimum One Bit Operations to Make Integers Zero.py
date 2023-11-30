class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if not n:                                                      #If n is 0, return 0 as it is already 0.
            return 0
        power_2_result = [0]                                           #Store the result for power of 2 which will be used frequently, initially value is 0.
        p = 1                                                          #Initialize power of 2 at 1.
        while p <= n:                                                  #Iterate while power of 2 is not greater than n.
            power_2_result.append(power_2_result[-1] * 2 + 1)          #For 2 ** x, we have to first convert the (x - 1) 0 after leftmost 1 to 2 ** (x - 1), next change the leftmost 1 to 0 then convert 2 ** (x - 1) back to 0. In total, power_2_result[x] is power_2_result[x - 1] * 2 + 1.
            p <<= 1                                                    #Multiply p by 2.

        binary = "{0:b}".format(n)                                     #Convert n to binary string.

        @cache                                                         #Cache result.
        def dp(s: str) -> int:                                         #Calculate the opeartions required to convert binary string s, whose leftmost bit need to be changed, to 0.
            if len(s) == 1:                                            #If s only has 1 bit, return 1.
                return 1
            count = 1 + power_2_result[len(s) - 1]                     #To change the leftmost bit, the pre-requisite is the rest bits form a power of 2. Then it needs 1 + power_2_result[len(s) - 1] to change s to 0.
            if s[1] == '1':                                            #If s[1] is 1, we just need to find the next non 0 bit.
                i = 2
                while i < len(s) and s[i] == '0':
                    i += 1
                if i < len(s):                                         #If there is such bit, add dp(s[i:]) to count to fulfil the pre-requisite.
                    count += dp(s[i:])
            else:                                                      #Otherwise, aadd dp(s[1:]) because s[1] need to be changed as well.
                count += dp(s[1:])
            return count

        return dp(binary)                                              #Return dp(binary).
