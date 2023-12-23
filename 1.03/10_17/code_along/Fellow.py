# TODO: implement Fellow class that inherits from "Person"
# we just include another method called "form_group()"
# that prints out all the people that this fellow knows
# using a for-loop. Implement below
...
from Person import PersonClass

class Fellow(PersonClass):

    def form_group(self):

        for fname in self.people:
            print(self.fname)

fellowA = Fellow("Farukh", "Hummus", ["Mo", "Tim", "Caridad"])

print(fellowA.name)
fellowA.form_group()