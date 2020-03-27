from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    # THIS DOES NOT WORK
    def append(self, item):
        if len(self.storage) == self.capacity:
            # If length is the capacity, then we do not add to head
            print(self.storage.tail.value)
            if self.current is None:
                # We need to see if self.current is none
                # If it is, set tail to the current value
                self.current = self.storage.tail
            self.current.value = item
            self.current = self.current.prev

            # self.current = self.storage.tail.prev
            # print('current tail', self.current.value)
            # print('prev tail', self.current.prev.value)
            # print('next tail', self.current.next.value)
            # self.current.next.value = item
            # print('current next', self.current.next.value)
            # print('prev next', self.current.next.prev.value)
            # self.storage.tail.prev = self.current.next
            # self.storage.tail.prev = self.current.next
            # self.current = self.storage.tail.prev
        else:
            self.storage.add_to_head(item)
            print('current head', self.storage.head.value)
            print('current tail', self.storage.tail.value)
            # This will set the tail to the last item
            
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
        list_buffer_contents.append(current.value)
        while current.prev:
            current = current.prev
            list_buffer_contents.append(current.value)
        print(list_buffer_contents)
        return list_buffer_contents

# ----------------Stretch Goal-------------------


# class ArrayRingBuffer:
#     def __init__(self, capacity):
#         pass

#     def append(self, item):
#         pass

#     def get(self):
#         pass
