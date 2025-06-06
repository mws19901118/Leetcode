class Solution:
    def robotWithString(self, s: str) -> str:
        count = Counter(s)                                                              #Count each character in s.
        order = sorted(count.keys())                                                    #Sort the characters in s.
        index = 0                                                                       #Initialize a pointer to traverse order.
        result, stack = [], []                                                          #Initialize result and a stack.
        for x in s:                                                                     #Traverse s.
            count[x] -= 1                                                               #Decrease count[x] as it is visited.
            stack.append(x)                                                             #Append x to stack, i.e. t.
            while stack and index < len(order) and stack[-1] <= order[index]:           #While stack is not empty and index hasn't reached the end of order and the stack top is not greater than order[index], pop stack and append it to result.
                result.append(stack.pop())
                while index < len(order) and not count[order[index]]:                   #While index hasn't reached the end of order and count[order[index]] is 0, move forward index. After the loop, order[index] is the smallest unvisited character, if index hasn't reached the end.
                    index += 1
        result.extend(stack[::-1])                                                      #For the rest of stack, reverse it then append to result.
        return "".join(result)                                                          #Join result and return.
