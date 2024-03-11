class StudentsInMLOps:
    def __init__(self):
        self.students = 0
        self.className = "StudentsInMLOps"

    def dropStudents(self, count):
        self.students -= count

    def getTotalStrength(self):
        return self.students

    def enrollStudents(self, count):
        self.students += count


    def getClassName(self):
        return self.className
