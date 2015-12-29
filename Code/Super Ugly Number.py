import heapq
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        k = len(primes)
        maxheap = []                                                      #Use a max heap to store the first k ugly numbers. (Originally it's min heap, so we convert it into max heap by storing the opposite number.)
        heapq.heappush(maxheap, -1)                                       #Push the first number -- 1.
        q = [[primes[i]] for i in range(k)]                               #Store the first level of ugly numbers(original primes). q[i] stands for the ugly numbers whose factors are only from primes[0] to primes[i].
        count = 1                                                         #Count current first numbers.
        while True:                                                       #BFS. Each level means the number of factors of current ugly numbers.
            stop = False                                                  #Indicate if we update the heap.
            for i in range(len(q)):
                for x in q[i]:                                            #Check each ugly number in current level.
                    if count < n:                                         #If we haven't found enough ugly numbers, push x into heap.
                        heapq.heappush(maxheap, -x)
                        stop = True                                       #This is an update to heap.
                        count += 1                                        #Update count.
                    else:
                        if -x > maxheap[0]:                               #Otherwise, if x is smaller than the top of heap, pop the heap and push x into heap.
                            heapq.heapreplace(maxheap, -x)
                            stop = True                                   #This is an update to heap.
            if stop is False:                                             #If we don't update the heap in current level, we can't find a new ugly number smaller than the current n-th ugly number, thus end BFS.
                break
            newq = [[] for i in range(len(q))]                            #Generate ugly numbers of next level.
            for i in range(len(q)):                                       #Traverse primes from primes[0] to primes[len(q)].
                for j in range(0, i + 1):                                 #Check each of ugly numbers in current level whose factors are from primes[0] to primes[i].
                    for x in q[j]:
                        if count < n or -x * primes[i] > maxheap[0]:      #If we haven't found enough ugly numbers or the new ugly number is smaller than the current n-th ugly number, generate the new ugly number by multiplying primes[i] and append it to newq[i].
                            newq[i].append(x * primes[i])
            while len(newq) > 0 and newq[-1] == []:                       #When we come to a large number, some primes may be to large to use as factor, so we don't have to consider them.
                newq.pop()                                                #Remove the corresponding list from newq.
            q = newq                                                      #Replace q with newq.
        return -maxheap[0]                                                #Return the n-th ugly number.
