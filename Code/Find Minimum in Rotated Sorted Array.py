class Solution:
# @param num, a list of integer
# @return an integer
def findMin(self, num):
    if(len(num)==1):return num[0];
    else:
        start=0;
        end=len(num)-1;            
        min=num[start];

        while(start<=end):                                                    #Binary search
            middle=int((end+start)/2);
            if(num[middle]>=min):
                start=middle+1;
            else:
                if(num[middle]<min):
                    min=num[middle];
                end=middle;
        return min;
