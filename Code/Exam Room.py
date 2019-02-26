'''
We will name a range of unoccupied seats from i to j an Available segment with first index i and last index j. For each available segment we can say how far the "best" seat in this segment is from the closest occupied seat. The number of empty seats in between is priority of the segment. The higher the priority the better seat you can get from a segment. For the edge cases when segment starts with index 0 or ends with index N - 1 priority equals to segment_size - 1. For segments in the middle of the row priority can be calculated as (segment_size - 1) // 2 or (last - first) // 2. Please note that two segments of different size may have equal priority. For example, segments with 3 seats and with 4 seats have the same priority "1".

We will use priority queue self.heap to store all currently available segments. Python implements heapq as min heap, so we will use negated priority to keep the best availabe segment on top of the queue. If two segments have equal priority, then the one with lower first index is better. Taken this into account, we will store availabale segment in self.heap as 4-items list: [-segment_priority, first_index_of_segment, last_index_of_segment, is_valid]. The first two items -segment_priority and first_index_of_segment guarantee correct priority queue order.

A helper function put_segment() takes first and last index of the available segment, calculates its priority and pushes a list object into self.heap. In addition, it puts this list object into two dicts: self.avail_first[first] = segment and self.avail_last[last] = segment. These dicts will be used later in leave().

We start with only one available segment [0, N - 1]. When seat() is called, we pop best available segment from self.heap. If segment's is_valid flag is False then we pop another one, until we get a valid available segment. There are two edge cases when popped segment starts at 0 or ends at N - 1. For these cases we return the edge seat number (0 or N - 1 respectively) and push new segment into self.heap. Otherwize, when the popped segment is in the middle of the row, we return its middle seat and create up to two new available segments of smaller size, and push them into self.heap.

Now, leave() implementation is quite interesting. When seat p is vacated, we need to check if there are adjacent available segment(s) in the heap, and merge them together with p. We use dicts self.avail_first and self.avail_last to check for adjacent available segments. If these segment(s) are found, they need to be excluded from self.heap. Deleting items in self.heap will break heap invariant and requires subsequent heapify() call that executes in O(n log n) time. Instead we can just mark segments as invalid by setting is_valid flag: segment[3] = False. Invalid segments will be skipped upon heappop() in seat().

https://leetcode.com/problems/exam-room/discuss/139941/Python-O(log-n)-time-for-both-seat()-and-leave()-with-heapq-and-dicts-Detailed-explanation
'''

from heapq import heappop, heappush


class ExamRoom(object):

    def __init__(self, N):
        """
        :type N: int
        """
        self.N = N
        self.heap = []
        self.avail_first = {}
        self.avail_last = {}
        self.put_segment(0, self.N - 1)

    def put_segment(self, first, last):

        if first == 0 or last == self.N - 1:
            priority = last - first
        else:
            priority = (last - first) // 2

        segment = [-priority, first, last, True]

        self.avail_first[first] = segment
        self.avail_last[last] = segment

        heappush(self.heap, segment)

    def seat(self):
        """
        :rtype: int
        """
        while True:
            _, first, last, is_valid = heappop(self.heap)

            if is_valid:
                del self.avail_first[first]
                del self.avail_last[last]
                break

        if first == 0:
            ret = 0
            if first != last:
                self.put_segment(first + 1, last)

        elif last == self.N - 1:
            ret = last
            if first != last:
                self.put_segment(first, last - 1)

        else:
            ret = first + (last - first) // 2

            if ret > first:
                self.put_segment(first, ret - 1)

            if ret < last:
                self.put_segment(ret + 1, last)

        return ret

    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """
        first = p
        last = p

        left = p - 1
        right = p + 1

        if left >= 0 and left in self.avail_last:
            segment_left = self.avail_last.pop(left)
            segment_left[3] = False
            first = segment_left[1]

        if right < self.N and right in self.avail_first:
            segment_right = self.avail_first.pop(right)
            segment_right[3] = False
            last = segment_right[2]

        self.put_segment(first, last)
