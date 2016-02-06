class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = '(' + s + ')'                                                       #Add parentheses outside s.
        def cal_right_parentheses(s, i):                                        #Calculate the value inside current parentheses.
            num = 0                                                             #Store current number, which hasn't been calculated.
            res = 0                                                             #Store current result.
            op = '+'                                                            #Default operator is plus.
            calculation = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}    #Use lambda function to represent plus and minus.
            
            while i < len(s):                                                   #Traverse through s.
                if s[i] in '+-':                                                #If encounters '+' or '-', calculate res and num with previous operator.
                    res = calculation[op](res, num)
                    num = 0                                                     #Reset num to 0.
                    op = s[i]                                                   #Set operator to current one.
                elif s[i] in '0123456789':                                      #If encounters digits, update num.
                    num = num * 10 + int(s[i])
                elif s[i] == '(':                                               #If encounters left parenthesis, recursively calculate the value inside current parentheses.
                    num,i = cal_right_parentheses(s, i + 1)
                elif s[i] == ')':                                               #If encounters right parenthesis, calculate res and num with previous operator.
                    res = calculation[op](res, num)
                    num = 0                                                     #Reset num to 0.
                    return res, i                                               #Return res and current index.
                i += 1
            res = calculation[op](res, num)                                     #Calculate res and num with previous operator.
            return res, i                                                       #Return res and current index.
        return cal_right_parentheses(s, 0)[0]
