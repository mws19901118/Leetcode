# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.it = iterator
        self.buffur = None                                                      #Use a buffer int to store the peeking element. If there is no peeking elements, it's none.
        if self.it.hasNext():
            self.buffer = self.it.next()                                        #Get tbe peeking element and store it in buffer.

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.buffer                                                      #Return buffer.

    def next(self):
        """
        :rtype: int
        """
        temp = self.buffer
        self.buffer = self.itr.next() if self.itr.hasNext() else None
        return temp                                                             #Return old buffer.

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.buffer != None                                              #If buffer is none, there is no next element.

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
