class MyQueue:
    DEFAULT_CAPACITY = 6
    DEFAULT_VALUE = -1

    def __init__(self, capacity=DEFAULT_CAPACITY, default_value=DEFAULT_VALUE):
        """Constructor for Queue class"""
        self._capacity = capacity
        self._queue = [default_value for _ in range(self._capacity)]
        self._head = 0  # indicates empty queue
        self._tail = 0
        self._num_items = 0

    def add(self, item):
        """Add an item to tail of the queue."""
        if self.is_full():
            raise OverflowError
        elif not isinstance(item, type(self.DEFAULT_VALUE)):
            raise TypeError
        self._queue[self._tail] = item
        self._num_items += 1
        self._tail += 1
        # if we reached the end, check if there's room at the beginning
        if self._tail == self._capacity:
            self._tail = 0

    def remove(self):
        """Remove an item from the head of the queue."""
        if self.is_empty():
            raise IndexError
        # else
        item = self._queue[self._head]
        self._num_items -= 1
        self._head += 1
        if self._head == self._capacity:
            self._tail = 0
        return item

    def is_empty(self):
        # return self._head == self._tail
        return self._num_items == 0

    def is_full(self):
        # return abs(self._head - self._tail) == self._capacity
        return self._num_items == self._capacity

    def __str__(self):
        # return_str = "Enrolled classes:\n"
        return_str = "[ "
        next_index = self._head
        for _ in range(self._num_items):
            return_str += f"{self._queue[next_index]} "
            next_index += 1
            if next_index == self._capacity:
                next_index = 0
        return_str += "]"
        return return_str


def main():
    num_queue = MyQueue()
    print(f"Before adding nums:")
    print(num_queue)

    for i in range(num_queue.DEFAULT_CAPACITY):
        num_queue.add((i + 1) * 10)
    print(f"After adding:")
    print(num_queue)
    print()

    for i in range(num_queue.DEFAULT_CAPACITY // 2):
        num = num_queue.remove()
        print(f"After removing one item:")
        print(num_queue)

    # for i in range(num_queue.DEFAULT_CAPACITY // 2):
    num_queue.add(100)
    print(f"\n After adding 100:")
    print(num_queue)

    num = num_queue.remove()
    print(f"After removing one item:")
    print(num_queue)

    # try:
    #     num_queue[0] = "Biology"
    #     num_queue[1] = "Math Analysis"
    #     num_queue[2] = "Spanish"
    #     num_queue[3] = "English"
    #     num_queue[5] = "CS 3A"
    # except IndexError:
    #     print("Failed to add a class. Check period numbers.")
    # except TypeError:
    #     print("Failed to add a class. Class must be a string.")
    # print(f"\nAfter adding classes:")
    # print(num_queue)
    #
    # try:
    #     print(f"\nLast class is {num_queue[len(num_queue) - 1]}")
    # except IndexError:
    #     print("Failed to get the last class item. Check index.")


if __name__ == '__main__':
    main()