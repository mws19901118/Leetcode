class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        def max1profit(prices):
          length=len(prices)
          if length==0 or length==1:
              return 0
          maxprofit=0
          lowprice=prices[0]
          for i in range(length):
              lowprice=min(lowprice,prices[i]) #maintain the lowest price
              maxprofit=max(prices[i]-lowprice,maxprofit) #if current profit>maxprofit, set maxprofit to current profit
          return maxprofit
        
        length=len(prices)
        if length==0 or length==1:
            return 0
        maxp=0
        for i in range(length):
            if i==length-1 or (i>0 and i<length-1 and prices[i]>=prices[i+1] and prices[i]>prices[i-1]):      #break the list into 2 parts at the peaks or the end
                temp1=max1profit(prices[:i+1])                                                                #calculate the former part max profit
                temp2=max1profit(prices[i:])                                                                  #calculate the latter part max profit
                if temp1+temp2>maxp:                                                                          #dynamic programming for total max profit
                    maxp=temp1+temp2
        return maxp
