class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        n=len(s)
        if n<=1:                        #If the length of s is smaller than or equal to 1, there is no repeating characters.
            return n
        dict={}                         #Record the index of last appearance of a character. Initially, it's -1.
        for i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ ":
            dict[i]=-1
        i=0                             #The begin index of a substring.
        j=0                             #Traverse througn the string.
        l=1                             #Record the length of current longest substring without repeating characters.
        while j<n:
            if dict[s[j]]==-1:          #If it's the first appearance of a character, record the index.
                dict[s[j]]=j
            else:                       #If we encounter a repeating character, update l and dict[s[j]].
                if j-i>l:
                    l=j-i
                if dict[s[j]]+1>i:      #Begin the next substring at the character behind the last appearance of s[j] if it's greater than i.
                    i=dict[s[j]]+1
                dict[s[j]]=j
            j+=1
        if j-i>l:                       #Deal with the substring in the end of s.
            l=j-i
        return l
