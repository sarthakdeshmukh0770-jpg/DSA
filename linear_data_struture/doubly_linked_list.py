class node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
class dll:
    def __init__(self):
        self.start=None
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,item):
        n=node(None,item,self.start)
        if self.start is not None:
            self.start.prev=n
        self.start=n
    def insert_at_last(self,item):
        n=node(None,item)
        if self.is_empty():
            self.start=n
            return
        temp=self.start
        while temp.next is not None:
            temp=temp.next
        temp.next=n
        n.prev=temp
    def insert_at_pos(self,pos,item):
        n=node(None,item)
        if pos<=0:
            return 'invalid position'
        temp=self.start
        if pos == 1:
            if temp is not None:
                self.start.prev=n
                n.next=self.start
            self.start=n
            return 
        for i in range (1,pos-1):
            if temp is None:
                return 'invalide postion'
            temp=temp.next
        if temp is None:
            return 'invalide position'
        n.prev=temp
        n.next=temp.next
        if temp.next is not None:
            n.next.prev=n
        temp.next=n
    def print_all(self):
        temp=self.start
        if self.is_empty():
            return 'list is empty'
        while temp is not None:
            print(temp.item)
            temp=temp.next
    def search(self,item):
        temp=self.start
        if self.is_empty():
            return 'list is empty '
        while temp is not None:
            if temp.item==item:
                return temp
            temp=temp.next
    def delete_at_first(self):
        if self.is_empty():
            return 'list is empty'
        if self.start.next is None:
            self.start=None
            return 
        self.start=self.start.next
        self.start.prev=None
    def delete_at_last(self):
        if self.is_empty():
            return 'list is empty'
        if self.start.next is None:
            self.start=None
            return 
        temp =self.start
        while temp.next is not None:
            temp=temp.next
        temp.prev.next=None
    def delete_at_pos(self,pos):
        if pos<=0:
            return 'invalid postion'
        temp=self.start
        if pos == 1:
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None
            return
        for i in range(1,pos):
            if temp is None:
                return 'invalid postion'
            temp=temp.next
        if temp is None:
            return 'invalid postion'
        if temp.next is not None:
            temp.next.prev=temp.prev
        temp.prev.next=temp.next
    def length(self):
        if self.is_empty():
            return 'list is empty'
        temp=self.start
        count=0
        while temp is not None:
            count+=1
            temp=temp.next
        return count
    def get_at_pos(self,pos):
        if pos<=0:
            return 'invalid position'
        if self.is_empty():
            return 'list is empty'
        temp=self.start
        for i in range(1,pos):
            if temp is None:
                return 'invalid postion'
            temp=temp.next
        if temp is None:
            return 'invalide postion'
        return temp.item
    def update_at_pos(self,pos,item):
        if pos<=0:
            return 'invalid position'
        if self.is_empty():
            return 'list is empty'
        temp=self.start
        for i in range(1,pos):
            if temp is None:
                return 'invalid position'
            temp=temp.next
        if temp is None:
            return 'invalid postion'
        temp.item=item
        return 'update succesfull'
    def count(self,item):
        if self.is_empty():
            return 'list is empty'
        temp=self.start
        count=0
        while temp is not None:
            if temp.item==item:
                count+=1
            temp=temp.next
        return count
    def find_first(self,item):
        if self.is_empty():
            return 'list is empty'
        temp=self.start
        index=1
        while temp is not None:
            if temp.item==item:
                return index
            index+=1
            temp=temp.next
        return 'item not in list'
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
            return 'item not found '
        return last_index
    def reverse(self):
        current = self.start
        temp = None

        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev   # move forward (via old 'next', now in prev)

        if temp is not None:
            self.start = temp.prev
    def sort_asc(self):
        temp=self.start
        while temp is not None:
            current=self.start
            while current.next is not None:
                if current.item>current.next.item:
                    current.item,current.next.item=current.next.item,current.item
                current=current.next 
            temp=temp.next
    def sort_desc(self):
        temp=self.start
        while temp is not None:
            current=self.start
            while current.next is not None:
                if current.item<current.next.item:
                    current.item,current.next.item=current.next.item,current.item
                current=current.next 
            temp=temp.next
    def remove_duplicated(self):
        temp=self.start
        while temp is not None:
            current=temp
            while current.next is not None:
                if temp.item==current.next.item:
                    current.next=current.next.next 
                    if current.next is not None:
                        current.next.prev = current
                else:
                    current = current.next
            temp=temp.next
        return 'remove duplicated' 
    def remove_duplicated_item(self,item): 
            if self.is_empty():
                return 'list is empty'
            temp=self.start
            #find first occurace of item 
            while temp is not None:
                if temp.item==item:
                   break
                temp=temp.next
            if temp is None:
                return 'item not in list '
            current=temp
            while current.next is not None:
                if current.next.item==item:
                    current.next=current.next.next
                    if current.next is not None:
                        current.next.prev = current
                else:
                    current=current.next
            return 'duplicated remove'

    
        
    


