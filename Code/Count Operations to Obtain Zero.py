class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        larger, smaller = (num1 if num1 >= num2 else num2), (num2 if num1 >= num2 else num1)    #Find the larger and smaller number in num1 and num2.
        count = 0
        while smaller > 0:                                                                      #Iterate while smaller is greater than 0.
            count += larger // smaller                                                          #Add larger // smaller to count.
            larger, smaller = smaller, larger % smaller                                         #Set larget to smaller and smaller to larger % smaller.
        return count
