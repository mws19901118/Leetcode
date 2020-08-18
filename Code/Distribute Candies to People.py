class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        iterationSum = (num_people + 1) * num_people // 2                                                                       #Calculate the sum of first iteration, i.e. 1, 2, ..., n.
        iterations = 0
        while candies >= iterationSum:                                                                                          #Calculate how many full interations the candies can be distributed.
            iterations += 1
            candies -= iterationSum
            iterationSum += num_people * num_people                                                                             #Each iteration is pervious iteration plus n ^ 2.
        result = [max(0, ((iterations - 1) * num_people + (i + 1) * 2) * iterations // 2) for i in range(num_people)]           #Calculate how many candies are already distributed to each person. For ith person, it's sum of i + 1, n + i + 1, 2n + i + 1, ..., (iteration - 1) * n + i + 1, i.e. ((iteration - 1) * n + 2 * (i + 1)) * iteration // 2. 
        currentCandyInNeed = iterations * num_people + 1                                                                        #Calculate the candy needed by first person in the last iteration, i.e. iterations * n + 1.
        i = 0
        while candies:                                                                                                          #While there are candies remaning, simulate last iteration.
            currentCandyInNeed = min(currentCandyInNeed, candies)                                                               #If candies are not enough, give all of them to current person.
            result[i] += currentCandyInNeed                                                                                     #Distribute candy to current person.
            candies -= currentCandyInNeed                                                                                       #Calculate remaining candies.
            currentCandyInNeed += 1                                                                                             #Plus one for the candy needed by next person.
            i += 1                                                                                                              #Go to next person.
        return result
