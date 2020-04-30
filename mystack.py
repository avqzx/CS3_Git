class MyStack:
    # class ("static") members and intended constants
    MAX_CAPACITY = 1000
    DEFAULT_CAPACITY = 10
    DEFAULT_VALUE = ""

    # initializer ("constructor") method -------------------
    def __init__(self, capacity=DEFAULT_CAPACITY, default_value=DEFAULT_VALUE):

        # instance attributes
        self._default = default_value
        self._capacity = min(capacity, self.MAX_CAPACITY)

        # set up the stack of given capacity with default values
        # self.clear()
        self._data = [self._default for _ in range(self._capacity)]
        self._tos = 0
        # print(f"\tConstructor: tos = {self._tos}, data = {self._data}")

    # accessors -------------------------------
    @property
    def capacity(self):
        return self._capacity

    # mutators -------------------------------
    @capacity.setter
    def capacity(self, new_capacity):
        if new_capacity > self.MAX_CAPACITY or new_capacity <= self._capacity:
            raise ValueError
        for i in range(self._capacity, new_capacity):
            self._data.append(self._default)
        self._capacity = new_capacity
        # print(f"\tCapacity setter: tos = {self._tos}, data = {self._data}")
        # self.clear()

    # instance methods -----------------------

    def push(self, item_to_push):
        if self._tos == self.capacity:
            raise OverflowError
        elif not isinstance(item_to_push, type(self._default)):
            raise TypeError

        self._data[self._tos] = item_to_push
        self._tos += 1
        # print(f"\tPush: tos = {self._tos}, data = {self._data}")

    def pop(self):
        if self._tos == 0:
            raise IndexError
        self._tos -= 1
        # print(f"\tPop: tos = {self._tos}, data = {self._data}")
        return self._data[self._tos]

    # def clear(self):
    #     """  remove all items from stack """
    #     # deepcopy() for mutable defaults - details in cs 3B/3M
    #     # self.stk = [copy.deepcopy(self.default_item)
    #     #             for _ in range(self.capacity)]
    #     self._data = [self._default for _ in range(self.capacity)]
    #     self._tos = 0

    def __str__(self):
        return_str = ""
        for i in range(self._tos):
            return_str += f"'{self._data[i]}' "
        return return_str

    def __len__(self):
        return self._tos


# client --------------------------------------------

def main():
    books = MyStack(5, "None")
    status(f"After initialization", books)

    books.push("Walden")
    books.push("What I believe")
    books.push("The Republic")
    books.push("Mindset")
    books.push("Factfulness")
    status("After pushing 5 books", books)

    try:
        books.push("Permanent Record")
    except OverflowError:
        print(f"\n*** Expected Error: Failed to push another book ***")

    item = books.pop()
    status(f"After popping '{item}'", books)

    new_book = "Sapiens"
    books.push(new_book)
    status(f"After pushing '{new_book}'", books)

    capacities = [10000, 10]
    for new_capacity in capacities:
        try:
            books.capacity = new_capacity
            status(f"After re-sizing to capacity {new_capacity}", books)
        except ValueError:
            status(f"*** Failed to set capacity to {new_capacity} ", books)

    try:
        books.push("Permanent Record")
        books.push("Enlightenment Now")
        books.push("Future")
        status("After pushing 3 more books", books)
    except OverflowError:
        status("Failed to push 3 more books", books)


def status(prefix, books):
    print(f"\n{prefix}: Length = {len(books)}, Capacity = {books.capacity}"
          f"\nStack has [ {books}]")


def fh_test():
    # instantiate two empty stacks, one of 50 ints, another of 15 strings
    s1 = Stack(50, -1)
    s2 = Stack(15, "undefined")
    # and one more with bad argument
    s3 = Stack(-100)

    # confirm the stack capacities
    print(f"------ Stack Sizes -------\n"
          f"  s1: {s1.capacity}   s2: {s2.capacity}   s3: {s3.capacity}\n")

    # test the stack -----
    try:
        print(s1.pop())
    except IndexError:
        print("Tried to pop from an empty stack")
    print()

    s1.push(44)
    s1.push(123)
    s1.push(99)
    s2.push("bank")
    s2.push("-34")
    s1.push(10)
    s1.push(1000)

    # try to put a square peg into a round hole
    try:
        s1.push("should not be allowed into an int statck")
    except TypeError:
        print("Successfully rejected a String from s1 - type incompatibility")

    try:
        s2.push(444)
    except TypeError:
        print("Successfully rejected 444 from s2 - type incompatibility")

    try:
        s1.push(44.4)
    except TypeError:
        print("Successfully rejected 44.4 from s1 - type incompatibility")

    # and here test return type if good argument
    s2.push("should be okay")
    print("Successfully accepted a good type")

    s2.push("a penny earned")
    s2.push("item #9277")
    s2.push("where am i?")
    s2.push("4")

    print("\n--------- First Stack ---------\n")
    for k in range(0, 10):
        try:
            print("[" + str(s1.pop()) + "]")
        except IndexError:
            print("Tried to pop from an empty stack")

    print("\n--------- Second Stack ---------\n")
    for k in range(0, 10):
        try:
            print("[" + str(s2.pop()) + "]")
        except IndexError:
            print("Tried to pop from an empty stack")


if __name__ == '__main__':
    main()
