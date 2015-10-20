class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.s1=[]                                    #Use stack s1 to store elements.
        self.s2=[]                                    #Use stack s2 as a backup when poping queue.

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.s1.append(x)

    # @return nothing
    def pop(self):
        while len(self.s1)>1:                         #Push the elements popped from s1 into s2, so the order of s2 is the reverse order of s1. 
            self.s2.append(self.s1[-1])
            self.s1.remove(self.s1[-1])
        self.s1.remove(self.s1[-1])                   #Delete the first element of s1, i.e. the first element of the queue.
        while len(self.s2)>0:                         #Push the elements popped from s2 into s1, recovering the normal order.
            self.s1.append(self.s2[-1])               
            self.s2.remove(self.s2[-1])

    # @return an integer
    def peek(self):
        if self.s1==[]:
            return None
        else:
            return self.s1[0]

    # @return an boolean
    def empty(self):
        return self.s1==[]
