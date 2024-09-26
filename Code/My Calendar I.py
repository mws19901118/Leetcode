from sortedcontainers import SortedList

class MyCalendar:
    def __init__(self):
        self.calendar = SortedList()                                                                                                        #Store events in a sorted list.

    def book(self, start: int, end: int) -> bool:
        index = self.calendar.bisect_right((start, end))                                                                                    #Binary search for the rightmost index to insert current event.
        if (index > 0 and self.calendar[index - 1][1] > start) or (index < len(self.calendar) and self.calendar[index][0] < end):           #If it conflicts with event before or after, return false.
            return False
        self.calendar.add((start, end))                                                                                                     #Otherwise, insert current event and return true.
        return True
