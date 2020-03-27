from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    # THIS DOES NOT WORK
    def append(self, item):
        if len(self.storage) == self.capacity:
            # self.current = self.storage.head
            # print('current head', self.current.value)
            self.current = self.storage.tail.prev
            print('current tail', self.current.value)
            print('prev tail', self.current.prev.value)
            print('next tail', self.current.next.value)
            self.current.next.value = item
            self.current = self.current.next 
            # self.current = self.storage.tail.prev
        else:
            self.storage.add_to_head(item)
            
        # if len(self.storage) == self.capacity:
        #     print('current', self.current.value)
        #     self.current = self.storage.head
        #     self.storage.head = self.current
        #     print(self.current.value)
        # else:
        #     if self.current is None:
        #         self.storage.add_to_head(item)
        #         self.current = self.storage.head
        #     else:
        #         self.storage.add_to_tail(item)
        #         self.current = self.storage.tail
                # self.storage.head = self.storage.head.next
                # self.current = self.storage.head
    
    # THIS WORKS
    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        current = self.storage.tail

        while current:
            list_buffer_contents.append(current.value)
            current = current.prev
        
        return list_buffer_contents

# ----------------Stretch Goal-------------------


# class ArrayRingBuffer:
#     def __init__(self, capacity):
#         pass

#     def append(self, item):
#         pass

#     def get(self):
#         pass
