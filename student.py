"""Unit 5 Test - John Paul Aguilar"""
from Array import Array


class Student:
    DEFAULT_NAME = "No Name"
    ORIGINAL_DEFAULT_YEAR = 0
    ORIGINAL_DEFAULT_SPORT = "No sport"
    DEFAULT_CLASSES = "ClassesUnknown"
    next_id = 1
    MAX_LEN_NAME = 20
    MIN_YEAR = 0
    MAX_YEAR = 12
    MAX_LEN_CLASSES_NAME = 40
    MIN_SPORTS_NAME_LEN = 0
    MAX_SPORTS_NAME_LEN = 20
    default_sport = ORIGINAL_DEFAULT_SPORT
    default_year = ORIGINAL_DEFAULT_YEAR

    def __init__(self, name=DEFAULT_NAME, year=None):
        if year is None:
            year = self.default_year
        self._student_id = self.next_id
        self.update_next_id(self.next_id + 1)
        try:
            self.name = name
        except ValueError:
            self._student_name = self.DEFAULT_NAME
        except TypeError:
            self._student_name = self.DEFAULT_NAME
        try:
            self.year = year
        except ValueError:
            self._year = self.default_year
        except TypeError:
            self._year = self.default_year
        self._current_sport = ""
        self.current_sport = self.default_sport
        self._phone = self.PhoneNumber()
        self._address = self.Address()
        self._classes = Array()
        self._date = self.Date()

    @property
    def name(self):
        """Returns the name of the student"""
        return self._student_name

    @name.setter
    def name(self, new_name):
        """Checks the entered name and assigns the appropriate option"""
        if type(new_name) is str:
            if 0 < len(new_name) <= self.MAX_LEN_NAME:
                self._student_name = new_name
            else:
                raise ValueError
        else:
            raise TypeError

    @property
    def year(self):
        """Returns the year of the student"""
        return self._year

    @year.setter
    def year(self, new_year):
        """Checks the validation of the year and assigns an appropriate
  value to the instance variable"""
        if self.valid_year(new_year):
            self._year = new_year
        else:
            raise ValueError

    @classmethod
    def set_default_year(cls, new_default_year):
        """Sets the current default year to a new value"""
        if cls.valid_year(new_default_year):
            cls.default_year = new_default_year
        else:
            raise ValueError

    @classmethod
    def get_default_year(cls):
        """Returns the current default year"""
        return cls.default_year

    @classmethod
    def valid_year(cls, new_year):
        """Checks if the inputted year fits the parameters"""
        if cls.MIN_YEAR <= new_year <= cls.MAX_YEAR:
            return True
        else:
            return False

    @property
    def classes(self):
        """Returns the current classes"""
        return str(self._classes)

    def add_class(self, period_number, new_class):
        """Sets one of the items in the classes array to a new value"""
        self._classes[period_number] = new_class

    @property
    def phone(self):
        """Returns the current phone number"""
        return f"{self._phone}"

    @phone.setter
    def phone(self, new_phone_number):
        """Sets the phone number to a new number if its valid"""
        self._phone.phone_number = new_phone_number

    @property
    def current_sport(self):
        """Returns the current sport"""
        return self._current_sport

    @current_sport.setter
    def current_sport(self, new_sport):
        """Sets the current sport to a new value if it is valid"""
        if self.valid_sport(new_sport):
            self._current_sport = new_sport
        else:
            raise ValueError

    @classmethod
    def get_default_sport(cls):
        """Returns the current default sport"""
        return cls.default_sport

    @classmethod
    def set_default_sport(cls, new_default_sport):
        """Sets the current default sport to a new value if it is valid"""
        if cls.valid_sport(new_default_sport):
            cls.default_sport = new_default_sport
        else:
            raise ValueError

    @classmethod
    def valid_sport(cls, new_sport):
        """Checks if a new sport is valid"""
        if (cls.MIN_SPORTS_NAME_LEN < len(new_sport) <
                cls.MAX_SPORTS_NAME_LEN):
            return True
        else:
            return False

    @classmethod
    def update_next_id(cls, new_id):
        """Sets the next class id to a new value"""
        if type(new_id) is int:
            cls.next_id = new_id
        else:
            raise TypeError

    def get_student_id(self):
        """Returns the student id of this student"""
        return self._student_id

    @staticmethod
    def which_student_earlier(s1, s2):
        """Compare 2 students and return the student with the lower year.
   If year is same, return the one whose name is ahead alphabetically.
   """
        if s1.year > s2.year:
            return s1
        elif s2.year > s1.year:
            return s2
        else:
            if s1.name > s2.name:
                return s1
            elif s2.name > s1.name:
                return s2
            else:
                return s2

    def same_grade(self, other):
        """Checks if an inputted student and the student of this instance
     are in the same grade"""
        if self._year == other.year:
            return True
        return False

    @property
    def address(self):
        """Returns the current address"""
        return self._address

    @address.setter
    def address(self, new_address):
        """Sets the address to a new address if all the values are valid"""
        house_num, name_of_street, apart_num = new_address
        self._address.house_number = house_num
        self._address.street_name = name_of_street
        self._address.apartment_number = apart_num

    @property
    def date(self):
        """Returns the current date"""
        return str(self._date)

    @date.setter
    def date(self, new_date):
        """Sets the date to a new date"""
        self._date.date = new_date

    def __gt__(self, other):
        """Allows for this student class to be compared to another one"""
        if self._date > other.date:
            return True
        else:
            return False

    def __str__(self):
        """Prints all of the info of the current student"""
        return f"Student ID: {self._student_id}, Student name: " \
               f"{self._student_name}, Year: {self._year}, Phone Number: " \
               f"{self._phone}, Address: {self._address}, Classes: " \
               f"{self._classes}, Date = {self._date}"

    class PhoneNumber:
        DEFAULT_PHONE_NUMBER = "0000000000"
        MAX_STRING_LEN = 20
        MIN_DIGIT = 10

        def __init__(self, phone_number=DEFAULT_PHONE_NUMBER):
            try:
                self.phone_number = phone_number
            except ValueError:
                self._phone_number = self.DEFAULT_PHONE_NUMBER

        @property
        def phone_number(self):
            """Returns the current phone number"""
            return self._phone_number

        @phone_number.setter
        def phone_number(self, new_phone_number):
            """Sets the phone number to a new value if it is valid"""
            phone_number = self.get_valid_num(new_phone_number)
            if phone_number is not None:
                self._phone_number = phone_number
            else:
                print(f"Could not set the phone number to {new_phone_number}")
                raise ValueError

        @staticmethod
        def extract_digits(phone_number):
            """Takes a phone number and returns all the valid numbers that are
            extracted"""
            ACCEPTED_DIGITS = "1234567890"
            bare_phone_number = ""
            for ch in phone_number:
                if ch in ACCEPTED_DIGITS:
                    bare_phone_number += ch
            return bare_phone_number

        @classmethod
        def get_valid_num(cls, phone_number):
            """Determines if a phone number is valid"""
            if len(phone_number) <= cls.MAX_STRING_LEN:
                bare_phone_number = cls.extract_digits(phone_number)
                if len(bare_phone_number) >= cls.MIN_DIGIT:
                    return bare_phone_number
            return None

        def __str__(self):
            """Returns the phone number in string form"""
            return f"({self._phone_number[:3]}) {self._phone_number[3:6]}-" \
                   f"{self._phone_number[6:]}"

    class Address:
        DEFAULT_HOUSE_NUMBER = 1
        DEFAULT_STREET_NAME = "No street name"
        DEFAULT_APARTMENT_NUM = 1
        MIN_HOUSE_NUMBER = 0
        MIN_APARTMENT_NUM = 0
        MAX_APARTMENT_NUM = 1000

        def __init__(self, house_num=DEFAULT_HOUSE_NUMBER,
                     street_name=DEFAULT_STREET_NAME,
                     apartment_num=None):
            try:
                self.house_number = house_num
            except ValueError:
                self._house_number = self.DEFAULT_HOUSE_NUMBER
            try:
                self.street_name = street_name
            except TypeError:
                self._street_name = self.DEFAULT_STREET_NAME
            if apartment_num is not None:
                try:
                    self.apartment_number = apartment_num
                except ValueError:
                    self._apartment_number = self.DEFAULT_APARTMENT_NUM
            else:
                self._apartment_number = apartment_num

        @property
        def house_number(self):
            """Returns the house number"""
            return self._house_number

        @house_number.setter
        def house_number(self, new_house_number):
            """Sets the house number to a new number"""
            if new_house_number > self.MIN_HOUSE_NUMBER:
                self._house_number = new_house_number
            else:
                raise ValueError

        @property
        def street_name(self):
            """Returns the street name"""
            return self._street_name

        @street_name.setter
        def street_name(self, new_street_name):
            """Sets the street name to a new name"""
            if type(new_street_name) is str:
                self._street_name = new_street_name
            else:
                raise TypeError

        @property
        def apartment_number(self):
            """Returns the house number"""
            return self._apartment_number

        @apartment_number.setter
        def apartment_number(self, new_apartment_number):
            """Sets the apartment number to a new number"""
            if (self.MIN_APARTMENT_NUM < new_apartment_number <=
                    self.MAX_APARTMENT_NUM):
                self._apartment_number = new_apartment_number
            else:
                raise ValueError

        @staticmethod
        def which_address_closer(address1, address2):
            """Determines which address has a street name that comes first
            alphabetically"""
            if address1.street_name < address2.street_name:
                return address1
            else:
                return address2

        def display(self):
            """Prints all of the contents of the address using __str__
            function"""
            print(self)

        def __str__(self):
            """Returns the all of the parts of the address that were inputted
            in a string"""
            if (self._house_number == self.DEFAULT_HOUSE_NUMBER and
                    self._street_name == self.DEFAULT_STREET_NAME):
                address = "None"
            else:
                address = f"{self._house_number} {self._street_name}, " \
                          f"#{self._apartment_number}"
            return address

    class Date:
        DEFAULT_DATE = "1/1/2000"

        def __init__(self, date=DEFAULT_DATE):
            try:
                self.date = date
            except ValueError:
                self._date = self.DEFAULT_DATE

        @property
        def date(self):
            """Returns the date"""
            return self._date

        @date.setter
        def date(self, date):
            """Sets the current date to a new date if the new date is valid"""
            date = date.split("/")
            month = int(date[0])
            day = int(date[1])
            year = int(date[2])
            if 1 <= month <= 12 and 1 <= day <= 31 and 1900 <= year <= 2020:
                self._date = f"{month}/{day}/{year}"
            else:
                raise ValueError

        def __gt__(self, other):
            """Allows dates to be compared to each other"""
            date = self._date.split("/")
            month = int(date[0])
            day = int(date[1])
            year = int(date[2])
            other = other.split("/")
            other_month = int(other[0])
            other_day = int(other[1])
            other_year = int(other[2])
            if year > other_year:
                return True
            elif year == other_year:
                if month > other_month:
                    return True
                elif month == other_month:
                    if day > other_day:
                        return True
            return False

        def __str__(self):
            """Returns the date as a string"""
            return self._date


class StudentListUtilities:
    NOT_FOUND = -1

    @staticmethod
    def to_string(students_list):
        """Takes a list of student objects as a parameter and prints the
     list"""
        students = ""
        for student in students_list:
            students += f"{student}\n"
        return students

    @staticmethod
    def bubble_sort(students_list):
        """Uses bubble sort to sort a list"""
        list_length = len(students_list)
        swaps = False
        for n in range(list_length):
            for index in range(list_length - n):
                if students_list[index] > students_list[index + 1]:
                    students_list[index], students_list[index + 1] = \
                        students_list[index + 1], students_list[index]
                    swaps = True
            if swaps is False:
                break
            swaps = False

    @classmethod
    def selection_sort(cls, student_list):
        """Uses selection to sort a list"""
        list_length = len(student_list) - 1
        for n in range(list_length):
            unsorted_length = list_length - n
            largest_index = \
                cls.get_largest_index(student_list, unsorted_length)
            student_list[largest_index], student_list[unsorted_length] = \
                student_list[unsorted_length], student_list[largest_index]

    @staticmethod
    def get_largest_index(student_list, unsorted_length):
        """Goes through a student list and returns the index where the student
        with the name that comes last alphabetically"""
        largest_index = 0
        for index in range(unsorted_length + 1):
            if student_list[index] > student_list[largest_index]:
                largest_index = index
        return largest_index

    @staticmethod
    def insertion_sort(student_list):
        """Uses insertion method to sort a list"""
        for unsorted_index in range(1, len(student_list)):
            unsorted_first_item = student_list[unsorted_index]
            sorted_index = unsorted_index - 1
            while sorted_index >= 0 and student_list[sorted_index] > \
                    unsorted_first_item:
                student_list[sorted_index + 1] = student_list[sorted_index]
                sorted_index -= 1
            sorted_index += 1
            student_list[sorted_index] = unsorted_first_item

    @classmethod
    def merge_sort(cls, student_list):
        """Uses merge sort to sort a student list"""
        if len(student_list) > 1:
            midpoint = len(student_list) // 2
            first_half = student_list[:midpoint]
            second_half = student_list[midpoint:]
            cls.merge_sort(first_half)
            cls.merge_sort(second_half)
            first_half_length = len(first_half)
            second_half_length = len(second_half)
            first_half_index = 0
            second_half_index = 0
            original_list_index = 0
            while (first_half_index != first_half_length and second_half_index
                   != second_half_length):
                if first_half[first_half_index] > \
                        second_half[second_half_index]:
                    student_list[original_list_index] = \
                        second_half[second_half_index]
                    second_half_index += 1
                else:
                    student_list[original_list_index] = \
                        first_half[first_half_index]
                    first_half_index += 1
                original_list_index += 1
            for i in range(second_half_length - second_half_index, 0, -1):
                student_list[original_list_index] = second_half[-i]
                original_list_index += 1
            for j in range(first_half_length - first_half_index, 0, -1):
                student_list[original_list_index] = first_half[-j]
                original_list_index += 1

    @classmethod
    def linear_search(cls, student_list, student_name):
        """Looks through the list in a straight line in order to find a student
     with the given name"""
        for index in range(len(student_list)):
            if student_list[index].name == student_name:
                return index
        return cls.NOT_FOUND

    @classmethod
    def binary_search(cls, student_list, student_name):
        """Calls a helper function to find a name inside a student list"""
        return cls.binary_search_h(student_list, student_name, 0,
                                   len(student_list) - 1)

    @classmethod
    def binary_search_h(cls, student_list, student_name, start,
                        end):
        """Continuously cuts the parts of the list that are checked in half
      until the name is found or it is determined that the name is not in
      the list"""
        list_length = end - start
        midpoint = (start + end) // 2
        if student_list[midpoint].name == student_name:
            return midpoint
        else:
            if abs(list_length) == 1:
                return cls.NOT_FOUND
            elif student_name > student_list[midpoint].name:
                return cls.binary_search_h(student_list, student_name,
                                           midpoint + 1, end)
            elif student_name < student_list[midpoint].name:
                return cls.binary_search_h(student_list, student_name, start,
                                           midpoint - 1)
