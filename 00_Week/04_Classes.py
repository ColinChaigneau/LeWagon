###
### Challenge - Orange Tree
###

import random

class OrangeTree:
    def __init__(self):
        self.age = 0
        self.height = 0
        self.fruits = 0
        self.dead = False
    
    def one_year_passes(self):
        if self.dead:
            return
        self.age += 1
        # Tree death
        if self.age > 50:
            if random.randint(self.age, 100) == 100:
                self.dead = True
        elif not self.dead:
            # Tree growing
            if self.age <= 10: 
                self.height += 1
            # Fruits production if not dead
            if self.age >= 15:
                self.fruits = 0
            elif self.age >= 10:
                self.fruits = 200
            elif self.age > 5:
                self.fruits = 100
        

    def pick_a_fruit(self):
        if self.fruits > 0:     
            self.fruits -= 1


###
### Challenge - Self
###

class Cat:
    def __init__(self):
        self.age = 1
        self.color = 'brown'
        self.weight = 5

    def age_10_years(self):
        self.age = 10
        return self

    def gain_weight(self):
        self.weight = 20
        return self

    def turn_grey(self):
        self.color = 'grey'
        return self

###
### Challenge - Richest Student
###

class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties
    
    def wealth(self):
        return self.fives * 5 + self.tens * 10 + self.twenties * 20
    
    def compare(self, another_student):
        return self.name if self.wealth() >= another_student.wealth() else another_student.name
    
    def advanced_compare(self, students):
        students.append(self)
        return [student.name for student in sorted(students, key = Student.wealth, reverse = True)]
