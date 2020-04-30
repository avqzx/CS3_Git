# import copy
from array import Array
from mystack import MyStack


class Student:
    # class constants aka class intended constants
    DEFAULT_NAME = "No Name"
    NAME_LEN_MAX = 16
    ORIGINAL_DEFAULT_YEAR = 0
    MIN_YEAR = 0
    MAX_YEAR = 12
    # DEFAULT_APT_NUM = Address.DEFAULT_APT_NUM

    # class variables aka class attributes
    next_id = 1
    default_year = ORIGINAL_DEFAULT_YEAR

    def __init__(self, name=DEFAULT_NAME, year=None):
        """Constructor for Student."""
        # print(f"init: name = {name}, year = {year}")
        if year is None:
            year = self.default_year
            # print(f"init updated: name = {name}, year = {year}")

        # if type(name) is str:
        #     self._name = name
        # else:
        #     self._name = self.DEFAULT_NAME
        try:
            self.name = name
        except ValueError:
            print(f"init: failed to set self.name to {name}."
                  f" Setting _name to {self.DEFAULT_NAME}")
            self._name = self.DEFAULT_NAME

        try:
            self.year = year
        except ValueError:
            print(f"init: failed to set self.year to {year}."
                  f" Setting _year to 0")
            self._year = 0

        # no exception handling needed below because we're using default values
        self._phone = self.Phone()
        self._address = self.Address()
        self._classes = Array()
        self._advisors = MyStack(5, "Unassigned")
        self._birth_date = self.Date()

        self._id = self.next_id
        self.update_next_id()

    @property
    def name(self):
        """Get or set the name of this student."""
        return self._name

    @name.setter
    def name(self, new_name):
        if len(new_name) > self.NAME_LEN_MAX:
            raise ValueError
        self._name = new_name

    @property
    def year(self):
        """Get or set the grade level of this student."""
        return self._year

    @year.setter
    def year(self, new_year):
        if not self.valid_year(new_year):
            # raise ValueError(f"Invalid year {new_year}")
            raise ValueError
        # else
        self._year = new_year

    @property
    def phone(self):
        return str(self._phone)

    @phone.setter
    def phone(self, new_ph_num):
        self._phone.number = new_ph_num
        # valid_num = self._phone.get_valid_num(new_ph_num)
        # if valid_num is None:
        #     raise ValueError
        # self._phone.number = valid_num

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, new_birth_date):
        self._birth_date.date = new_birth_date

    @property
    def address(self):
        return str(self._address)

    @address.setter
    def address(self, new_address):
        # new_house_num, new_street, new_apt_num = new_address
        # self._address.house_number = new_house_num
        # self._address.street = new_street
        # self._address.apt_num = new_apt_num
        parts = new_address.split()
        # print(parts)
        self._address.house_number = int(parts[0])
        self._address.street = parts[1] + " " + parts[2]
        self._address.apt_num = int(parts[-1])

    @property
    def classes(self):
        """Get or set the classes taken by this student."""
        return str(self._classes)

    # TODO - do this later
    # @classes.setter
    # def classes(self, new_classes):
    #     self._classes = new_classes

    def add_class(self, period, new_class):
        """Method to add a class to this student."""
        self._classes[period - 1] = new_class
        # if type(new_class) is str:
        #     self._classes.append(new_class)
        #
        # if type(new_class) is list:
        #     self._classes += new_class

    @property
    def advisors(self):
        """Get or set the advisors for this student."""
        return self._advisors

    def add_advisor(self, advisor):
        """Method to add a class to this student."""
        # index = self._advisors.next_unassigned_index()
        # self._advisors[index] = advisor
        self._advisors.push(advisor)

    def __str__(self):
        """Built-in Method to return a string with student info."""
        # return f"Student ID: {self._id}, Name: {self._name}"
        result = (f"Student ID: {self._id}, Name: {self.name}, "
                  f"Year: {self.year}\n"
                  f"Address: {self.address}, Phone: {self.phone}\n"
                  f"Classes: {self.classes}\nBirth Date: {self.birth_date}"
                  f"\nAdvisors: {self.advisors}")
        # if self.classes:
        #     result += "\nClasses: "
        #     for next_class in self.classes[:-1]:
        #         result += f"{next_class}, "
        #     result += self.classes[-1]
        return result

    def print_info(self):
        """Method to print all the info about a student."""
        print(self)

    def same_grade(self, other):
        """Method to check if two students are in the same grade."""
        return self._year == other.year

    @classmethod
    def get_default_year(cls):
        """Get or set the default year class variable."""
        return cls.default_year

    @classmethod
    def set_default_year(cls, new_default_year):
        if not cls.valid_year(new_default_year):
            raise ValueError
        # else
        cls.default_year = new_default_year

    @classmethod
    def valid_year(cls, year):
        """Helper function to check a given year value."""
        if cls.MIN_YEAR <= year <= cls.MAX_YEAR:
            return True
        # else
        return False

    @classmethod
    def update_next_id(cls):
        cls.next_id += 1

    @staticmethod
    def which_student_earlier(student1, student2):
        """Compare 2 students  and return the student with the lower year.
        If the year is same, return the one whose name is ahead alphabetically.
        """
        if student1.year < student2.year:
            result = student1
        elif student2.year < student1.year:
            result = student2
        else:
            if student1.name < student2.name:
                result = student1
            else:
                result = student2
        return result

    @classmethod
    def which_student_earlier_copy(cls, student1, student2):
        """Compare 2 students  and return a copy of the student with the lower
        year.
        If year is same, return the one whose name is ahead alphabetically.
        """
        if student1.year < student2.year:
            result = student1
        elif student2.year < student1.year:
            result = student2
        else:
            if student1.name < student2.name:
                result = student1
            else:
                result = student2
        # return copy.copy(result)  # a better way
        new_student = cls(result.name, result.year)
        # new_student.classes = result.classes
        return new_student

    def __gt__(self, other):
        """Built-in method to support > operator."""
        # if self.year > other.year:
        #     return True
        # elif self.year < other.year:
        #     return False
        # else:
        # if self.name > other.name:
        if self.birth_date > other.birth_date:
            return True
        else:  # name is earlier or same means NOT greater than
            return False

    class Date:
        DEFAULT_DATE = "1/1/2000"

        def __init__(self, new_date=DEFAULT_DATE):
            try:
                self.date = new_date
            except ValueError:
                self._date = self.DEFAULT_DATE

        @property
        def date(self):
            return self._date

        @date.setter
        def date(self, new_date):
            parts = new_date.split("/")
            if 1 <= int(parts[0]) <= 12 and 1 <= int(parts[1]) <= 31 and \
                    1900 <= int(parts[2]) <= 2020:
                self._date = new_date
            else:
                raise ValueError

        def __gt__(self, other):
            """Built-in method to support > operator."""
            self_month, self_day, self_year = self.date.split("/")
            other_month, other_day, other_year = other.date.split("/")
            # self_month = int(self_parts[0])
            # other_month = int(other_parts[0])
            # self_day = int(self_parts[1])
            # other_day = int(other_parts[1])
            # self_year = int(self_parts[2])
            # other_year = int(other_parts[2])

            if self_year > other_year:
                return True
            elif self_year < other_year:
                return False
            else:
                if self_month > other_month:
                    return True
                elif self_month < other_month:
                    return False
                else:
                    if self_day > other_day:
                        return True
                    else:
                        return False

        def __str__(self):
            # return f"({self._month})/{self._day}/{self._year}"
            return self._date

    class Phone:
        DEFAULT_NUM = "0000000000"
        VALID_LEN = 10

        def __init__(self, new_num=DEFAULT_NUM):
            try:
                self.number = new_num
            except ValueError:
                self._number = self.DEFAULT_NUM

        @property
        def number(self):
            return self._number

        @number.setter
        def number(self, new_num):
            valid_num = self.get_valid_num(new_num)
            if valid_num is None:
                raise ValueError
            # else
            self._number = valid_num

        @classmethod
        def get_valid_num(cls, number):
            if type(number) is not str:
                print(f"{number} is not a string")
                return None
            pure_number = cls.extract_digits(number)
            if len(pure_number) != cls.VALID_LEN:
                print(f"{pure_number} is not {cls.VALID_LEN} digits long")
                return None
            # print(f"get_valid_num: returning {pure_number}")
            return pure_number

        @staticmethod
        def extract_digits(number):
            if type(number) is not str:
                print(f"{number} is not a string")
                return None
            # else
            digits_only = ""
            for ch in number:
                if ch.isdigit():
                    digits_only += ch
            # print(f"extract_digits: returning {digits_only}")
            return digits_only

        def __str__(self):
            return f"({self.number[:3]}) {self.number[3:6]}-{self.number[6:]}"

    class Address:
        DEFAULT_HOUSE_NUM = 0
        DEFAULT_STREET = "No Street"
        DEFAULT_APT_NUM = 0
        VALID_LEN = 10

        def __init__(self, house_number=DEFAULT_HOUSE_NUM,
                     street=DEFAULT_STREET, apt_num=DEFAULT_APT_NUM):
            try:
                self.house_number = house_number
            except (TypeError, ValueError):
                self._house_number = self.DEFAULT_HOUSE_NUM

            try:
                self.street = street
            except TypeError:
                self._street = self.DEFAULT_STREET

            try:
                self.apt_num = apt_num
            except (TypeError, ValueError):
                self._apt_num = self.DEFAULT_APT_NUM

        @property
        def house_number(self):
            return self._house_number

        @house_number.setter
        def house_number(self, new_num):
            if type(new_num) is not int:
                raise TypeError
            elif new_num <= 0:
                raise ValueError
            # else
            self._house_number = new_num

        @property
        def street(self):
            return self._street

        @street.setter
        def street(self, new_street):
            if type(new_street) is not str:
                raise TypeError
            # else
            self._street = new_street

        @property
        def apt_num(self):
            return self._apt_num

        @apt_num.setter
        def apt_num(self, new_num):
            if type(new_num) is not int:
                raise TypeError
            elif new_num <= 0:
                raise ValueError
            # else
            self._apt_num = new_num

        @staticmethod
        def which_address_closer(addr1, addr2):
            if addr1.street < addr2.street:
                return addr1
            else:
                return addr2

        def __str__(self):
            if (self.house_number == self.DEFAULT_HOUSE_NUM and
                    self.street == self.DEFAULT_STREET):
                addr_str = f"<None>"
            else:
                addr_str = f"{self.house_number} {self.street}"
                if self.apt_num != self.DEFAULT_APT_NUM:
                    addr_str += f", #{self.apt_num}"
            return addr_str


class StudentListUtilities:

    NOT_FOUND = -1

    # to count the comparisons needed for each recursive binary search
    items_checked = 0

    @staticmethod
    def to_string(students):
        """Debug function to print student info, one per line."""
        return_str = ""
        # for student in students:
        for i in range(len(students)):
            student = students[i]
            # return_str += str(student) + "\n"
            return_str += f"\n{student}\n"
        return return_str

    @staticmethod
    def to_short_string(students):
        """Debug function to print just the student name, one per line."""
        return_str = "[ "
        for student in students:
            return_str += student.name + " "
        return_str += " ]"
        return return_str

    @staticmethod
    def to_gui_string(students):
        """Debug function to print just the student name, one per line."""
        if not students:
            return "<None>"
        return_str = ""
        for student in students:
            return_str += f"Name: {student.name}, Year: {student.year}\n"
        return return_str

    @classmethod
    def linear_search(cls, name, students):
        """Search for a name in the list of students using linear search."""
        i = 0  # to avoid i being undefined if 'students' is empty
        for i in range(len(students)):
            if students[i].name == name:
                print(f"Linear: '{name}' found at index {i} after "
                      f"checking {i + 1} items")
                return i
        print(f"Linear: {name} NOT found after checking {i + 1} items")
        return cls.NOT_FOUND

    @classmethod
    def binary_search(cls, name, students):
        """Search for a name in the list of students using binary search."""
        # print(f"\nEntered binary_search looking for {name}")
        cls.items_checked = 0  # reset count from previous search
        index = cls.binary_search_h(name, students, 0, len(students) - 1)
        if index == cls.NOT_FOUND:
            print(f"Binary: '{name}' NOT found ", end="")
        else:
            print(f"Binary: '{name}' found at index {index} ", end="")
        print(f"after checking {cls.items_checked} items")
        return index

    @classmethod
    def binary_search_h(cls, name, students, start, end):
        """Helper function for recursive binary search."""
        # print(f"start = {start} end = {end}", end=", ")
        if start > end:
            # print(f"Returning NOT_FOUND")
            return cls.NOT_FOUND

        mid = (start + end) // 2
        # print(f"mid = {mid}")
        mid_student_name = students[mid].name
        cls.items_checked += 1
        if mid_student_name == name:
            # print(f"Name '{name}' found at index {mid}")
            return mid
        else:
            if name < mid_student_name:
                return cls.binary_search_h(name, students, start, mid - 1)
            else:
                return cls.binary_search_h(name, students, mid + 1, end)

    @classmethod
    def binary_search_iterative(cls, students, name):
        """Iterative version of binary search."""
        print(f"Entered binary_search_iterative looking for {name}")
        start = 0
        end = len(students) - 1
        mid_index = end // 2
        mid_student = students[mid_index]
        i = 0
        while mid_student.name != name:
            print(f"start = {start} end = {end} mid = {mid_index}: "
                  f"middle student '{mid_student.name}' did not match, "
                  f"")
            i += 1
            if mid_index <= start or mid_index >= end:
                print(f"{name} NOT found after {i} comparisons")
                return cls.NOT_FOUND

            if name < mid_student.name:
                end = mid_index - 1
            else:
                start = mid_index + 1
            mid_index = (start + end) // 2
            mid_student = students[mid_index]

        print(f"Name '{name}' found after {i} comparisons")
        return mid_index

    @staticmethod
    def bubble_sort(students):
        """Sort in-place the given list of Student objects using Bubble Sort."""
        list_size = len(students)
        for i in range(list_size - 1):
            list_changed = False
            for j in range(list_size - 1 - i):
                # s1 = students[j]
                # s2 = students[j + 1]
                # if Student.which_student_earlier(s1, s2) == s2:
                if students[j] > students[j + 1]:
                    students[j], students[j + 1] = \
                            students[j + 1], students[j]
                    # print(StudentListUtilities.to_short_string(students))
                    list_changed = True
            if not list_changed:
                return

    @classmethod
    def selection_sort(cls, students):
        """Sort in-place the given list of students using Selection Sort."""
        unsorted_len = len(students)
        while unsorted_len > 1:
            largest_index = cls.get_largest_index(students, unsorted_len)
            students[largest_index], students[unsorted_len - 1] = \
                students[unsorted_len - 1], students[largest_index]
            print(StudentListUtilities.to_short_string(students))
            unsorted_len -= 1

    @staticmethod
    def get_largest_index(item_list, length):
        """Return the index of the largest item in the given list."""
        largest_index = 0
        largest_item = item_list[largest_index]
        # search items from second index to the last index, both inclusive
        for i in range(1, length):
            if item_list[i] > largest_item:
                largest_item = item_list[i]
                largest_index = i
        return largest_index

    @classmethod
    def insertion_sort(cls, students):
        """Sort in-place the given list using Insertion Sort."""
        for i in range(1, len(students)):
            print(f"i = {i}: {cls.to_short_string(students)}")
            next_unsorted = students[i]
            j = i - 1  # start checking from the last sorted item
            while j >= 0 and students[j] > next_unsorted:
                # move the larger item up to make room for the unsorted item
                students[j + 1] = students[j]
                print(cls.to_short_string(students))
                j -= 1
            # insert the unsorted item
            students[j + 1] = next_unsorted
            print(cls.to_short_string(students))
            print()

    @classmethod
    def merge_sort(cls, students):
        """Sort in-place the given list of students using Merge Sort."""
        length = len(students)
        if length == 1:
            print(f"returning because length of "
                  f"{StudentListUtilities.to_short_string(students)} is 1")
            return

        mid = length // 2
        print(f"students: {StudentListUtilities.to_short_string(students)}"
              f" len = {length}, mid = {mid}")
        # time.sleep(0.5)

        first_half = students[:mid]
        second_half = students[mid:]
        cls.merge_sort(first_half)
        cls.merge_sort(second_half)
        print(f"Now to merge {StudentListUtilities.to_short_string(first_half)}"
              f" with {StudentListUtilities.to_short_string(second_half)}")

        i = 0
        j = 0
        k = 0
        while i < len(first_half) and j < len(second_half):
            if first_half[i] > second_half[j]:
                students[k] = second_half[j]
                j += 1
            else:
                students[k] = first_half[i]
                i += 1
            k += 1
            print(f"i = {i} j = {j} k = {k} students = "
                  f"{StudentListUtilities.to_short_string(students)}")

        while i < len(first_half):
            students[k] = first_half[i]
            i += 1
            k += 1

        while j < len(second_half):
            students[k] = second_half[j]
            j += 1
            k += 1

        print(f"merged list {StudentListUtilities.to_short_string(students)}\n")
