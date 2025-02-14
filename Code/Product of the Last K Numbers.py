class ProductOfNumbers:

    def __init__(self):
        self.product = [1]                                                                                          #Initialize product.
        self.size = 0                                                                                               #Initialize current index.
        self.last_zero_index = -1                                                                                   #Initialize the last index of 0.

    def add(self, num: int) -> None:
        if not num:                                                                                                 #If num is 0, update last_zero_index and append 1 to product to "reset".
            self.last_zero_index = self.size
            self.product.append(1)
        else:                                                                                                       #Othwise, append product[-1] * num to product to update prefix product.
            self.product.append(self.product[-1] * num)
        self.size += 1                                                                                              #Increase size.

    def getProduct(self, k: int) -> int:
        return 0 if self.last_zero_index >= self.size - k else self.product[-1] // self.product[-(k + 1)]           #If last_zero_index >= size - k, 0 is included in last k numbers so return 0; otherwise, calculate the product using prefix product and return.


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
