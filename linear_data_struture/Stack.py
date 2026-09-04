class stack:
    def __init__(self):
        self.list=[]
    def is_empty(self):
        return len(self.list)==0
    def push(self,item):
        return self.list.append(item)
    def pop(self):
        if not self.is_empty():
            return self.list.pop()
        else:
            raise IndexError('list is empty')
    def peek(self):
        if not self.is_empty():
            return self.list[-1]
        else:
            raise IndexError('list i empty')
    def size(self):
        return len(self.list)

# driver code

a1=stack()
print(a1.is_empty())
a1.push(10)
a1.push(20)
a1.push(30)
a1.pop()
print(a1.peek())
print(a1.size())
print(a1.is_empty())
