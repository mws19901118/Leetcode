class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        front = 0
        while front + 1 < len(arr) and arr[front + 1] > arr[front]:     #Find the index of peak element from the front.
            front += 1
        back = len(arr) - 1
        while back - 1 >= 0 and arr[back - 1] > arr[back]:              #Find the index of peak element from the back.
            back -= 1
        return front == back and front != len(arr) - 1 and back != 0    #Front and back should be equal and also can't be on the boundary of either side of arr.
