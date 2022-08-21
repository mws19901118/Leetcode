class Solution:
    def shouldStamp(self, x: str, stamp: str) -> bool:                                              #Determine if x can be formed by stamping.
        return x != '?' * len(x) and all(a in (b, '?') for a, b in zip(x, stamp))                   #If x is already all '?', we don't need to stamp. If any character is neither the corrsponding character in stamp nor '?', return false; otherwise return true.
        
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        result = []                                                                                 #Think reversely, replacing available substring back to '?'. So, store the index to stamp in reverse order.
        visited = [False] * len(target)                                                             #Store if we have already stamped at current index.
        flag = True                                                                                 #Indicate if we should keep iterating.
        while flag:
            flag = False                                                                            #If no stamp can be performed in current iteration, we should stop.
            for i in range(len(target) - len(stamp) + 1):                                           #Check every possible index.
                if not visited[i] and self.shouldStamp(target[i:i + len(stamp)], stamp):            #If i is not stamped and target[i:i + len(stamp)] can be formed by stamping, stamp at i.
                    target = target[:i] + '?' * len(stamp) + target[i + len(stamp):]
                    result.append(i)                                                                #Append i to result.
                    visited[i] = True
                    flag = True
        return result[::-1] if target == '?' * len(target) else []                                  #If target is all '?', we can find a sequence to stamp, so, reverse result and return; otherwise return empty list.
