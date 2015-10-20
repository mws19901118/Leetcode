class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        def Scramble(s1,s2,dict):
            if dict.has_key((s1,s2)):
                return dict[(s1,s2)]
            else:
                if s1==s2:                      #If s1 equals to s2, they are obviously scramble.
                    dict[(s1,s2)]=True
                    return True
                else:
                    n=len(s1)
                    for i in range(1,n):        #Enum all the split points.
                        if (Scramble(s1[:i], s2[:i], dict) and Scramble(s1[i:], s2[i:], dict)) or (Scramble(s1[:i], s2[-i:], dict) and Scramble(s1[i:], s2[:-i], dict)):
                            dict[(s1,s2)]=True  #The first part is to determine if current string is consist of several scramble substrings, while the second part is to determine if current string is scramble.
                            return True
                    dict[(s1,s2)]=False
                    return False
        dict={}                                 #Dict to store intermediate results.
        return Scramble(s1, s2, dict)
