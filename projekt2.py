from typing import Any, Callable

class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def is_leaf(self):
        if self.left_child or self.right_child:
            return False
        return True

    def add_left_child(self, value: Any):
        if self.left_child is None:
            self.left_child = value

    def add_right_child(self, value: Any):
        if self.right_child is None:
            self.right_child = value

    def traverse_in_order(self, visit: Callable[[Any], None]):
        if self.left_child:
            self.left_child.traverse_in_order(visit)

        visit(self)

        if self.right_child:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        if self.left_child:
            self.left_child.traverse_post_order(visit)

        if self.right_child:
            self.right_child.traverse_post_order(visit)

        visit(self)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        visit(self)

        if self.left_child:
            self.left_child.traverse_pre_order(visit)

        if self.right_child:
            self.right_child.traverse_pre_order(visit)

    def print(self):
        return self.value


class BinaryTree:
    root: BinaryNode

    def __init__(self, root):
        self.root = root

    def traverse_in_order(self, visit: Callable[[Any], None]):
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        self.root.traverse_pre_order(visit)


def check_level(tree: BinaryTree, first_node: BinaryNode, second_node: BinaryNode) -> BinaryNode:
    def level(node, value, lvl):
        if node == None:
            return 0
        if node.value == value:
            return lvl
        deeper = level(node.left_child, value, lvl + 1)
        if deeper != 0:
            return deeper
        deeper = level(node.right_child, value, lvl + 1)
        return deeper

    first_node = level(tree.root, first_node.value, 1)
    second_node = level(tree.root, second_node.value, 1)
    if first_node == second_node:
        return True
    return False

def printed(node: 'BinaryNode'):
    print(node.value)

w1 = BinaryNode(1)
w2 = BinaryNode(2)
w3 = BinaryNode(3)
w4 = BinaryNode(4)
w5 = BinaryNode(5)
w7 = BinaryNode(7)
w8 = BinaryNode(8)
w9 = BinaryNode(9)
# poziom1
tree = BinaryTree(w1)
# poziom2
w1.add_left_child(w2)
w1.add_right_child(w3)
# poziom3
w2.add_left_child(w4)
w2.add_right_child(w5)
w3.add_right_child(w7)
# poziom4
w4.add_left_child(w8)
w4.add_right_child(w9)

assert tree.root.value == 1
assert tree.root.left_child.left_child.left_child.value == 8
# tree.traverse_in_order(printed)
# print("")
# tree.traverse_pre_order(printed)
# print("Dla węzła 4 i 4:", check_level(tree, w4, w4))
print("Dla węzła 8 i 5:", check_level(tree, w8, w5))
print("Dla węzła 9 i 7:", check_level(tree, w9, w7))
print("Dla węzła 4 i 7:", check_level(tree, w4, w7))
print("Dla węzła 2 i 3:", check_level(tree, w2, w3))
