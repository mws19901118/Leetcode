class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [1]                                       #Initialize products with a dummy product at the beginning.
        for x in nums:                                      #Traverse nums and calculate the product from the beginning to current number.
            product.append(product[-1] * x)
        rightProduct = 1                                    #Initialzie the product from right.
        for i in reversed(range(len(nums))):                #Traverse nums backward.
            product[i + 1] = product[i] * rightProduct      #The product except self at each index i equals to the product from beginning to index i - 1 multiply the product from right to index i + 1. 
            rightProduct *= nums[i]                         #Update rightProduct.
        return product[1:]                                  #Return product[1:] as the first product is dummy.
