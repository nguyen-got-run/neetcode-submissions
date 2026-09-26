import numbers

class MinStack:

    def __init__(self):
        self.stack = []
        self.minHistory = []

    def push(self, val: int) -> None:
        if not isinstance(val, numbers.Number):
            self.stack.append(null)
        else:
            self.stack.append(val)
            
            if len(self.minHistory):
                lastMin = self.minHistory[-1]
                self.minHistory.append(min(val, lastMin))
            else:
                self.minHistory.append(val)

    def pop(self) -> None:       
        self.stack.pop()
        self.minHistory.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minHistory[-1]
        
