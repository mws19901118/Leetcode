class StockSpanner:

    def __init__(self):
        self.stock = []                                   #Use list to store remaining stocks and its span.

    def next(self, price: int) -> int:
        span = 1                                          #When a new stock price comes in, the initial span is 1.
        while self.stock and self.stock[-1][0] <= price:  #While stock is not empty and the last stock's price is smaller than or equal to new stock price, pop the last stock price and add its span to current span.
            span += self.stock.pop()[1]                   #Because if next stocks price comes later and it's smaller than current one, its span is 1 and is not related to previous stock prices. 
                                                          #If it's larger than or equal to current one, we can directly add current span to the new span. 
                                                          #So, no need to keep stock price which are in later stock price's span in stock.
        self.stock.append((price, span))                  #Append current stock price and its span to stock.
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
