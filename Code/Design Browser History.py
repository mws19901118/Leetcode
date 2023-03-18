class BrowserHistory:

    def __init__(self, homepage: str):
        self.index = 0                                                          #Initialize the current index and limit both at 0.
        self.limit = 0
        self.stack = [homepage]                                                 #Push homepage to stack.

    def visit(self, url: str) -> None:
        if self.index == len(self.stack) - 1:                                   #If current index is at the end of stack, push an empty string to stack.
            self.stack.append('')
        self.stack[self.index + 1] = url                                        #Put url at self.index + 1.
        self.index += 1                                                         #Update index and limit.
        self.limit = self.index

    def back(self, steps: int) -> str:
        self.index = max(0, self.index - steps)                                 #Move index back, at most to 0.
        return self.stack[self.index]                                           #Return url at current index.

    def forward(self, steps: int) -> str:
        self.index = min(self.limit, self.index + steps)                        #Move index forward, at most to limit.
        return self.stack[self.index]                                           #Return url at current index.


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
