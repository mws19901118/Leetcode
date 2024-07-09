class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        count, finishTime = 0, 0                      #Count total waiting time and the finish time of last customer.
        for a, t in customers:                        #Traverse customers.
            finishTime = max(a, finishTime) + t       #Start at max of arriving time and last finish time then it taks t time to finish the dish.
            count += finishTime - a                   #Add the wait time for current customer to count.
        return count / len(customers)                 #Return the average of wait time.
