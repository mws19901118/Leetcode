class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        division = 10 ** 9 + 7                                              #Initialize division.
        valid_column_states = []                                            #Initialize valid states of colors of any column.
        for state in range(3 ** m):                                         #Traverse from 0 to 3 ** m, because each cell can have 3 colors.
            colors = list()
            t = state
            for _ in range(m):                                              #Convert the state to a list of colors whose length is m.
                color.append(t % 3)
                t //= 3
            if any(color[i] == color[i + 1] for i in range(m - 1)):         #If there is same colors in adjacent cells, skip.
                continue
            valid_column_states.append("".join(str(x) for x in color))      #Convert state to string and append it to valid states.
            
        adjacent_column_states = defaultdict(list)                          #Initialize the valid adjacent column states for each valid states.
        for i, x in enumerate(valid_column_states):                         #Traverse each pair of valid states.
            for j, y in enumerate(valid_column_states[:i]):
                if all(u != v for u, v in zip(x, y)):                       #If they don't have same colors in adjacent cells, append both to each other's adjacent states. 
                    adjacent_column_states[x].append(y)
                    adjacent_column_states[y].append(x)

        count = Counter(valid_column_states)                                #Count the number of painting ways for painting from the first column to current column where current column is at each column state.
        for _ in range(n - 1):                                              #Iterate n - 1 times.
            new_count = Counter()                                           #Initialize new counter.
            for current_state in valid_column_states:                       #Traverse current state.
                for next_state in adjacent_column_states[current_state]:    #Traverse the adjacent state of current state.
                    new_count[next_state] += count[current_state]           #Add count[current_state] to new_count[next_state].
                    new_count[next_state] %= division                       #Take modulo for new_count[next_state].
            count = new_count                                               #Replace count with new count.

        return sum(count.values()) % division                               #Sum of valies in count and take modulo then return.
