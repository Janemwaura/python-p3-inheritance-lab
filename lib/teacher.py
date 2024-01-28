#!/usr/bin/env python


from user import User
import random

class Teacher(User):
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

    def teach(self):
        return random.choice(self.knowledge)

my_teacher = Teacher("My", "Teacher")


print(my_teacher.knowledge)
