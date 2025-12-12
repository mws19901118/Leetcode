class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        countAll = 0                                          #Count message for ALL.
        online = set(i for i in range(numberOfUsers))         #Store online users in a set; initially all users.
        sortedEvents = []                                     #Store sorted events.
        for e, t, s in events:                                #Traverse events.
            t = int(t)
            if e == 'OFFLINE':                                #If event type is OFFLINE, append (t, 2, s)(offline) and (t + 60, 1, s)(online) to sortedEvents.
                sortedEvents.append((t, 2, s))
                sortedEvents.append((t + 60, 1, s))
            elif s == 'ALL':                                  #If event type is MESSAGE and target is ALL, increase countAll.
                countAll += 1
            else:                                             #Otherwise, append message event with timestamp t and priority 3 to sortedEvents.
                sortedEvents.append((t, 3, s))
        sortedEvents.sort()                                   #Sort sortedEvents by timestamp then by priority in ascending order.
        result = [0] * numberOfUsers                          #Initialize result.
        for t, p, s in sortedEvents:                          #Traverse sortedEvents.
            if p == 1:                                        #If event priority is 1, add s to online.
                online.add(int(s))
            elif p == 2:                                      #If event priority is 2, remove s from online.
                online.remove(int(s))
            elif s == 'HERE':                                 #If message is for HERE, increase result for every online user.
                for id in online:
                    result[id] += 1
            else:                                             #Otherwise, increase result for every mentioned user.
                for x in s.split(' '):
                    id = int(x[2:])
                    result[id] += 1
        for i in range(numberOfUsers):                        #For each user, increase result by countAll.
            result[i] += countAll
        return result
