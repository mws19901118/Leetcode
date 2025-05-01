class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()                                                              #Sort tasks in asending order.
        workers.sort()                                                            #Sort workers in asending order..
        
        def assign(x: int) -> bool:                                               #Check if it is possible to assign tasks for x worker.
            p = pills                                                             #Initialize pills remaining.
            sorted_workers = SortedList(workers[len(workers) - x:])               #Put the largest x workers in a sorted list.
            for i in reversed(range(x)):                                          #Traverse the smallest x tasks from behind.
                if sorted_workers[-1] >= tasks[i]:                                #If current largest worker can work on current task, pop the worker from sorted list.
                    sorted_workers.pop()
                elif not p:                                                       #Otherwise, if p is 0, no pills left and current worker cannot be assigned with any task, return false.
                    return False
                else:                                                             #Otherwise, binary search the index of worker with min strength to work on current task after taking a pill.
                    index = sorted_workers.bisect_left(tasks[i] - strength)
                    if index == len(sorted_workers):                              #If cannot find such worker, return false.
                        return False
                    sorted_workers.pop(index)                                     #Pop that worker from sorted list.
                    p -= 1                                                        #Consume 1 pill.
            return True

        start, end, result = 1, min(len(workers), len(tasks)), 0                  #Binary search from 1 to min(len(workers), len(tasks)) to find the max number of tasks can be assigned.
        while start <= end:
            mid = (start + end) // 2
            if assign(mid):
                result = mid
                start = mid + 1
            else:
                end = mid - 1

        return result
