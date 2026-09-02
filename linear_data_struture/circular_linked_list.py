class node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class Cll:
    def __init__(self):
        self.last=None
    def is_empty(self):
        return self.last==None
    def insert_at_start(self,item):
        n=node(item,None)
        if self.last is not None:
            n.next=self.last.next
            self.last.next=n
        else: 
            n.next=n
            self.last=n
    def insert_at_last(self,item):
        n=node(item,None)
        if  self.last is not None:
            n.next=self.last.next
            self.last.next=n
            self.last=n
        else:
            n.next=n
            self.last=n
        
    def delete_at_first(self):
            if self.is_empty():
                return 'list is empty'
            if self.last.next==self.last:
                self.last=None
            else:
                self.last.next=self.last.next.next

    def delete_at_last(self):
        if self.is_empty():
            return 'list is empty'
        if self.last.next==self.last:
             self.last=None
             return
        temp=self.last
        while temp.next!=self.last :
            temp=temp.next
        temp.next=self.last.next
        self.last=temp
    def search(self,item):
        if self.is_empty():
            return 'list is empty'
        temp=self.last.next
        while temp is not self.last:
            if temp.item==item:
                return temp
            temp=temp.next
        if temp.item==item:
            return temp
        return 'item not found' 
    def print_all(self):
        if self.is_empty():
            return 'list is empty'
        temp=self.last.next
        while temp is not self.last:
            print(temp.item)
            temp=temp.next
        print(temp.item)
    def insert_at_pos(self,pos,item):
        n=node(item,None)
        if self.is_empty():
            return 'list is empty'
        if pos<=0:
            return 'invalid position'
        if pos==1:
                n.next=self.last.next
                self.last.next=n
                return 
        temp=self.last.next
        for i in range(1,pos-1):
            if temp is self.last:
                return 'invalid position'
            temp=temp.next
        if temp is self.last:
            return 'invalid position'
        n.next=temp.next
        temp.next=n
    def delete_at_pos(self,pos):
        if self.is_empty():
            return 'list is empty'
        if pos<=0:
            return 'invalid position'
        temp=self.last.next
        if pos==1:
            if temp.next is self.last:
                self.last=None
            else:
                self.last.next=temp.next
            return 
        for i in range(1,pos-1):
            if temp is self.last:
                return 'invalid position'
            temp=temp.next
        if temp is self.last:
            return 'invalid position'
        if temp.next is self.last:
            self.last=temp
        temp.next=temp.next.next
    def length(self):
        if self.is_empty():
            return 'list is empty'
        temp=self.last.next
        count=0
        while temp is not self.last:
            count+=1
            temp=temp.next
        count+=1
        return count
    def get_at_postion(self,pos):
        if self.is_empty():
            return 'list is empty'
        if pos<=0:
            return 'invalid postion'
        if pos==1:
            return self.last.next.item
        temp =self.last.next
        for i in range (1,pos):
            if temp is self.last:
                return 'invalid postion'
            temp=temp.next
        return temp.item
    def update_at_pos(self,pos,item):
        if self.is_empty():
            return 'list is empty'
        if pos<=0:
            return 'invalid postion'
        if self.last.next is self.last and pos ==1:
            self.last.item=item
            return
        temp=self.last.next
        for i in range(1,pos):
            if temp  is self.last:
                return 'invalid postion'
            temp=temp.next
        temp.item=item
    def count(self,item):
        if self.is_empty():
            return 'list is empty'
        count=0
        temp=self.last.next
        while temp is not self.last:
            if temp.item==item:
                count+=1
            temp=temp.next
        if temp.item==item:
            count+=1
        return count
    def find_first(self,item):
        if self.is_empty():
            return 'list is empty'
        index=0
        temp=self.last.next
        while temp is not self.last:
            if temp.item==item:
                return index
            index+=1
            temp=temp.next
        if temp.item==item:
            return index
        return 'item not found'
    def find_last(self,item):
        if self.is_empty():
            return 'list is empty'
        count=0
        last_index=-1
        temp=self.last.next
        while temp is not self.last:
            if temp.item==item:
                last_index=count
            count+=1
            temp=temp.next
        if temp.item==item:
            last_index=count
        return last_index
    
        

# driver code
# cll=Cll()
# cll.is_empty()
# cll.insert_at_start(10)
# cll.insert_at_last(50)
# cll.insert_at_pos(2,40)
# cll.insert_at_last(40)
# # cll.print_all()
# # cll.delete_at_first()
# # cll.delete_at_last()
# # cll.delete_at_pos(3)
# # print(cll.count(10))
# # cll.print_all()
# # print(cll.find_first(40))
# # print(cll.find_last(40))
# # print(cll.length())
# cll.update_at_pos(2,90)
# cll.print_all()
        





