# stack by inherit list class 

class Stack(list):
    def is_empty(self):
        return len(self)==0
    def push(self,item):
        return self.append(item)
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError('list is empty')
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError('list is empty')
    def size(self):
        return len(self)
    def insert(self,pos,item):
        raise AttributeError('no attribute insert')

# driver code 
a1=Stack()
a1.push(10)
a1.push(20)
a1.push(30)
a1.pop()
print(a1.peek())
print(a1.size())
a1.insert(0,89)
    