class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        p = [0 for i in range(len(num1) + len(num2))]                                                   #The length of product is at most the sum of nums1 length and num2 length.
        for i, j in product(range(len(num1)), range(len(num2))):                                        #Traver num1 and num2.
            p[-1 - i - j] += (ord(num1[-1 - i]) - ord('0')) * (ord(num2[-1 - j]) - ord('0'))            #Calculate the sum at each digit.
        
        carry=0                                                                                         #Initialize carry.
        for i in range(len(num1) + len(num2)):                                                          #Traverse p.
            carry, p[-1 - i]= divmod(p[-1 - i] + carry, 10)                                             #Update the digit at current index and carry.
            
        result="".join([str(x) for x in p]).lstrip('0')                                                 #Covert each digit to string and join them together then remove all leading 0.
        return "0" if not result else result                                                            #If result is empty string, return "0"; otherwise, return result.
