class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.movies_set = defaultdict(SortedSet)                                                             #Use sorted set to store the price and shop of each movie.
        self.rent_set = SortedSet()                                                                          #Use sorted set to store all rented movies.
        self.prices = {}                                                                                     #Store prices of each movie at each store.
        for s, m, p in entries:                                                                              #Traverse entries.
            self.movies_set[m].add((p, s))                                                                   #Add price p and store s to the sorted set of movie m.
            self.prices[(m, s)] = p                                                                          #Update the price of movie m at store s.

    def search(self, movie: int) -> List[int]:
        return [self.movies_set[movie][i][1] for i in range(min(5, len(self.movies_set[movie])))]            #Traverse the sorted set of movie and return the first 5 stores.

    def rent(self, shop: int, movie: int) -> None:
        p = self.prices[(movie, shop)]                                                                       #Get the price of movie at store.
        self.movies_set[movie].remove((p, shop))                                                             #Remove the price and shop from the sorted set of movie.
        self.rent_set.add((p, shop, movie))                                                                  #Add price, shop and movie to rented sorted set.

    def drop(self, shop: int, movie: int) -> None:
        p = self.prices[(movie, shop)]                                                                       #Get the price of movie at store.
        self.movies_set[movie].add((p, shop))                                                                #Add the price and shop to the sorted set of movie.
        self.rent_set.remove((p, shop, movie))                                                               #Remove price, shop and movie from rented sorted set.

    def report(self) -> List[List[int]]:
        return [[self.rent_set[i][1], self.rent_set[i][2]] for i in range(min(5, len(self.rent_set)))]       #Traverse the rented sorted set of movie and return the first 5 shops and movies.


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
