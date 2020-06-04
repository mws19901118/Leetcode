class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        cost = sum([costs[i][0] for i in range(len(costs))])              #Each person will either fly to city A or city B. Assume they all fly to city A initially and calculate the cost.
        diff = [costs[i][1] - costs[i][0] for i in range(len(costs))]     #Calculate the diff of cost for each person it that person flies to city B.
        diff.sort()                                                       #Sort diff of cost in ascending order.
        cost += sum(diff[i] for i in range(len(costs) // 2))              #Add the first half of sorted diff of cost. This should minimize the total cost.
        return cost
