class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        l=len(s)
        dict={}                               #Record the number of occurence of each sequence.
        result=[]
        for i in range(l-9):
            temp=s[i:i+10]
            if dict.has_key(temp):
                dict[temp]+=1                 #Count the occurence.
                if dict[temp]==2:             #If the number of occurence is greanter than 1, append the sequence to result.
                    result.append(temp)
            else:
                dict[temp]=1
        return result
