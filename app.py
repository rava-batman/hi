class Person:
    def __init__(self, name, age, is_married=False):
        self.name = name
        self.age = age
        self.is_married = is_married
        self.children = []

    def adopt_child(self, child):
        self.children.append(child)
        child.is_step_child = not child.has_biological_parent(self)

    def has_children(self):
        return len(self.children) > 0

    def get_parents(self):
        return [parent.name for parent in self.children[0].parents] if self.has_children() else "No children"

class Couple:
    def __init__(self, person1, person2):
        self.spouse1 = person1
        self.spouse2 = person2
        self.spouse1.is_married = True
        self.spouse2.is_married = True

    def check_and_adopt(self, child):
        if not self.spouse1.has_children() and not self.spouse2.has_children():
            self.spouse1.adopt_child(child)
            self.spouse2.adopt_child(child)
        else:
            print("They already have children.")

class Child(Person):
    def __init__(self, name, age, parents=None):
        super().__init__(name, age)
        self.parents = parents or []
        self.is_step_child = False

    def has_biological_parent(self, parent):
        return parent in self.parents

    def is_step_child(self):
        return self.is_step_child

# Usage
parent1 = Person("John", 35)
parent2 = Person("Jane", 33)
couple = Couple(parent1, parent2)

child1 = Child("Alice", 5)
couple.check_and_adopt(child1)

print("Parents of child:", child1.get_parents())
print("Is step child:", child1.is_step_child())