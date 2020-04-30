import tkinter as tk
from student import Student
from student import StudentListUtilities


class StudentGui:
    DEFAULT_NAME = ""
    DEFAULT_GRADE = 9
    DEFAULT_ADDRESS = "123 Main St, 456"
    DEFAULT_PHONE = "123 456 7890"

    def __init__(self):
        """Constructor for a GUI for Student."""
        self._root = tk.Tk()

        # -------------- one message widget ---------------------
        header = "Enter student info"
        self._header = tk.Message(self._root, text=header)
        self._header.config(font=("times", 18, "italic"),
                            bg="lightblue", width=300)

        # ----------------- some label widgets ------------------
        self._label_name = tk.Label(self._root, text="Name",
                                    padx=20, pady=10)
        self._label_grade = tk.Label(self._root, text="Grade",
                                     padx=20, pady=10)
        self._label_address = tk.Label(self._root, text="Address",
                                       padx=20, pady=10)
        self._label_phone = tk.Label(self._root, text="Phone",
                                     padx=20, pady=10)

        # Assume this will be used to show list of students at the start
        self._label_answer_text = tk.Label(self._root, padx=20, pady=10)
        self._label_answer_value = tk.Label(self._root, padx=20, pady=10)

        # ----------------- some entry widgets ------------------
        self._entry_name = tk.Entry(self._root)
        self._entry_name.insert(0, self.DEFAULT_NAME)
        self._entry_grade = tk.Entry(self._root)
        self._entry_grade.insert(0, str(self.DEFAULT_GRADE))
        self._entry_address = tk.Entry(self._root)
        self._entry_address.insert(0, self.DEFAULT_ADDRESS)
        self._entry_phone = tk.Entry(self._root)
        self._entry_phone.insert(0, self.DEFAULT_PHONE)

        # ----------------- some button widgets ------------------
        self._button_add = tk.Button(self._root, text="Add",
                                     command=self._add_student)
        self._button_remove = tk.Button(self._root, text="Remove",
                                        command=self._remove_student)
        self._button_student_info = tk.Button(self._root, text="Student Info",
                                              command=self._student_info)
        self._button_all_students = tk.Button(self._root, text="All Students",
                                              command=self._all_students)

        # ------------ place all widgets using grid layout -------------
        self._header.grid(row=0, column=0, columnspan=2, sticky=tk.EW)

        self._label_name.grid(row=1, column=0, sticky=tk.E)
        self._entry_name.grid(row=1, column=1, padx=25, sticky=tk.W)

        self._label_grade.grid(row=2, column=0, sticky=tk.E)
        self._entry_grade.grid(row=2, column=1, padx=25, sticky=tk.W)

        self._label_address.grid(row=3, column=0, sticky=tk.E)
        self._entry_address.grid(row=3, column=1, padx=25, sticky=tk.W)

        self._label_phone.grid(row=4, column=0, sticky=tk.E)
        self._entry_phone.grid(row=4, column=1, padx=25, sticky=tk.W)

        self._label_answer_text.grid(row=5, column=0, pady=4, sticky=tk.E)
        self._label_answer_value.grid(row=5, column=1, sticky=tk.W)

        self._button_add.grid(row=6, column=0, padx=20, sticky=tk.EW)
        self._button_remove.grid(row=6, column=1, padx=20, sticky=tk.EW)

        self._button_student_info.grid(row=7, column=0, padx=25, pady=15,
                                       sticky=tk.EW)
        self._button_all_students.grid(row=7, column=1, padx=25, pady=15,
                                       sticky=tk.EW)

        # ------ Initialize a list to hold students as they are added -----
        self._students = []

        # to make testing easier
        # self._students = [
        #     Student("JP", 10),
        #     Student("Jasmine", 10),
        #     Student("Bresy", 11),
        #     Student("Francisco", 11),
        #     Student("Jonathan", 11),
        #     Student("Jacob", 12),
        # ]

        self._display_students()

    @property
    def root(self):
        return self._root

    def _add_student(self):
        """event handler to add a student."""

        # First, create a Student object with name and grade
        name = self._entry_name.get()
        grade = int(self._entry_grade.get())
        student = Student(name, grade)

        # Now, try to set address and phone
        address = self._entry_address.get()
        try:
            student.address = address
        except ValueError:
            self._label_answer_text.config(text="Error")
            message = f"*** Failed to set {address} as new address ***"
            self._label_answer_value.config(text=message)
            return

        phone = self._entry_phone.get()
        try:
            student.phone = phone
        except ValueError:
            self._label_answer_text.config(text="Error")
            message = f"*** Failed to set {phone} as new phone ***"
            self._label_answer_value.config(text=message)
            return

        # Finally, add to our list of students and display updated list
        self._students.append(student)
        self._display_students()

    def _display_students(self):
        self._label_answer_text.config(text="Students")
        students = StudentListUtilities.to_gui_string(self._students)
        self._label_answer_value.config(text=students)

    def _remove_student(self):
        """event handler to remove a student."""
        name = self._entry_name.get()
        index = StudentListUtilities.linear_search(name, self._students)
        if index == StudentListUtilities.NOT_FOUND:
            self._label_answer_text.config(text="Error")
            result = f"Name '{name}' not found."
        else:
            self._students.pop(index)
            self._label_answer_text.config(text="Students")
            result = StudentListUtilities.to_gui_string(self._students)
        self._label_answer_value.config(text=result)

    def _student_info(self):
        """event handler to display full info of a student."""
        name = self._entry_name.get()
        index = StudentListUtilities.linear_search(name, self._students)
        if index == StudentListUtilities.NOT_FOUND:
            self._label_answer_text.config(text="Error")
            result = f"Name '{name}' not found."
        else:
            self._label_answer_text.config(text="Student Info")
            result = f"Record for {name} - {self._students[index]}"
        self._label_answer_value.config(text=result)

    def _all_students(self):
        """event handler to display all students."""
        self._label_answer_text.config(text="Students")
        students = StudentListUtilities.to_gui_string(self._students)
        self._label_answer_value.config(text=students)


demo = StudentGui()
demo.root.title("Student GUI")
demo.root.mainloop()
