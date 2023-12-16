

class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
    def __str__(self) -> str:
        return f'{self.firstName} {self.lastName}'
    
class Student(Person):
    def __init__(self,firstName, lastName):
        super().__init__(firstName, lastName)
        self.degreeCourse = None
    def __str__(self) -> str:
        if self.degreeCourse == None:
            return f'{self.firstName} {self.lastName} is not registered to any course'
        else:
             return f'{self.firstName} {self.lastName} is registered to {self.degreeCourse}'
    def setDegreeCourse(self, degreeCourse):
        self.degreeCourse = degreeCourse

if __name__ == "__main__":
    firstName = input("Insert first name: ")
    lastName = input("Insert last name: ")

    isStudent = None
    i = 0
    while not(isStudent == "y" or isStudent == "n"):
        if i == 0:
            isStudent = input("Are you a student?(y/n)")
        else:
            isStudent = input('Please type "y" or "n":')
        i += 1
        
    if isStudent == "y":
        degreeCourse = input("Please insert your degree course: ")
        st = Student(firstName, lastName)
        st.setDegreeCourse(degreeCourse)
    else:
        st = Person(firstName, lastName)

    print(st)


# python3 -c 'from student import Student; print(Student("Stefano", "Guarino"))'