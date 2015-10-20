class Solution:
    # @return a string
    def getPermutation(self, n, k):
        k-=1                                #k minus 1, because the index of a list begins with 0.
        seq=[]
        result=""
        for i in range(1,n+1):
            seq.append(i)                   #Store all the digits between 1 and n in a list.
        amount=1
        for i in range(1,n):
            amount*=i                       #Calculate (n-1)!, which is the amount of permutations of n starting with a certain digit.
        for i in range(1,n):
            index=k/amount                  #Calculate the starting digit, which is the index-th element in seq.
            k=k%amount                      #Calculate the remaining k to calculate the next digit.
            result+=str(seq[index])
            seq.remove(seq[index])          #Remove this digit from seq.
            amount/=(n-i)                   #Divide amount by n-1, in order to calculate the next digit.
        result+=str(seq[0])                 #Add the only element left in seq to result. It's the last digit.
        return result
