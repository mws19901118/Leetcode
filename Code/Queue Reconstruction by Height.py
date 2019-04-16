from functools import cmp_to_key
class Solution:
    def cmp(self, p1, p2):                                  #Customized sort: for people, first sort by height in descending order than for people in the same height, sort by number of person in the front in ascending order.
        if p1[0] > p2[0]:
            return -1
        elif p1[0] < p2[0]:
            return 1
        elif p1[1] > p2[1]:
            return 1
        elif p1[1] < p2[1]:
            return -1
        else:
            return 0
        
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=cmp_to_key(self.cmp)) #Customized sort.
        queue = []                                        #Initialize a queue.
        for p in people:                                  #For each people(k, h) after sort, insert it in the kth position of queue.
            queue.insert(p[1], p)                         #Because we already processed higher people, so after insertion, the number of person in the front won't be affected by upcoming insertion.
        return queue                                      #Return queue.
