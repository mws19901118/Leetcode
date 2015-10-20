class Solution:
    # @return an integer
    def numTrees(self, n):
        def numOfTrees(n,dict):
            if dict.has_key(n):
                return dict[n]
            else:
                sum=0
                for i in range(1,n+1):
                    sum=sum+numOfTrees(i-1,dict)*numOfTrees(n-i,dict)     #Current number of trees equals the sum of product of number of trees of left child multipled br that of right child when i(form 1 to n) is the root.
                dict[n]=sum
                return dict[n]
        
        dict={}                                                           #Dictionary to record exsited value.
        dict[0]=1
        dict[1]=1
        return numOfTrees(n, dict)
