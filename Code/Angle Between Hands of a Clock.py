class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hourHand = (hour % 12 + minutes * 1.0 / 60) * 30                                #Calculate the angle of hour hand.
        minutesHand = minutes * 6                                                       #Calculate the angle of minute hand.
        return min(abs(hourHand - minutesHand), 360 - abs(hourHand - minutesHand))      #Calculete the abosulute value of the difference betweem hour hand and minute hand. Return the min value of difference and 360 - difference.
