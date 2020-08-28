# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        x = rand7()                                 #Determines to choose from [1, 5] or [6, 10].
        while(x == 7):                              #Redo the selection while the chosen number is 7.
            x = rand7()                             #The number with equal chances will be either even (2,4,6) or odd (1,3,5). Note that 7 is excluded.
        
        r1_5 = rand7()                              #In here, generate a number between 1 and 5.
        while(r1_5 > 5):                            #Redo if it is larger than 5.
            r1_5 = rand7()
        return r1_5 + (x % 2) * 5                   #Return the number getting help from x % 2.
