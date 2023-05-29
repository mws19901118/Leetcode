class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.slots = [big, medium, small]                   #Store available slots of each car type in a list.

    def addCar(self, carType: int) -> bool:
        if not self.slots[carType - 1]:                     #If the corresponding car type has no slots, return false.
            return False
        self.slots[carType - 1] -= 1                        #Otherwise, decrease the slots and return true.
        return True


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
