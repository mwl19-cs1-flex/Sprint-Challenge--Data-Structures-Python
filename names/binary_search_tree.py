import sys
sys.path.append('../queue_and_stack')

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        if target >= self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

### COOL IDEAS BUT HEY THIS WON'T WORK
# import sys
# sys.path.append('../queue_and_stack')

# class BinarySearchTree:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

#     def insert(self, value):
#         if value < self.value:
#             if self.left is None:
#                 self.left = BinarySearchTree(value)
#             else:
#                 self.left.insert(value)
#         else:
#             if self.right is None:
#                 self.right = BinarySearchTree(value)
#             else:
#                 self.right.insert(value)

#     def contains(self, target):
#         if target.value == self.value:
#             return True
#         if target.value < self.value:
#             if self.left is None:
#                 return False
#             if target.left is None:
#                 return false
#             else:
#                 return self.left.contains(target.left)
#         if target.value >= self.value:
#             if self.right is None:
#                 return False
#             if target.right is None:
#                 return False
#             else:
#                 return self.right.contains(target.right)

#     def get_max(self):
#         if self.right:
#             return self.right.get_max()
#         else:
#             return self.value

#     def for_each(self, cb, bst):
#         cb(self.value, bst.value)

#         if self.left and bst.left != None:
#             self.left.for_each(cb, bst.left)
#         if self.right and bst.right != None:
#             self.right.for_each(cb, bst.right)
#         if bst.left and self.left != None:
#             bst.left.for_each(cb, bst.left)
#         if bst.right and self.right != None:
#             bst.right.for_each(cb, bst.right)
