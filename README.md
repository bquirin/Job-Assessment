# Job-Assessment
This is the repository which holds two python projects one for each of the Assessment tasks.

## The First Task
Given a string, replace every letter with its position in the alphabet. If anything in the text isn’t a letter, ignore it and don’t return it.

A is 1, B is 2, C is 3, etc.

As an example:

replaceLetterWithPosition(“This NETbuilder assessment is way too easy.”)

Should return:

“20 8 9 19 14 5 20 2 21 9 12 4 5 18 1 19 19 5 19 19 13 5 14 20 9 19 23 1 25 20 15 15 5 1 19 25”

## The Second Task
Create a class Family with the following methods. All arguments are strings: names of persons. Upon the first use of a name, that name is added to the family.

⦁ male(name)and female(name) returning boolean

Define the gender (corresponding to the method name) of the given person. Return false when these assignments cannot be made because of conflicts with earlier registered information.

⦁ isMale(name) and isFemale(name) returning boolean

Return true when the person has the said gender. When no gender was assigned, both methods should return false

⦁ setParent(childName, parentName) returning boolean

Defines the child-parent relationship between two persons. Returns false when the relationship cannot be made because of conflicts with earlier registered information.

⦁ getParents(name) and getChildren(name) returning array of string

Return the names of the person's parents/children in alphabetical order
