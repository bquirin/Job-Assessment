class Person:
    children = []
    parents = []
    mother = ""
    father = ""

    def __init__(self, name, gender=""):
        self.name = name
        self.gender = gender

    def __repr__(self):
        return f"{self.name}({self.gender})"


class Family:
    # class variable
    people = []

    def __init__(self):
        pass

    def find(self, name):
        for human in Family.people:
            if human.name == name:
                return human
        return None

    def male(self, name):
        human = self.find(name)

        if human is None:
            human = Person(name)
            human.gender = "Male"
            Family.people.append(human)
            return True
        elif human.gender == "":
            human.gender = "Male"
            return True
        elif human.gender != "Male":
            return False
        return False

    def female(self, name):
        human = self.find(name)

        if human is None:
            human = Person(name)
            human.gender = "Female"
            Family.people.append(human)
            return True
        elif human.gender == "":
            human.gender = "Female"
            return True
        elif human.gender != "Female":
            return False
        return False

    def isMale(self, name):
        human = self.find(name)

        if human.gender == "Male":
            return True
        return False

    def isFemale(self, name):
        human = self.find(name)

        if human.gender == "Female":
            return True
        return False

    def setParent(self, childName, parentName):
        child = self.find(childName)
        parent = self.find(parentName)

        if child is None:
            child = Person(childName)
            Family.people.append(child)

        if parent is None:
            parent = Person(parentName)
            Family.people.append(parent)

        if self.isMale(parentName):
            child.father = parent
        elif self.isFemale(parentName):
            child.mother = parent

        parent.children.append(child)
        child.parents.append(parent)

        return True

    def getParents(self, name):
        parents = []

        for human in self.find(name).parents:
            parents.append(human.name)
        return parents.sort()

    def getChildren(self, name):
        children = []

        for human in self.find(name).children:
            children.append(human.name)
        return children.sort()
