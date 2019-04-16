from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        times = list(map(lambda x: -x, Counter(tasks).values()))      #Count each tasks and convert counts to a list where each element is the negative value of count.
        heapq.heapify(times)                                          #Heapify times so it's a max heap of count(min heap of negative value of count).
        result = 0                                                    #Initialize result.
        while times:                                                  #While we have tasks unscheduled, iterate scheduling tasks.
            temp = []                                                 #Use a list to store tasks scheduled in this iteration but has remains.
            c = 0                                                     #Initialize the number of tasks scheduled in this iteration.
            while times and c < n + 1:                                #While we have tasks unscheduled and the number of tasks scheduled is not equal to n + 1(Needs cooling, so the max of tasks scheduled in each iteration is n + 1).
                x = heapq.heappop(times) + 1                          #Pop the count on heap top, decrthe count by 1(increase the negative value of count by 1).
                if x < 0:                                             #If count is larger than 0(negative value of count smaller than 0), append count to temp.
                    temp.append(x)
                c += 1                                                #Increase c by 1, meaning we schedule the task.

            for x in temp:                                            #For each count in temp, push it back to the max heap.
                heapq.heappush(times, x)
            
            if times:                                                 #If we have tasks unscheduled, add the max value between c and n + 1 to result.
                result += max(c, n + 1)
            else:                                                     #Otherwise we have scheduled all tasks, so no cooling interval needed, just add c to result.
                result += c

        return result                                                 #Return result.
