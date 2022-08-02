#!/usr/bin/python3
#9-student.py
"""defines the student class
"""
class Student:
    """The Student class
    """    
    def __init__(self, first_name, last_name, age):
        """defines a student

        Args:
            first_name (string): The first name of the student
            last_name (string): The last name of the student
            age (number): The age of the student
        """        
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self):
        """retrieves a dictionary representation of a Student instance

        Returns:
            any: dictionary representation of the student instance
        """        
        return self.__dict__