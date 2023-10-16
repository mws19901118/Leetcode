class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        def calculateSum(l: int, r: int) -> int:                                  #Calculate the books taken from books[l:r + 1] ending at r with the condition that every bookshelf i in books[l:r] has at least books[r] - r + i.
            length = min(books[r], r - l + 1)                                     #Since the books taken have to be strictly increasing from left to right, the length of contiguous bookshelves is min(books[r], r - l + 1). 
            return (2 * books[r] - (length - 1)) * length // 2                    #To maxmize books taken, the number of books taken from each bookshelf is an arithmetic array, so calculate the sum of the arithmetic way.

        stack = [-1]                                                              #Use a monostack to store the index of bookshelves whose book numbers are strictly increasing while traversing books.
        dp = [0]                                                                  #Store the max number of books taken ending at each bookshelf, with initial 0 as no books taken before traversing.
        for i, x in enumerate(books):                                             #Traverse books.
            # While we cannot push i, we pop from the stack
            while stack[-1] != -1 and books[stack[-1]] - stack[-1] >= x - i:      #While stack[-1] is not -1 and pop stack and books[stack[-1]] is at least x + stack[-1] - i to form an arithmetic array whose difference is 1 from stack[-1] to i, pop stack.
                stack.pop()
            dp.append(dp[stack[-1] + 1] + calculateSum(stack[-1] + 1, i))         #Calculate the books taken ending at current bookshelf. It is the dp[stack[-1] + 1] plus the books taken in books[stack[-1] + 1:i + 1].
            stack.append(i)                                                       #Append i to stack.
        return max(dp)                                                            #Return max in dp.
