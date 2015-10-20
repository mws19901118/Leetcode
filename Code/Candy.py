class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        n=len(ratings)
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            candy=[1]*n
            i=1
            while i<n:                                    #forward traverse
                if ratings[i]>ratings[i-1]:
                    candy[i]=candy[i-1]+1
                i+=1
            i=n-2
            while i>=0:                                   #reverse traverse
                if ratings[i]>ratings[i+1] and candy[i]<=candy[i+1]:
                    candy[i]=candy[i+1]+1
                i-=1
            sum=0
            for i in range(len(candy)):
                sum+=candy[i]
            return sum
