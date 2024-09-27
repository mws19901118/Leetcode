class MyCalendarTwo:
    def __init__(self):
        self.events = []                                                                        #Store events.
        self.overlaps = []                                                                      #Store existing double bookings.

    def book(self, start: int, end: int) -> bool:
        if any(self.does_overlap(x, y, start, end) for x, y in self.overlaps):                  #Check if the new booking overlaps with any double bookings.
            return False
        for x, y in self.events:                                                                #Check existing bookings, if it has overlap with new booking, add the overlap to double bookings.
            if self.does_overlap(x, y, start, end):
                self.overlaps.append(self.get_overlapped(x, y, start, end))
        self.events.append((start, end))                                                        #Add the new booking to events.
        return True

    def does_overlap(self, start1: int, end1: int, start2: int, end2: int) -> bool:             #Return True if the booking [start1, end1) & [start2, end2) overlaps.
        return max(start1, start2) < min(end1, end2)

    def get_overlapped(self, start1: int, end1: int, start2: int, end2: int) -> tuple:          #Return the overlap between [start1, end1) & [start2, end2).
        return max(start1, start2), min(end1, end2)
