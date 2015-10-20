class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        n=len(strs)
        if n==0:                                          #If strs==[], return "".
            return ""
        l=len(strs[0])                                    #Get the possible prefixes from the first string.
        i=1
        result=""
        while i<=l:
            temp=strs[0][:i]                              #Get next possible prefix whose length is i.
            j=1
            while j<n:                                    #Traverse through other strings.
                if i>len(strs[j]) or strs[j][:i]!=temp:   #If length of current prefix is greater than length of strs[j] or current prefix is not a prefix of strs[j], break.
                    break
                j+=1
            if j==n:                                      #If j equals n, then current prefix is a common prefix.
                result=temp
                i+=1
            else:                                         #Otherwise, break.
                break
        return result
