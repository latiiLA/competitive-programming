class ListNode:
    def __init__(self, value, prev = None):
        self.value = value
        self.prev = prev
        self.next = None
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = ListNode(homepage)

    def visit(self, url: str) -> None:
        self.history.next = ListNode(url, self.history)
        self.history = self.history.next

    def back(self, steps: int) -> str:
        while self.history.prev and steps > 0:
            steps -= 1
            self.history = self.history.prev
        return self.history.value
        
    def forward(self, steps: int) -> str:
        while self.history.next and steps > 0:
            steps -= 1
            self.history = self.history.next
        
        return self.history.value
        
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)