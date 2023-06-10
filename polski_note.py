"""This code is release of Polski notation calculator."""


class EmptyException(Exception):
    """Exception class for empty stack."""


class Stack:
    """Stack class."""

    def __init__(self):
        """Stack initial conditions."""
        self.__queue = []
        self.__size = 0

    @property
    def is_empty(self):
        """Check if stack is empty or not."""
        return self.__size == 0

    def push(self, item):
        """Add item to queue."""
        self.__size = self.__size + 1
        self.__queue.append(item)

    def pop(self):
        """Remove item from queue."""
        if self.is_empty:
            raise EmptyException
        self.size = self.__size - 1
        return self.__queue.pop()


def main():
    """Input & Output main function and dictionary."""
    stack = Stack()
    actions = {
        '*': lambda fd, ld: fd * ld,
        '/': lambda fd, ld: ld // fd,
        '+': lambda fd, ld: fd + ld,
        '-': lambda fd, ld: ld - fd
    }
    item = input().split(' ')
    for symbol in item:
        operation = actions.get(symbol)
        if operation:
            fd = stack.pop()
            ld = stack.pop()
            result = operation(fd, ld)
            stack.push(result)
        else:
            stack.push(int(symbol))
    print(stack.pop())


if __name__ == '__main__':
    main()
