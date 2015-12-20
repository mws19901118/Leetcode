# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return -1
        q = []                                                          #Store the candidates.
        for i in range(n):
            q.append(i)
        while len(q) > 1:
            newq = []
            for i in range(len(q) / 2):                                 #For candidate q[2 * i] and q[2 * i + 1], ask if q[2 * i] knows q[2 * i + 1].
                if knows(q[2 * i], q[2 * i + 1]):                       #If q[2 * i] knows q[2 * i + 1], q[2 * i] can't be the celebrity.
                    newq.append(q[2 * i + 1])
                else:                                                   #If q[2 * i] doesn't knows q[2 * i + 1], q[2 * i + 1] can't be the celebrity.
                    newq.append(q[2 * i])
            if len(q) % 2 == 1:                                         #If there is 1 candidate last, put it in the new candidate list.
                newq.append(q[-1])
            q = newq
        for i in range(n):                                              #Check if the last candidate is valid, it should be known by every all the others but knows no one.
            if i != q[0] and (not knows(i, q[0]) or knows(q[0], i)):
                return -1
        return q[0]
