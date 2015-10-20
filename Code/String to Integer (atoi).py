class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        l=len(str)
        i=0
        flag=False
        while i<l and str[i]==' ':                              #Deal with whitespaces in the beginning.
            i+=1
        if i<l and str[i]=='-':                                 #Deal with minus sign.
            flag=True
            i+=1
        elif i<l and str[i]=='+':                               #Deal with plus sign
            i+=1
        if i==l or ord(str[i])<48 or ord(str[i])>57:            #Deal with unconvertable situations.
            return 0
        else:
            j=i
            while j<l and ord(str[j])>=48 and ord(str[j])<=57:  #Calculate the length of integer.
                j+=1
            answer=0
            for k in range(i,j):
                answer+=(ord(str[k])-48)*10**(j-1-k)            #Convert.
            if flag:                                            #Deal with negative integer.
                answer=-answer                      
            if answer>2147483647:                               #Deal with out of range situations.
                return 2147483647
            if answer<-2147483648:
                return -2147483648
            return answer
