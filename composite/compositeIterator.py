from menuComponentIterator import MenuComponentIterator


class CompositeIterator:
    def __init__(self, iterator):
        # type: (MenuComponentIterator) -> None
        self.stack = []
        self.stack.append(iterator)

    def next(self):
        if self.hasNext():
            iterator = self.stack[-1]
            component = iterator.next()
            from menu import Menu
            if isinstance(component, Menu):
                self.stack.append(component.createIterator())
            return component
        else:
            return None

    def hasNext(self):
        if not self.stack:
            return False
        else:
            iterator = self.stack[-1]
            if not iterator.hasNext():
                self.stack.remove(iterator)
                return self.hasNext()
            else:
                return True


