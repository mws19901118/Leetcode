class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        digits = list(num)                        #Split num.
        i = 0
        while i < len(digits) - 1 and k > 0:      #Traverse the list from beginning while k > 0.
            if digits[i] > digits[i + 1]:         #If current digit is larger than next digit, remove current digit.
                digits.pop(i)
                i = max(0, i - 1)                 #Back current digit if it's not the begnning.
                k -= 1                            #Decrease k.
            else:
                i += 1
        for i in range(k):                        #Now, digits list is in non-descending order, remove remaning k digits from behind.
            digits.pop()
        while digits and digits[0] == "0":        #Handle leading 0.
            digits.pop(0)
        if not digits:                            #If digits is empty, add a "0".
            digits = ["0"]
        return "".join(digits)                    #Join digits and return.
