class Solution:
    def bestClosingTime(self, customers: str) -> int:
        nFromBeginning, yFromEnd = 0, Counter(customers)['Y']      #Store the count of 'N' from beginning and count of 'Y' from end.
        minPenalty, hour = nFromBeginning + yFromEnd, 0            #Initialize minimum penalty to be the sum of nFromBeginning and yFromEnd at 0th hour and shop close hour to be 0.
        for i, x in enumerate(customers):                          #Traverse customers.
            nFromBeginning += int(x == 'N')                        #Update nFromBeginning if necessary.
            yFromEnd -= int(x == 'Y')                              #Update yFromEnd if necessary.
            if nFromBeginning + yFromEnd < minPenalty:             #If the sum of nFromBeginning and yFromEnd is smaller than current min penalty, update minPenalty and shop close hour.
                minPenalty = nFromBeginning + yFromEnd
                hour = i + 1
        return hour                                                #Return hour.
