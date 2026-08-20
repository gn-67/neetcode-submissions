class MinStack:

    #each function needs to run in O(1) time
    #so we can append two values for each element, the value and the current minimum

    def __init__(self):
        self.stack = []

        

    def push(self, val: int) -> None:
        if len(self.stack) == 0 or val < self.stack[-1][1]:
            curMin = val
            self.stack.append([val, curMin])

        else:
            curMin = self.stack[-1][1]
            self.stack.append([val, curMin])


    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

        

    def getMin(self) -> int:
        return self.stack[-1][1]
        
        
