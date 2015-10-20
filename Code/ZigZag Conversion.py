class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if numRows==1:                            #If there is only one row, we don't have to convert.
            return s
        l=len(s)
        section=(numRows-1)*2                     #The length of each zigzag section is (numRows-1)*2
        n=l/section                               #Calculate the number of full section.
        answer=''
        for i in range(n):                        #Deal with the first row, which has only 1 character in each section.
            answer+=s[i*section]
        if n*section<l:                           #Check if there is another character in the remain section.
            answer+=s[n*section]
        for j in range(1,numRows-1):
            for i in range(n):                    #Deal with the mid rows, which has 2 characters in each section.
                answer+=s[i*section+j]            #Deal with the first character.
                answer+=s[i*section+section-j]    #Deal with the second character.
            if n*section+j<l:                     #Check if there is another character in the remain section.
                answer+=s[n*section+j]
            if n*section+section-j<l:             #Check if there is another character in the remain section.
                answer+=s[n*section+section-j]
        for i in range(n):                        #Deal with the last row, which has only 1 character in each section.
            answer+=s[i*section+numRows-1]
        if n*section+numRows-1<l:                 #Check if there is another character in the remain section.
            answer+=s[n*section+numRows-1]
        return answer
