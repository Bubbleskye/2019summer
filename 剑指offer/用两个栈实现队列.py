class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):

        # write code here
        self.stack1.append(node)
    def pop(self):
        if self.stack2:
            return self.stack2.pop()
        else:
            while len(self.stack1)!=0:
                tmp=self.stack1.pop()
                self.stack2.append(tmp)
            return self.stack2.pop()