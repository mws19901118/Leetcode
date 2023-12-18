from sortedcontainers import SortedSet

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_rating_map = {}                                          #Initialize a map from food to rating.
        self.food_cuisine_map = {}                                         #Initialize a map from food to cuisine.
        self.cuisine_food_map = defaultdict(SortedSet)                     #Use a SortedSet to store food and rating for each cuisine.
        for f, c, r in zip(foods, cuisines, ratings):                      #Traverse foods, cuisines and ratings together.
            self.food_rating_map[f] = -r                                   #Set the rating for current food.
            self.food_cuisine_map[f] = c                                   #Set the cuisine for current food.
            self.cuisine_food_map[c].add((-r, f))                          #Add (-r, f) to the SortedSet of current cuisine

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_cuisine_map[food]                              #Get the cuisine of current food.
        prev = (self.food_rating_map[food], food)                          #Get the previous value for current food in the foot rating map.
        self.cuisine_food_map[cuisine].remove(prev)                        #Remove it from the SortedSet of current cuisine.
        self.food_rating_map[food] = -newRating                            #Update food rating map with new value.
        self.cuisine_food_map[cuisine].add((-newRating, food))             #Insert new value of current food into the SortedSet of current cuisine.

    def highestRated(self, cuisine: str) -> str:
        return self.cuisine_food_map[cuisine][0][1]                        #Return the food name in first tuple in the SortedSet of current cuisine.
