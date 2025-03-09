class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)                                    #Get the number of tiles.
        i = 1                                              #Find the index of first tile that is same as its previous tile.
        while i < n and colors[i] ^ colors[i - 1]:
            i += 1
        if i == n and colors[-1] ^ colors[0]:              #If there is no such tile and the last tile is not as first tile, the tiles in circle are all alternating.
            return n                                       #Thus, return n because every tile can be the start of an alternating group.
        length, result = 1, 0                              #Initialize alternating subarry length and result.
        for j in range(i + 1, i + n):                      #Traverse n - 1 tiles from i + 1.
            if colors[j % n] ^ colors[(j - 1) % n]:        #If current tile is not same as its previous tile, increase length and increase result if length is not smaller than k.
                length += 1
                result += length >= k
            else:                                          #Otherwise, reset length to 1 to start a new alternating subarray.
                length = 1
        return result
