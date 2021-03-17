class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):                                    #Stpre radius, x_center and y_center.
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        angle = 2 * math.pi * random.random()                                                               #Generate a random angle between 0 and math.pi * 2.
        length = self.radius * math.sqrt(random.random())                                                   #Generate a random length between 0 and self.radius. Because circle is 2D figure, to make distribution random, take the root of random; otherwise it's distributed more close to the center.
        return [self.x_center + length * math.cos(angle), self.y_center + length * math.sin(angle)]         #Calculate the coordinates based on polar notation and return.

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
