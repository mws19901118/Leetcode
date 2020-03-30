class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0
        for i in range(len(rating)):                                #Iterate over each soldier.
            lower, higher = [0, 0], [0, 0]
            for j in range(len(rating)):
                if rating[j] < rating[i]:                           #Calculate the count of solders whose rating is lower than current soldier, both before current soldier and after current soldier.
                    lower[int(i < j)] += 1
                if rating[j] > rating[i]:                           #Calculate the count of solders whose rating is higher than current soldier, both before current soldier and after current soldier.
                    higher[int(i < j)] += 1
            count += lower[0] * higher[1] + lower[1] * higher[0]    #The total unique teams can form with current soldier in the middle is lower[left] * higher[right] + higher[left] * lower[right].
        return count
