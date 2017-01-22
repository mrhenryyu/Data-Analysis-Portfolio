# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 13:28:07 2016

@author: HenryYu
"""

class Parent():
    def __init__(self, last_name, eye_color):
        self.last_name = last_name
        self.eye_color = eye_color
        print("Parent Constructor Called")
    
    def show_info(self):
        print("Last name - " + self.last_name)
        print("Eye color - " + self.eye_color)

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor Called")        
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

billy_cyrus = Parent("Cyrus", "Blue")
#print(billy_cyrus.eye_color)

miley_cyrus = Child("Cyrus", "Blue", 5)
print(miley_cyrus.last_name)
print(miley_cyrus.number_of_toys)
miley_cyrus.show_info()