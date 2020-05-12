"""Unit 6 Assignment 7 - John Paul Aguilar"""
import tkinter as tk
from student import Student
from student import StudentListUtilities


class StudentGUI:
    ORIGINAL_NAME = ""
    student_list = []
    ORIGINAL_YEAR = 0

    def __init__(self):
        self._root = tk.Tk()

        # Label widgets
        self._label_name = tk.Label(self._root, text="Name")
        self._label_year = tk.Label(self._root, text="Year")
        self._student_list = tk.Label(self._root, text=" - ")

        self._original_name = self.ORIGINAL_NAME
        self._original_year = self.ORIGINAL_YEAR
        # Entry Widgets
        self._entry_name = tk.Entry(self._root)
        self._entry_name.insert(0, self._original_name)
        self._entry_year = tk.Entry(self._root)
        self._entry_year.insert(0, self._original_year)

        # Button Widgets
        self._button_name = tk.Button(self._root, text="Add Student",
                                      command=self._add_student)
        self._button_show = tk.Button(self._root, text="Show all students",
                                      command=self._show_students)

        self._label_name.grid(row=1, column=0, sticky=tk.E)
        self._entry_name.grid(row=1, column=1, sticky=tk.W)
        self._label_year.grid(row=2, column=0, sticky=tk.E)
        self._entry_year.grid(row=2, column=1, sticky=tk.W)

        self._button_name.grid(row=4, column=0, pady=15)
        self._button_show.grid(row=5, column=0, pady=15)

    @property
    def root(self):
        """Returns the Tk class"""
        return self._root

    def _add_student(self):
        """Adds a new student object to the list"""
        new_student = Student(self._entry_name.get(),
                              int(self._entry_year.get()))
        self.student_list.append(new_student)

    def _show_students(self):
        """Shows the list of students that have been accumulated"""
        student_str_list = StudentListUtilities.to_string(self.student_list)
        print(type(student_str_list))
        self._student_list.config(text=student_str_list)
        self._student_list.grid(row=6, column=0)


student_gui = StudentGUI()
student_gui.root.title("List of Students")
student_gui.root.mainloop()

"""
This was what I did in the time specified. 
I was confused by the grid and frames part if GUI and hope to clarify"""