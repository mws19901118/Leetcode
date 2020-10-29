class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        lastPerson = 0                                        #Index of last person.
        index = 0                                             #Index pointer.
        
        leftEnd = 0
        while index < len(seats):
            if seats[index] == 1:
                leftEnd = index - lastPerson                  #Find the distance between first person and left end.
                lastPerson = index                            #Update index of last person.
                break
            index += 1
        maxDist = 0
        while index < len(seats):
            if seats[index] == 1:
                maxDist = max(maxDist, index - lastPerson)    #Find the max distance between 2 adjacent people.
                lastPerson = index                            #Update index of last person.
            index += 1
        
        rightEnd = len(seats) - 1 - lastPerson                #Find the distance between last person and right end.
        return max(leftEnd, rightEnd, maxDist / 2)            #Return the max of leftEnd, rightEnd and half of maxDist.
