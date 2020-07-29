class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = list(collections.Counter(tasks).values())                   #Count each task.
        maxNum = max(count)                                                 #Find the max count of a task and how many tasks have max count.
        maxNumCount = count.count(maxNum)                                   #If there are idle CPU cycles, the total time needed is (n + 1) * (maxNum - 1) + maxNumCount.
        return max(len(tasks), (n + 1) * (maxNum - 1) + maxNumCount)        #If there is no idel CPU cycle, the total time needed is the length of tasks.
                                                                            #So, return the max result of time needed with and without idle CPU cycles.
