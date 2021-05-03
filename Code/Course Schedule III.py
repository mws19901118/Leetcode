class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda x: x[1])          #Sort courses by last day.
        heap = []                                   #Initailize a max heap.
        total, count = 0, 0                         #Initialize the total time used so far and the count of max courses can be taken.
        for c in courses:                           #Traverse courses.
            if total + c[0] <= c[1]:                #If total + c[0] <= c[1], current course can be taken.
                count += 1                          #Update count.
                total += c[0]                       #Update total.
                heapq.heappush(heap, -c[0])         #Push the current course duration to max heap.
            elif heap and -heap[0] > c[0]:          #Else if heap is not empty and the max duration of courses we have taken is larger than current course duration, we drop that coures and take this course. 
                total += heap[0] + c[0]             #Update total.
                heapq.heappop(heap)                 #Pop heap.
                heapq.heappush(heap, -c[0])         #Push the current course duration to max heap.
        return count                                #Return count.
