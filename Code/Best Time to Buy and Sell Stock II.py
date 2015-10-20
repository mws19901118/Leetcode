class Solution:
    # @param prices, a list of integer
    # @return an integer
        sum=0
        i=0
        while i<length-1:
            while i<length-1 and prices[i]>=prices[i+1]:              #search for the nadir
                i+=1
            low=prices[i]
            while i<length-1 and prices[i]<prices[i+1]:               #search for the peak
                i+=1
            high=prices[i]
            sum+=high-low
        return sum
