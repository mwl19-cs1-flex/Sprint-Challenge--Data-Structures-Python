from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    # THIS DOES NOT WORK
    def append(self, item):
        if len(self.storage) == self.capacity:
            node = self.current
            self.storage.delete(node)
            self.storage.add_to_head(item)
            self.current = self.storage.head
        else:
            if self.current is None:
                self.storage.add_to_head(item)
                self.current = self.storage.head
            else:
                self.storage.add_to_tail(item)
                self.current = self.storage.tail
                # self.storage.head = self.storage.head.next
                # self.current = self.storage.head

    # THIS WORKS
    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        self.current = self.storage.head
        current = self.current
        while current:
            list_buffer_contents.append(current.value)
            current = current.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


# class ArrayRingBuffer:
#     def __init__(self, capacity):
#         pass

#     def append(self, item):
#         pass

#     def get(self):
#         pass
