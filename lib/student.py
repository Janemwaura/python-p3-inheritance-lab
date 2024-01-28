#!/usr/bin/env python

from user import User

class Student(User):
    default_knowledge = [
        "str is a data type in Python",
        "programming is hard, but it's worth it",
        "JavaScript async web request",
        "Python function call definition",
        "object-oriented teacher instance",
        "programming computers hacking learning terminal",
        "pipenv install pipenv shell",
        "pytest -x flag to fail fast",
    ]
    
    def __init__(self, first_name, last_name, knowledge=None):
        super().__init__(first_name, last_name)
        self.knowledge = knowledge if knowledge is not None else self.default_knowledge

    def learn(self, new_knowledge):
        self.knowledge.append(new_knowledge)    
# Example usage
my_student = Student("John", "Doe")

# Or with knowledge
knowledge_for_student = ["Python basics", "OOP principles"]
my_student_with_knowledge = Student("Jane", "Smith", knowledge=knowledge_for_student)
