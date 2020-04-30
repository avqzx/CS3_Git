import random
import string
from student import Student
from student import StudentListUtilities


def get_random_digits(num_digits):
    new_num = [str(random.randint(1, 9)) for _ in range(num_digits)]
    return "".join(new_num)


def get_random_street():
    street = random.choice(string.ascii_uppercase)
    num_letters = random.randint(3, 11)
    rest = [random.choice(string.ascii_lowercase) for _ in range(num_letters)]
    # print(rest)
    street += "".join(rest)
    street += " " + random.choice(["St", "Dr", "Ave", "Blvd", "Ct"])
    # street += " " + random.choice(["Street", "Drive", "Avenue", "Boulevard",
    #                                "Court"])
    return street


# names = ["Bresy", "Francisco", "JP", "Jacob", "Jasmine", "Jonathan",
#          "Kevin", "Luis", "Marvin"]

students = [
            # Student("Luis", 11),
            Student("JP", 10),
            Student("Jasmine", 10),
            Student("Bresy", 11),
            Student("Francisco", 11),
            Student("Jonathan", 11),
            Student("Jacob", 12),
            # Student("Kevin", 11),
            # Student("Marvin", 11),
            ]

# print(names)
# print(students[0])
# print(students[1].year)
print(StudentListUtilities.to_string(students))
# StudentListUtilities.bubble_sort(students)
# StudentListUtilities.selection_sort(students)
# StudentListUtilities.insertion_sort(students)
# StudentListUtilities.merge_sort(students)
# print(StudentListUtilities.to_string(students))

science_classes = ["AP Physics", "Physics", "Chemistry", "Biology"]
math_classes = ["Algebra 2", "Trig/Anal. Geom.", "Math Analysis", "AP Calc BC"]
english_classes = ["World Lit.", "American Lit.", "AP Language", "English 1A/1B"]
spanish_classes = ["Spanish 1", "Spanish 2", "Spanish 3", "Spanish 4"]
electives = ["Art", "CS 3A", "Music", "Strength"]
advisors = ["Stacy", "Ali", "Karla", "Marianne", "Nanor", "Amy"]

print(f"\n======= Adding birth date =======")

for student in students:
    """
    new_ph_num = get_random_digits(10)
    try:
        student.phone = new_ph_num
        # print(f"phone is now {student.phone}, type is {type(student.phone)}")
    except ValueError:
        print(f"*** Failed to set {new_ph_num} as new phone number ***")

    new_house_num = random.randint(1000, 9999)
    new_street = get_random_street()
    new_apt_num = random.randint(1, 100)
    try:
        # student.address = new_house_num, new_street, new_apt_num
        student.address = str(new_house_num) + " " + new_street + " " + str(new_apt_num)
        # print(f"Address is now {student.address}, type is {type(student.address)}")
    except ValueError:
        print(f"*** Failed to set {new_house_num}, {new_street}, {new_apt_num} "
              "as new address ***")

    print(f"{student.name} has {len(student._classes)} classes")

    try:
        student.add_class(1, random.choice(math_classes))
        student.add_class(2, random.choice(science_classes))
        student.add_class(3, random.choice(english_classes))
        student.add_class(4, random.choice(spanish_classes))
        student.add_class(6, random.choice(electives))
    except IndexError:
        print("*** Failed to add a class. Check period numbers. ***")
    except TypeError:
        print("*** Failed to add a class. Class must be a string. ***")

    # try:
    #     print(f"\nLast class for {student.name} is {student._classes[5]}")
    # except IndexError:
    #     print("*** Failed to get the last class item. Check index. ***")
    """
    try:
        birth_date = (str(random.randint(1, 1)) + "/" +
                      str(random.randint(1, 11)) + "/" +
                      str(random.randint(2000, 2000)))
        student.birth_date = birth_date
    except ValueError:
        print(f"*** Failed to set birth date {birth_date} for "
              f"{student.name} ***")

    # for i in range(5):
    #     student.add_advisor(random.choice(advisors))



print(f"\n======= After adding Advisors: =======")
print(StudentListUtilities.to_string(students))

print(f"\n======= After sorting: =======")
StudentListUtilities.bubble_sort(students)
print(StudentListUtilities.to_string(students))


"""
for name in names:
    print()
    index = StudentListUtilities.linear_search(name, students)
    # index = StudentListUtilities.binary_search(name, students)
    # if index == StudentListUtilities.NOT_FOUND:
    #     print(f"Name '{name}' not found in student list")
    # else:
    #     print(f"Record for {name} - {students[index]}")
"""