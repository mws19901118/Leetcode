class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        w=s.split(" ")                    #Split the string.
        n=len(w)
        for i in range(n):                #Traverse backward from the end.
            if len(w[n-1-i])!=0:          #If length of current word is not 0, return the length.
                return len(w[n-1-i])
        return 0                          #Return 0 if no words exit.
