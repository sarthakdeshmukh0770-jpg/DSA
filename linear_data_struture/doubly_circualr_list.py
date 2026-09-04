class node:

    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next


class DCll:

    def __init__(self):
        self.start=None
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,item):
        n=node(None,item,None)
        if self.is_empty():
            n.prev=n
            n.next=n
            self.start=n
            return
        n.next=self.start
        self.start.prev.next=n
        n.prev=self.start.prev
        self.start.prev=n
        self.start=n
    def insert_at_last(self,item):
        n=node(None,item,None)
        if self.is_empty():
            n.prev=n
            n.next=n
            self.start=n
            return
        n.next=self.start
        n.prev=self.start.prev
        self.start.prev.next=n
        self.start.prev=n
    def print_all(self):
        if self.is_empty():
            return 'list is empty'
        temp=self.start
        while temp.next is not self.start:
            print(temp.item)
            temp=temp.next
        print(temp.item)
    def search(self,item):
        if self.is_empty():
            return 'list is empty'
        temp=self.start
        while temp.next is not self.start:
            if temp.item==item:
                return temp
            temp=temp.next
        if temp.item==item:
            return temp
    def delete_at_start(self):
        if self.is_empty():
            return 'list is empty'
        if self.start.next is self.start:
            self.start=None
            return
        self.start.prev.next=self.start.next
        self.start.next.prev=self.start.prev
        self.start=self.start.next
    def delete_at_last(self):
        if self.is_empty():
            return 'list is empty'
        if self.start.next is self.start:
            self.start=None
            return 
        self.start.prev.prev.next=self.start
        self.start.prev=self.start.prev.prev
    def insert_at_pos(self,pos,item):
        n=node(None,item)
        if pos<=0:
            return 'invalid position'
        if pos==1:
            if self.is_empty():
                n.prev=n
                n.next=n
                self.start=n
                return
            n.next=self.start
            n.prev=self.start.prev
            self.start.prev.next=n
            self.start.prev=n
            self.start=n
            return 
        temp=self.start
        for i in range(1,pos-1):
            if temp.next is self.start:
                return 'invalid position' 
            temp=temp.next
        n.prev=temp
        n.next=temp.next
        temp.next.prev=n
        temp.next=n
    def delete_at_pos(self,pos):
        if self.is_empty():
            return 'list is empty'
        if pos<=0:
            return 'invalid position'
        if pos==1:
            if self.start.next is self.start:
                self.start=None
                return 
            self.start.prev.next=self.start.next
            self.start.next.prev=self.start.prev
            self.start=self.start.next
            return
        temp=self.start
        for i in range(1,pos-1):
            if temp.next is self.start:
                return 'invalid position'
            temp=temp.next
        temp.next=temp.next.next
        temp.next.prev=temp
    def print_desc(self):
        temp=self.start
        while temp.next is not self.start:
            temp=temp.next
        while temp.prev is not temp :
            print(temp.item)
            temp=temp.prev
        print(temp.item)
    def length(self):
        if self.is_empty():
            return 'list is empty'
        temp=self.start
        count=0
        while temp.next is not self.start:
            count+=1
            temp=temp.next
        count+=1
        return count 
    def get_pos(self,pos):
        if pos<=0:
            return 'invalid position'
        if self.is_empty():
            return 'list is empty'
        temp=self.start
        for i in range(1,pos):
            if temp.next is self.start:
                return 'invalid position'
            temp=temp.next
        return temp.item 
    


        



