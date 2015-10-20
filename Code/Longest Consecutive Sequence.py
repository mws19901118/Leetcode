class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        if num==[]:
            return 0
        dict={}                                           #store the mapping between low and high boundary
        for i in num:
            if i in dict:                                 #do not process duplicates
                continue
            low=dict[i-1] if i-1 in dict else i
            high=dict[i+1] if i+1 in dict else i
            dict[i]=i
            dict[low]=high
            dict[high]=low
        return max(abs(key - value) + 1 for key, value in dict.iteritems())       #numbers within a consecutive sequence won't point out of the boundary
