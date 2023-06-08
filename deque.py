# 87250890
"""This code is a deque release."""


class EmptyQueue(Exception):
    """Exception class for empty deque."""


class OccupiedQueue(Exception):
    """Exception class for full deque."""


class TwoWaysDeque:
    """Deque class."""

    def __init__(self, max_size):
        """Deque initial conditions."""
        self.__queue = [None] * max_size
        self.__max_size = max_size
        self.__head = 0
        self.__tail = 0
        self.__size = 0

    def push_back(self, item):
        """Add item to back-end."""
        if self.is_full():  # без not, т.к. def is_full(self) подкорректировал
            raise OccupiedQueue
        self.__queue[self.__tail] = item
        self.__tail = (self.__tail + 1) % self.__max_size
        self.__size = self.__size + 1

    def push_front(self, item):
        """Add item to front-end."""
        if self.is_full():  # без not, т.к. def is_full(self) подкорректировал
            raise OccupiedQueue
        self.__queue[self.__head - 1] = item
        self.__head = (self.__head - 1) % self.__max_size
        self.__size = self.__size + 1

    def pop_front(self):
        """Remove item from front-end."""
        if self.is_empty():
            raise EmptyQueue
        item = self.__queue[self.__head]
        self.__queue[self.__head] = None
        self.__head = (self.__head + 1) % self.__max_size
        self.__size = self.__size - 1
        return item

    def pop_back(self):
        """Remove item fro back-end."""
        if self.is_empty():
            raise EmptyQueue
        item = self.__queue[self.__tail - 1]
        self.__queue[self.__tail - 1] = None
        self.__tail = (self.__tail - 1) % self.__max_size
        self.__size = self.__size - 1
        return item

    def is_empty(self):
        """Check if deque is empty or not."""
        return self.__size == 0

    def is_full(self):
        """Check if deque is full or not."""
        return self.__size == self.__max_size


def main():
    """Input & Output main function."""
    operations = int(input())
    max_size = int(input())
    deque = TwoWaysDeque(max_size)
    for _ in range(operations):
        try:
            command, *arg = input().split()
            method = getattr(deque, command)
            if arg:
                method(*arg)  # необычно просто, но подзадумался..
            else:
                print(method(*arg))  # здесь без else не проходит
        except (EmptyQueue, OccupiedQueue):
            print('error')


if __name__ == '__main__':
    main()
