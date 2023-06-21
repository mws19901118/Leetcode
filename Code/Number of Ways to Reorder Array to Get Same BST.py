class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        division = 10 ** 9 + 7                                                                                        #Initialize division.
        
        def DFS(nums: List[int]) -> int:                                                                              #DFS to find the total number of ways to form same BST with given number list.
            if len(nums) <= 2:                                                                                        #If there are no more than 2 numbers, there is only one way to form BST.
                return 1
            smaller, greater = [x for x in nums[1:] if x < nums[0]], [x for x in nums[1:] if x > nums[0]]             #Partition nums[1:] based on the if numbers is smaller or greater than nums[0].
            return DFS(smaller) * DFS(greater) * comb(len(nums) - 1, len(smaller)) % division                         #Form left subtree and right subtree using smaller and greater respectively and calculate result recursively.
                                                                                                                      #We can also rearrange nums[1:], to choose len(smaller) places out of len(nums) - 1 places to put smaller. So the final result is DFS(smaller) * DFS(greater) * comb(len(nums) - 1, len(smaller)) % division.
        return (DFS(nums) - 1) % division                                                                             #Return DFS(nums) - 1 after taking modulo.
