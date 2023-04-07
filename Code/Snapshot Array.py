class SnapshotArray:

    def __init__(self, length: int):
        self.snapshots = [[] for _ in range(length)]                                      #Only store changed values with snapshot.
        self.currentSnap = 0                                                              #Store current snap.

    def set(self, index: int, val: int) -> None:
        self.snapshots[index].append((self.currentSnap, val))                             #Append self.currentSnap and val as tuple to the snapshot of index. If there are multiple set at current snap, it doesn't matter to insert them all, because the binary search always find the last one.

    def snap(self) -> int:
        self.currentSnap += 1                                                             #Increase self.currentSnap.
        return self.currentSnap - 1                                                       #Return the original value.

    def get(self, index: int, snap_id: int) -> int:
        snap = bisect_right(self.snapshots[index], (snap_id, 1000000001))                 #Binary search in self.snapshots[index] to find the right most place to insert snap_id and a really large value.
        return 0 if not snap else self.snapshots[index][snap - 1][1]                      #If snap is 0, return 0 because the value at index is not set yet; otherwise, return self.snapshots[index][snap - 1][1], which is the lateset value of index at snap_id.


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
