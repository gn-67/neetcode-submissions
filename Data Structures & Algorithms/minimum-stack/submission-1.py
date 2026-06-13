class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            cmin = val
            self.stack.append((val, cmin))
            return

        if val < self.stack[-1][1]:
            cmin = val
            self.stack.append((val, cmin))
        else:
            cmin = self.stack[-1][1]
            self.stack.append((val,cmin))
            

        #if val is less than cmin, cmin = val
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        
