class Solution:                                                               #The problem could be solved simply using bucket sort, but here is a much faster solution.
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        n=len(num)
        if n<2:
            return 0
        maxV=max(num)                                                         #Record the max value of the array.
        minV=min(num)                                                         #Record the min value of the array.
        
        bucketLen = max(1,int(0.5 + 1.0 * (maxV - minV) / (n - 1)))           #Then the maximum gap will be no smaller than ceiling[(maxV - minV) / (n - 1)]. Thus, let the larger value of it and 1 be the length of each bucket.
        bucketNum = (maxV-minV)/bucketLen+1                                   #Hence, the number of buckets could be calculated.
        buckets = [[] for i in xrange(bucketNum)]
        for item in num:
            index=(item-minV)/bucketLen                                       #Compute the index of bucket for each item.
            if buckets[index]==[]:                                            #If the bucket is empty, append the value of current item twice.
                buckets[index].append(item)                                   #The 1st one is the min value of the bucket.
                buckets[index].append(item)                                   #The 2nd one is the max value of the bucket.
            else:
                buckets[index][0]=min(buckets[index][0],item)                 #Maintain the min value of the bucket.
                buckets[index][1]=max(buckets[index][1],item)                 #Maintain the max value of the bucket.
        
        maxgap=0
        prev=buckets[0]                                                       #This represents the previous nonempty bucket.
        for i in range(1,bucketNum):
            if buckets[i]!=[]:                                                
                maxgap=max(buckets[i][0]-prev[1],maxgap)                      #If current bucket is not empty, maxgap equals to the larger value of itself and the difference between the min value of current bucket and the max value of previous nonempty bucket.
                prev=buckets[i]                                               #Maintain the previous nonempty bucket.
        return maxgap
