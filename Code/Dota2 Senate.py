class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q = [x for x in senate]                                       #Split input senate to a list of characters.
        countR, countD = q.count('R'), q.count('D')                   #Count R and D.
        banR, banD = 0, 0                                             #Count banned R and banned D.
        while True:                                                   #Iterate.
            newCountR, newCountD = 0, 0                               #Count remaining R and remaining D in next round.
            newq = []                                                 #Store remaining senate in next round.
            for x in q:                                               #Traverse current senate.
                if not countR and countD:                             #If only Dore left, return Dire.
                    return 'Dire'
                elif not countD and countR:                           #If only Radiant left, return Dadiant.
                    return 'Radiant'
                if x == 'R':                                          #Handle current Radiant.
                    if banR:                                          #If there are Radiants to be banned, ban current one and decrease banR.
                        banR -= 1
                    else:                                             #Otherwise, ban a Dire and increase newCountR and append x to newq.
                        banD += 1
                        newCountR += 1
                        newq.append(x)
                else:                                                 #Handle current Dire.
                    if banD:                                          #If there are Dires to be banned, ban current one and decrease banD.
                        banD -= 1
                    else:                                             #Otherwise, ban a Radiant and increase newCountD and append x to newq.
                        banR += 1
                        newCountD += 1
                        newq.append(x)
            q = newq                                                  #Replace q with newq.
            countR, countD = newCountR, newCountD                     #Update countR and countD.
