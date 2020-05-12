"""Unit 5 Test - John Paul Aguilar"""


class Array:
    DEFAULT_PERIODS_NUM = 6
    DEFAULT_CLASS = "Tutorial"

    def __init__(self, periods_num=DEFAULT_PERIODS_NUM,
                 initial_class=DEFAULT_CLASS):
        self._classes_array = [initial_class for _ in range(periods_num)]

    def __getitem__(self, index):
        """Returns the item at the inputted index"""
        if self.valid_index(index):
            return self._classes_array[index]

    def __setitem__(self, index, value):
        """Sets the item at the inputted index to a new value if both the
        index and value are valid"""
        if self.valid_index(index):
            if type(value) is str:
                self._classes_array[index] = value
            else:
                raise TypeError
        else:
            raise IndexError

    def valid_index(self, index):
        """Determines if an index is valid"""
        if 0 <= index < len(self._classes_array):
            return True
        else:
            raise IndexError

    def __len__(self):
        """Returns the length of the array"""
        return len(self._classes_array)

    def __str__(self):
        """Returns the array as a string"""
        string_classes = ""
        array_length = len(self._classes_array)
        for index in range(array_length):
            if index != array_length - 1:
                string_classes += f"{self._classes_array[index]}, "
            else:
                string_classes += f"{self._classes_array[index]}"
        return string_classes
