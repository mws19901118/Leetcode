class MinStack:
    def __init__(self):                                     //Initialize.
        self.valstack=[]
        self.minstack=[]
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.valstack.append(x)
        if len(self.minstack)==0 or x<=self.minstack[-1]:   //If minstack is empty or x<=current min, push x into minstack.
            self.minstack.append(x)

    # @return nothing
    def pop(self):
        if self.valstack[-1]==self.minstack[-1]:
           self. minstack.pop()
        self.valstack.pop()

    # @return an integer
    def top(self):
        return self.valstack[-1]

    # @return an integer
    def getMin(self):
        return self.minstack[-1]
