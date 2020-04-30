class Array:
    DEFAULT_SIZE = 6
    DEFAULT_VALUE = "Tutorial"

    def __init__(self, size=DEFAULT_SIZE, default_value=DEFAULT_VALUE):
        """Constructor for Array class"""
        self._size = size
        self._data = [default_value for _ in range(self._size)]
        self._default = default_value

    def __setitem__(self, index, item_to_set):
        """Overload [] to allow changing an array item."""
        if not self.valid_index(index):
            raise IndexError
        elif not isinstance(item_to_set, type(self.DEFAULT_VALUE)):
            raise TypeError
        self._data[index] = item_to_set
        return True

    def __getitem__(self, index):
        """Overload [] to allow fetching an array item."""
        if not self.valid_index(index):
            raise IndexError
        # else
        return self._data[index]

    def valid_index(self, test_index):
        """Helper function to check if an index is valid."""
        if not (0 <= test_index < self._size):
            return False
        else:
            return True

    def next_unassigned_index(self):
        """Return the next index that can be used."""
        i = 0
        while self._data[i] != self._default:
            i += 1
        return i

    def __len__(self):
        """Overload len() to allow getting the length of the array."""
        return len(self._data)

    def __str__(self):
        # return_str = "Enrolled classes:\n"
        return_str = ""
        for i in range(len(self._data) - 1):
            return_str += f"{self._data[i]}, "
        return_str += self._data[-1]
        return return_str

"""
classes = Array(6, "Tutorial")
# classes = Array(default_value="Tutorial")
# classes = Array()
print(f"Before adding classes:")
print(classes)
try:
    classes[0] = "Biology"
    classes[1] = "Math Analysis"
    classes[2] = "Spanish"
    classes[3] = "English"
    classes[5] = "CS 3A"
except IndexError:
    print("Failed to add a class. Check period numbers.")
except TypeError:
    print("Failed to add a class. Class must be a string.")
print(f"\nAfter adding classes:")
print(classes)

try:
    print(f"\nLast class is {classes[len(classes) - 1]}")
except IndexError:
    print("Failed to get the last class item. Check index.")
"""
