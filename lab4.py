from typing import Any, List

class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value = None):
        self.value = value
        self.children = []

    def is_leaf(self) -> bool:
        if self.children == 0:
            return False
        else:
            return True

    def add(self, child: 'TreeNode') -> None:
        self.children.append(child)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)

        for child in self.children:
            self.for_each_deep_first(visit)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)

        kolejka_fifo = self.children
        while len(kolejka_fifo):
            print(kolejka_fifo[0])
            kolejka_fifo += kolejka_fifo[0]

        del kolejka_fifo[0]

    def search(self, value: Any) -> Union['TreeNode', None]:
        if self.value == value:
            return self

        wezel = None
        for child in self.children:
            dziecko = child.search(value)

            if dziecko:
                wezel = dziecko

        return wezel

    def print(self):
        return self.value