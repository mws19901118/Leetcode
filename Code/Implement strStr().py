class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        l=len(haystack)
        n=len(needle)
        for i in range(l-n+1):            #The last possible index is l-n.
            if needle==haystack[i:i+n]:
                return i
        return -1
