class Stack:
    # initialize your data structure here.
    def __init__(self):                                   #Use 2 queues to simulate stack.
        self.q1=[]
        self.q2=[]

    # @param x, an integer
    # @return nothing
    def push(self, x):
        if self.q1==[]:                                   #If q1 is empty, append x into q2; otherwise append x into q1.
            self.q2.append(x)
        else:
            self.q1.append(x)

    # @return nothing
    def pop(self):
        if self.q1==[]:                                 #If q1 is empty, deque all the elements of q2 and append them into q1 except the last element.
            while len(self.q2)>1:
                self.q1.append(self.q2[0])
                self.q2.remove(self.q2[0])
            self.q2.remove(self.q2[0])
        else:                                           #If q2 is empty, deque all the elements of q1 and append them into q2 except the last element.
            while len(self.q1)>1:
                self.q2.append(self.q1[0])
                self.q1.remove(self.q1[0])
            self.q1.remove(self.q1[0])

    # @return an integer
    def top(self):
        if self.q1==[] and self.q2==[]:                 #If q1 and q2 are both empty, return None.   
            return None
        elif self.q1==[]:                               #If q1 is empty, return the last element of q2.
            return self.q2[-1]
        else:                                           #If q2 is empty, return the last element of q1.
            return self.q1[-1]

    # @return an boolean
    def empty(self):
        return self.q1==[] and self.q2==[]              #If q1 and q2 are both empty, return true; otherwise return false.
        
