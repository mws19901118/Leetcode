class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        points = []                                                  #Put meeting start day and end day in points.
        for x, y in meetings:
            points.append((x, 0))                                    #Start day shoulkd have tag 0 while end day should have tag 1 so for start days and end days on same day, start should cones first.
            points.append((y, 1))
        points.sort()                                                #Sort points.
        last_meeting_end, count, result = 0, 0, 0                    #Initialize last meeting end day, count of overlap meetings and result.
        for x, t in points:                                          #Traverse points.
            if not t:                                                #If it is start day, increase count.
                if not count :                                       #Before increasing count, if count is 0, then the gap from last meeting end to now is a potential no meeting day(the length has to be positive_.
                    result += max(0, x - last_meeting_end - 1)
                count += 1
            else:                                                    #If it is end day, decrease count.
                count -= 1
                if not count:                                        #After decreasing count, if count is 0, then update last meeting end day,
                    last_meeting_end = x
        return result + days - last_meeting_end                      #Return result + gap from last meeting end day to the last day.
