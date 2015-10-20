class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        if A>=G or B>=H or E>=C or F>=D:                                                  #If the 2 rectangles don't overlap, return the sum of areas.
            return (D-B)*(C-A)+(H-F)*(G-E)
        else:                                                                             #If they overlap, return the sum of areas minus the overlapping area.
            return (D-B)*(C-A)+(H-F)*(G-E)-(min(C,G)-max(A,E))*(min(H,D)-max(B,F))        #The overlapping area is (min(C,G)-max(A,E))*(min(H,D)-max(B,F))
                
