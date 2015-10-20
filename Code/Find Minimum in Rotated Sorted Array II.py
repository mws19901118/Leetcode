class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        if(len(num)==1):
            return num[0];
        else:
            start=0;
            end=len(num)-1;
            while(start<end and num[start]>=num[end]): #Binary search
                middle=int((end+start)/2);
                if(num[middle]>num[start]):
                    start=middle+1
                elif(num[middle]<num[start]):
                    end=middle
                else:                                 #Can not discard either branch. Thus, it goes O(n) in such case.
                    start=start+1
            return num[start];
