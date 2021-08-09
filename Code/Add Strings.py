class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        split1, split2 = list(num1)[::-1], list(num2)[::-1]     #Split then reverse num1 and num2.
        sumArray, carry = [], 0                                 #Initalize sum array to be empty and carry to be 0.
        for x, y in zip(split1, split2):                        #Traverse split1 and split2 when both are valid.
            s = int(x) + int(y) + carry                         #Simulate sum and append result to sumArray.
            sumArray.append(str(s % 10))
            carry = s // 10
        if len(sumArray) < len(split1):                         #If there are numbers remain in split1, keep simulating sum.
            l = len(sumArray)
            for x in split1[l:]:
                s = int(x) + carry
                sumArray.append(str(s % 10))
                carry = s // 10
        elif len(sumArray) < len(split2):                       #If there are numbers remain in split2, keep simulating sum.
            l = len(sumArray)
            for y in split2[l:]:
                s = int(y) + carry
                sumArray.append(str(s % 10))
                carry = s // 10
        if carry:                                               #If carry is 1, append "1" to sumArray.
            sumArray.append("1")
        return "".join(sumArray[::-1])                          #Reverse sumArray then join and return.
