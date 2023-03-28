class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dollars = [0] * 366                                                                                                                     #Initialize dollars needed from day 0 to each day.
        index = 0                                                                                                                               #Initialize the pointer to traverse in days.
        for i in range(1, 366):                                                                                                                 #Traverse from 1 to 365.
            if index < len(days) and i == days[index]:                                                                                          #If current day is a day to travel, calculate min cost till current day as the end of 1-day pass, 7-day pass and 30-day pass respectively.
                dollars[i] = min(dollars[i - 1] + costs[0], dollars[max(0, i - 7)] + costs[1], dollars[max(0, i - 30)] + costs[2])
                index += 1                                                                                                                      #Move forward index.
            else:                                                                                                                               #Otherwise, the min cost is same as previous day.
                dollars[i] = dollars[i - 1]
        return dollars[-1]                                                                                                                      #Return the min cost for last day.
