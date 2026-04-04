class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        columns = len(encodedText) // rows                                                                                   #Calculate the columns, since it is a matrix and we know the rows.
        diagonals = ["".join([encodedText[j] for j in range(i, len(encodedText), columns + 1)]) for i in range(columns)]     #Traverse each diagonal starting at the first row, and join the diagonal as string.
        return "".join(diagonals).rstrip()                                                                                   #Join all the diagonals, strip the trailing spaces and return.
