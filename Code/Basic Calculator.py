class Solution:
    def evalRPN(self, tokens):                                                          #Calculate reverse polish notation(Problem NO.150).
        if len(tokens)==1:
            return int(tokens[0])
        stack=[tokens[0],tokens[1]]
        i=2
        while i<len(tokens):
            if tokens[i]=='+' or tokens[i]=='-' or tokens[i]=='*' or tokens[i]=='/':
                a=stack.pop()
                b=stack.pop()
                if tokens[i]=='/':
                    stack.append(str(int(float(b)/int(a))))
                else:
                    b=b+tokens[i]
                    b=b+a
                    stack.append(str(int(eval(b))))
            else:
                stack.append(tokens[i])
            i=i+1
        return int(stack.pop())
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        l=len(s)
        RPN=[]                                                                                                          #Record the reverse polish notation.
        stack=[]                                                                                                        #Store the stack of operations.
        priority={'+':1,'-':1,'*':2,'/':2}                                                                              #Store the priorities of operations.
        i=0
        while i<l:                                                                                                      #Convert simple expression to reverse polish notation.
            if ord(s[i])>=48 and ord(s[i])<=57:                                                                         #If s[i] is number, obtain the integer begenning with it and append the string form of integer to RPN.
                j=i
                while  j<l and ord(s[j])>=48 and ord(s[j])<=57:
                    j+=1
                RPN.append(s[i:j])
                i=j
            elif s[i]=='(':                                                                                             #If s[i] is '(', append it to stack.
                stack.append(s[i])
                i+=1
            elif s[i]==')':                                                                                             #If s[i] is ')', append the operaters poped from stack to RPN until the operater is '('.
                while True:
                    op=stack.pop()
                    if op=='(':
                        break
                    else:
                        RPN.append(op)
                i+=1
            elif s[i]=='+' or s[i]=='-' or s[i]=='*' or s[i]=='/':                                                      #If s[i] is '+', '-', '*' or '/', append the operaters poped from stack to RPN until stack is empty of the last element is '(' or the priority of last element is smaller than the priority of s[i].
                while 1:
                    if stack==[] or stack[len(stack)-1]=='(' or priority[stack[len(stack)-1]]<priority[s[i]]:
                        break
                    else:
                        RPN.append(stack.pop())
                stack.append(s[i])
                i+=1
            else:                                                                                                       #Ignore blanks.
                i+=1
        while stack!=[]:                                                                                                #After traverse through the experssion string, if the stack is not empty, append the operaters poped from stack until stack is empty.
            RPN.append(stack.pop())
        return self.evalRPN(RPN)                                                                                        #Return the value of RPN.
