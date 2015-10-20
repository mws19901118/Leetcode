class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        if len(tokens)==1:
            return int(tokens[0])
        stack=[tokens[0],tokens[1]]             #stack of tokens            
        i=2
        while i<len(tokens):
            if tokens[i]=='+' or tokens[i]=='-' or tokens[i]=='*' or tokens[i]=='/':
                a=stack.pop()                   #pop number a
                b=stack.pop()                   #pop number b
                if tokens[i]=='/':              #divide
                    stack.append(str(int(float(b)/int(a))))
                else:                           #other operators
                    b=b+tokens[i]
                    b=b+a
                    stack.append(str(int(eval(b))))     #calculate the value of an expression and push it back to the stack
            else:
                stack.append(tokens[i])         #push token
            i=i+1
        return int(stack.pop())
