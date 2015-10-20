class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        count={}
        for i in num:
            if count.has_key(i):
                count[i]=count[i]+1
            else:
                count[i]=1
            if count[i]>len(num)/2:
                return i
