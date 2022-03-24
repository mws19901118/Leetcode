class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()                                                       #Sort people's weight.
        start, end, boats = 0, len(people) - 1, 0                           #Initialize 2 pointers at the start and the end of people and the count of boats.
        while start <= end:                                                 #Traverse people.
            while start < end and people[start] + people[end] > limit:      #For the weight of people[start], find the max weight so that people[start] + people[end] <= limit. 
                boats += 1                                                  #Each person after people[weight] needs a single boat.
                end -= 1
            boats += 1                                                      #people[start] and people[end] can be put in same boat.
            start += 1
            end -= 1
        return boats                                                        #Return boats.
