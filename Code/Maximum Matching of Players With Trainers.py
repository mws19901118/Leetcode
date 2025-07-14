class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()                                            #Sort players.
        trainers.sort()                                           #Sort trainers.
        index, result = 0, 0                                      #Initialize index in players and also initialize result.
        for x in trainers:                                        #Traverse trainers.
            if index < len(players) and players[index] <= x:      #If index hasn't reached the end and players[index] is not greater than x. we can assign the player to the trainer.
                index += 1                                        #Increase index.
                result += 1                                       #Increase result.
        return result
