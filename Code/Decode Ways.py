class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        n=len(s)
        if n==0:
            return 0
        num=[1]                                                 #Record the number of decode ways
        if int(s[0])!=0:                                        #If the first digit is 0, the number is 0; otherwise the number is 1.
            num.append(1)
        else:
            num.append(0)
        for i in range(1,n):                                    #Pass from the second digit to the end.
            temp=0
            if int(s[i])!=0:                                    #If current digit is not 0, add the number for string ended with previous digit to temp.
                temp+=num[-1]
            if int(s[i-1:i+1])>=10 and int(s[i-1:i+1])<=26:     #If current 2 digits is larger than or equal to 10 and smaller than or equal to 26, add the number for string ended with the digit before previous digit. 
                temp+=num[-2]
            num.append(temp)                                    #Append temp to the list.
        return num[-1]                                          #Return the last item of the list.
