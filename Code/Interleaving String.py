class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):                                                                                #If the sun of s1 length and s2 length does not equal s3 length, directly return false.
            return False
        dp = [False for i in range(len(s2) + 1)]                                                                        #Initialize dp array.
        dp[0] = True                                                                                                    #dp[0] = 0, means "" is the interleaving string of "" and "".
        for i in range(len(s2)):                                                                                        #Compute if s3[:i] is the interleaving string of "" and s2[:i].
            dp[i + 1] = dp[i] and s2[i] == s3[i]
        for i in range(len(s1)):                                                                                        #Traverse s1.
            dp[0] = dp[0] and s1[i] == s3[i]                                                                            #Check if s3[:i] is the interleaving string of s1[:i] and "".
            for j in range(len(s2)):                                                                                    #Traverse s2.
                dp[j + 1] = (dp[j + 1] and s3[i + j + 1] == s1[i]) or (dp[j] and s3[i + j + 1] == s2[j])                #To make s3[:i + j + 1] the interleaving string of s1[:i] and s2[:j], it has to be either s3[i + j] is the interleaving string of s1[:i - 1] and s2[j] then s1[i] == s3[i + j + 1] or s3[i + j] is the interleaving string of s1[:i] and s2[j - 1] then s2[j] == s3[i + j + 1].
        return dp[-1]                                                                                                   #Return dp[-1]
