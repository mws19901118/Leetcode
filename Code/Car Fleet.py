class Solution:
    def catchUp(self, car1, car2, target):                                          #Determine if a car in the behind(car1) can catch up a car in the front(car2).
        return (target - car1[0]) / car1[1] <= (target - car2[0]) / car2[1]         #If car1 can catch up car2, the time needed to travel from starting position to target should not be larger than that of car2.
    
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position or not speed:                                               #If no cars, return 0.
            return 0
        car = sorted([(p, s) for p, s in zip(position, speed)], reverse = True)     #Use a tuple of (position, speed) to represent each car and sort by position in descending order.
        lead = car[0]                                                               #Initially, the lead car is the first car after sort, and there is one car fleet.
        count = 1
        for i in range(1, len(car)):                                                #For each car behind lead, if current car can not catch up the lead, then there is no more car for the car fleet that the lead car belongs to.
            if not self.catchUp(car[i], lead, target):
                count += 1                                                          #Increase count of car fleet by 1.
                lead = car[i]                                                       #Now, current car is the new lead car.
        return count                                                                #Return count.
