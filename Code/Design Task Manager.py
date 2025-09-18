class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.userByTask = defaultdict(int)                                #Store user id by task id.
        self.priority = defaultdict(int)                                  #Store priority of each task.
        self.taskPool = SortedSet()                                       #Store pending tasks.
        for u, t, p in tasks:                                             #Traverse tasks.
            self.add(u, t, p)                                             #Add each task.
        
    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.userByTask[taskId] = userId                                  #Map userId by taskId.
        self.priority[taskId] = priority                                  #Add task priority.
        self.taskPool.add((-priority, -taskId))                           #Push (-priority, -taskId) to task pool to maintain the max priority.

    def edit(self, taskId: int, newPriority: int) -> None:
        userId = self.userByTask[taskId]                                  #Get user id of current task.
        self.rmv(taskId)                                                  #Remove current task.
        self.add(userId, taskId, newPriority)                             #Add back same task with new priority.

    def rmv(self, taskId: int) -> None:
        self.taskPool.remove((-self.priority[taskId], -taskId))           #Remove task from task pool.
        self.userByTask.pop(taskId)                                       #Remove userId by taskId map.
        self.priority.pop(taskId)                                         #Remove task priority.

    def execTop(self) -> int:
        if not self.taskPool:                                             #If task pool is empty, return -1.
            return -1
        taskId = -self.taskPool[0][1]                                     #Find the task with highest priority.
        userId = self.userByTask[taskId]                                  #Get its user.
        self.rmv(taskId)                                                  #Remove task.
        return userId                                                     #Return user.


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
