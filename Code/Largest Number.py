class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        def mycmp(n1,n2):
            return int(str(n2)+str(n1))-int(str(n1)+str(n2))            #My compare function: if the value of "n1"+"n2" is greater than that of "n2"+"n1", n1 should be in front of n2; vice versa.
        num.sort(cmp=mycmp)                                             #Sort the array using my compare function.
        ans=""
        flag=False                                                      #It indicates that the numbers before current number are all 0 when it is false.
        for i in num:
            if flag==False and i!=0:
                flag=True
            if flag==True:                                              #If flag is true, convert current number to string and concatenate it with ans.
                ans+=str(i)
        if ans=="":                                                     #If all the numbers are 0, ans is an empty string, set it to "0"
            ans="0"
        return ans
