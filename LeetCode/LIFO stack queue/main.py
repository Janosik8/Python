class MyStack:

    def __init__(self):
        self.q = []

    def push(self, x: int) -> None:
        local_q = [x]
        if self.q.__contains__(x):
            self.q.remove(x)

        for i in range(len(self.q)):
            local_q.append(self.q[i])
        self.q = local_q

    def pop(self) -> int:
        return self.q.pop(0)

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        if self.q == []:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
param_3 = obj.top
param_2 = obj.pop()
param_4 = obj.empty()


