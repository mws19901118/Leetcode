class Solution:
    def isLeadingZeros(self, num: str) -> bool:                                                 #Determine if num is a string of number with leading zeros.
        return num.startswith('00') or (int(num) > 0 and num.startswith('0'))
    
    def dfs(self, num: str, target: int, mulExpr: str = '', mulVal: int = 1) -> List[str]:      #Find all expressions in num whose evaluation equals target with mulExpr and mulVal as the multiplication expression and value on the right side.
        result = []                                                                             #Initialize result list.
        if not self.isLeadingZeros(num) and int(num) * mulVal == target:                        #If num does not have leading 0 and num * mulVal == target, append (result + mulExpr) to result.
            result.append(num + mulExpr)
        for x in range(len(num) - 1):                                                           #Traverse from left to right.
            lnum, rnum = num[:x + 1], num[x + 1:]                                               #Split num to lnum and rnum.
            if self.isLeadingZeros(rnum):                                                       #If rnum has leading zeros, skip this split.
                continue
            rightExpr, rightVal = rnum + mulExpr, int(rnum) * mulVal                            #Get the expresstion and value of entire right part.
            for left in self.dfs(lnum, target - rightVal):                                      #Find all expressions in lnum whose evaluation equals to target - rightVal.
                result.append(left + '+' + rightExpr)                                           #Append '+' + rightExpr to each of them and append final result to result.
            for left in self.dfs(lnum, target + rightVal):                                      #Find all expressions in lnum whose evaluation equals to target + rightVal.
                result.append(left + '-' + rightExpr)                                           #Append '-' + rightExpr to each of them and append final result to result.
            for left in self.dfs(lnum, target, '*' + rightExpr, rightVal):                      #Find all expressions in lnum whose evaluation equals to target, with rightExpr and rightVal as the multiplication expression and value on the right side.
                result.append(left)                                                             #Append all of them to result.
        return result                                                                           #Return result.
        
    def addOperators(self, num: str, target: int) -> List[str]:
        return self.dfs(num, target)                                                            #Begin dfs.
