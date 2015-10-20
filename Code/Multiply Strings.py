class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):                                                                 #The problem could be solved by 'return str(int(num1)*int(num2))'， but it is meant to use large integer multiplication.
        l1=len(num1)
        l2=len(num2)
        product=[0 for i in range(l1+l2)]                                                           #The length of product is at most the sum of l1 and l2.
        for i in range(l1):
            for j in range(l2):
                product[l1+l2-1-i-j]+=(ord(num1[l1-1-i])-ord('0'))*(ord(num2[l2-1-j])-ord('0'))     #Calculate the sum in each digit.
        
        carry=0
        for i in range(l1+l2):
            newcarry=(product[l1+l2-1-i]+carry)/10                                                  #Calculate new carry.
            product[l1+l2-1-i]=(product[l1+l2-1-i]+carry)%10                                        #Calculate the number in each digit.
            carry=newcarry                                                                          #Update carry.
            
        result=""
        i=0
        while i<l1+l2 and product[i]==0:                                                            #Deal with beginning 0s.
            i+=1
        if i==l1+l2:                                                                                #If the product is 0, return "0".
            return "0"
        while i<l1+l2:                                                                              #Convert the product integer array to string.
            result+=str(product[i])
            i+=1
    
        return result
