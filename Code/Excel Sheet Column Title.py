class Solution:
    # @return a string
    def convertToTitle(self, num):
        ans=''
        a=[0]
        for i in range(14):
            a.append((a[-1]+1)*26)                      #Generate the form of amount of column titles of which length is no longer than the value of corresponding index.  
        num=num-1                                       #Begin with 0, not 1.
        i=0
        while num>=a[i]:                                #Find the length of column title of current number.
            i=i+1
        i=i-1
        temp=0
        while i>=1:                                     #Deal with the situation when length is larger than 1(prevent index out of bounds).
            temp=(num-a[i])/(a[i]-a[i-1])               #Calculate the correspoding digit of character, which should be the answer of num divided by the amount of column titles of which length is exactly current length minus 1.
            ans=ans+chr(ord('A')+temp)                  #Transform between digit and ascii.
            num=num-(temp+1)*(a[i]-a[i-1])              #Iterate, let num be the remaining number.
            i=i-1                                       #Shorten to calculate the next character.
        ans=ans+chr(ord('A')+num)                       #Deal with the situation when length equals 1.
        return ans
