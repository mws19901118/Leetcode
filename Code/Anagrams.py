class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        dict={}
        result=[]
        for s in strs:
            key=''.join(sorted(s))            #Sort every string to a list of characters and join them together.
            if key not in dict:               #The value of dict is a list to record the strings which are the same anagrams.
                dict[key]=[s]
            else:
                dict[key].append(s)
        
        for i in dict.values():
            if len(i)>1:                      #If the length of value is larger than 1, there are a group of strings forming an anagrams, and append them to result.
                result+=i
        
        return result
