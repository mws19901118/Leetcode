class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        carry, i = 0, len(num) - 1                                      #Initialize carry and index pointer.
        result = []                                                     #Initialize result.
        while k or i >= 0:                                              #Traverse while k is greater than 0 or i hasn't reached the beginning of num.
            current = carry + k % 10 + (num[i] if i >= 0 else 0)        #Calculate current sum.
            result.append(current % 10)                                 #Append last digit of current sum to result.
            carry = current // 10                                       #Calculate new carry.
            i -= 1                                                      #Decrease i.
            k //= 10                                                    #Move to next digit of k.
        if carry:                                                       #If carry is 1, add carry to result.
            result.append(carry)
        return result[::-1]                                             #Return the reversed result.
