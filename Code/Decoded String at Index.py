class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        currentLength = 0                                                                     #Store decoded string length.
        letters, digits = [""], [1]                                                           #Use stack to store repeated kernel letters and repeated times, initislly empty string and 1.
                                                                                              #Each kernel is in the format of AX + Y, X is inner kernel repeated A times while Y is only repeated once. 
                                                                                              #Only store Y part cause inner kernel X is stored in previous element in stack. 
        for c in S:                                                                           #Traverse through S.
            if c.isalpha():                                                                   #If c is letter, increase current length.
                currentLength += 1
                if currentLength == K:                                                        #If current length is K, directly return c.
                    return c
                if digits[-1] == 1:                                                           #If previous kernel repeated times is 1, append c to it.
                    letters[-1] += c
                else:                                                                         #Otherwise, add c to letters and its repeated times is 1.
                    letters.append(c)
                    digits.append(1)
            else:
                num = int(c)                                                                  #If c is digit, convert it to int.
                digits[-1] *= num                                                             #Multiply digits[-1] and current length by num.
                currentLength *= num
                if currentLength >= K:                                                        #If current length is larger than or equal to K, 
                    currentLength //= digits[-1]                                              #Shrink current length to current kernel length.
                    digits.pop()                                                              #Pop digits.
                    K = (K - 1) % currentLength + 1                                           #Update index K to be the target index in kernel.
                    while letters and K + len(letters[-1]) <= currentLength:                  #If K is not in the Y part of current kernel.
                        currentLength = (currentLength - len(letters[-1])) // digits[-1]      #Shrink length to inner kernel X for next iteration.
                        digits.pop()                                                          #Pop digits.
                        letters.pop()                                                         #Pop letters.
                        K = (K - 1) % currentLength + 1                                       #Update index K to be the target index in inner kernel.
                    return letters[-1][(K - 1) % currentLength - currentLength]               #Return the value on target index in Y.
                    
