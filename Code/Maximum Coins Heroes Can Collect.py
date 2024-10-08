class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        sortedMonster = sorted([(x, y) for x, y in zip(monsters, coins)])            #Sort monster and coin by the power of monster.
        sortedHero = sorted((x, i) for i, x in enumerate(heroes))                    #Sort hero by the power of hero and keeps original index.
        result = [0] * len(heroes)                                                   #Initialize result.
        index, prev = 0, 0                                                           #Use a pointer to traverse sortedMonster also keeps the result of previous hero(initially 0).
        for x, i in sortedHero:                                                      #Traverse sortedHero.
            result[i] = prev                                                         #Result of current hero should be not smaller than previous hero.
            while index < len(sortedMonster) and sortedMonster[index][0] <= x:       #Move forward index while it is valid and its monster has power smaller than or equal to current hero.
                result[i] += sortedMonster[index][1]                                 #Add its coin to current hero.
                index += 1
            prev = result[i]                                                         #Update prev.
        return result
