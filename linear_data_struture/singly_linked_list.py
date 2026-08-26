class node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class sll:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,item):
        n=node(item,self.start)
        self.start=n
    def insert_at_last(self,item):
        n=node(item)
        if self.is_empty():
            self.start=n
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
    def print_list(self):
        temp=self.start
        if self.is_empty():
            return "list is empty"
        while temp is not None:
            print(temp.item)
            temp=temp.next
    def insert_at_pos(self,item,pos):
        n=node(item)
        if pos<=0:
            return 'invalid position'
        if pos == 1:
            n.next=self.start
            self.start=n
            return 
        temp=self.start
        for i in range(1,pos-1):
            if temp is None:
                return 'invalid postion'
            temp=temp.next
        if temp is None:
            return 'invalid postion' 
        n.next=temp.next
        temp.next=n
    def search(self,item):
        if self.is_empty():
            return 'list is empty'
        temp=self.start
        while temp is not None:
            if temp.item==item:
                return item
            temp=temp.next
        return 'item not found'
    def delete_at_first(self):
        if self.is_empty():
            return 'list is empty'
        self.start=self.start.next
    def delete_at_last(self):
        if self.is_empty():
            return 'list is empty'
        if self.start.next == None:
            self.start=None
            return 
        temp=self.start
        while temp.next.next is not None:
            temp=temp.next
        temp.next=None
    def delete_at_pos(self,pos):
        if pos<=0:
            return 'invalid postion'
        if self.is_empty():
            return 'list is empty'
        if pos == 1:
            self.start=self.start.next
            return
        temp=self.start
        for i in range (1,pos -1):
            if temp is None:
                return 'invalid position'
            temp=temp.next
        if temp is None or temp.next is None :
            return 'invalid postion'
        temp.next=temp.next.next
    def length(self):
        if self.is_empty():
            return 0 
        count=0
        temp=self.start
        while temp is not None:
            count+=1
            temp=temp.next
        return count 
    def get_at_pos(self,pos):
        if pos<=0:
            return 'invalid postion'
        if self.is_empty():
            return 'list is empty'
        temp=self.start
        for i in range(1,pos):
            if temp is None:
                return 'invalid postion'
            temp=temp.next
        if temp is None:
            return 'invalid postion'
        return temp.item
    def update_at_pos(self,pos,item):
        if pos<=0:
            return 'invalid position'
        if self.is_empty():
            return 'list is empty'
        temp =self.start
        for i in range (1,pos):
            if temp is None:
                return 'invalid postion'
            temp=temp.next
        if temp is None :
            return 'invalid position'
        temp.item=item
        return 'update successfull'
    def count(self,item):
        if self.is_empty():
            return 'list is empty'
        temp=self.start
        count=0
        while temp is not None:
            if  temp.item==item:
                count+=1
            temp=temp.next
        return count 
    def find_first(self,item):
        if self.is_empty():
            return 'list is empty'
        index=1
        temp=self.start
        while temp is not None:
            if temp.item==item:
                return index 
            index+=1
            temp=temp.next
        return 'item not found'
    def find_last(self,item):
        if self.is_empty():
            return 'list is empty'
        temp=self.start
        index=1
        last_index=0
        while temp is not None:
            if temp.item==item:
                last_index=index
            index+=1
            temp=temp.next
        if last_index==0:
            return 'item not found'
        return last_index 
    def reverse(self):
        prev=None
        temp =self.start
        while temp is not None:
            next_node=temp.next
            temp.next=prev
            prev=temp
            temp=next_node
        self.start=prev 
    def sort_asc(self):
        if self.is_empty():
            return 'list is empty'
        temp=self.start
        while temp is not None:
            current=self.start
            while current.next is not None:
                if current.item > current.next.item:
                    current.item,current.next.item=current.next.item,current.item
                current=current.next 
            temp=temp.next
    def sort_dec(self):
        if self.is_empty():
            return 'list is empty'
        temp=self.start
        while temp is not None:
            current=self.start
            while current.next is not None:
                if current.item < current.next.item:
                    current.item,current.next.item=current.next.item,current.item
                current=current.next 
            temp=temp.next
   
#testing the sll 

# s1=sll()

# s1.insert_at_start(100)
# s1.insert_at_start(50)
# s1.insert_at_last(12)
# s1.insert_at_pos(90,1)
# s1.is_empty()
# print(s1.search(100))
# s1.print_list()
# s1.delete_at_first()
# s1.delete_at_last()
# s1.delete_at_pos(2)
# s1.print_list()
# print(s1.length())
# print(s1.get_at_pos(1))
# s1.update_at_pos(1,99)
# s1.insert_at_last(50)
# print(s1.count(50))
# s1.print_list()
# print(s1.find_first(50))
# print(s1.find_last(50))
# s1.reverse()
# s1.sort()
# s1.sort_dec()
# s1.print_list()
