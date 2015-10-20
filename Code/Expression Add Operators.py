class Solution(object):
    def addOperators(self, num, target):
        def isLeadingZeros(num):
            return num.startswith('00') or (int(num) == 0 and num.startswith('0'))  #Deal with the string with leading zeros.
        def solve(num, target, mulExpr = '', mulVal = 1):
            ans = []
            if isLeadingZeros(num):                                                 #remove leading zeros  
                pass
            elif int(num) * mulVal == target:
                ans.append(num + mulExpr)
            for x in range(len(num) - 1):                                           #Traverse from right to left.
                lnum = num[:x+1] 
                rnum = num[x+1:]
                if isLeadingZeros(rnum):                                            #remove leading zeros
                    continue
                right = rnum + mulExpr                                              #The whole right part expresstion.
                rightVal = int(rnum) * mulVal                                       #The whole right part value.
                for left in solve(lnum, target - rightVal):                         #op = '+'
                    ans.append(left + '+' + right)
                for left in solve(lnum, target + rightVal):                         #op = '-'
                    ans.append(left + '-' + right)
                for left in solve(lnum, target, '*' + right, rightVal):             #op = '*'
                    ans.append(left)
            return ans
        if not num:
            return []
        return solve(num, target)
        
