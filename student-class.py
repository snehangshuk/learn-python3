class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
  
  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade.score) 

  def print_grades(self):
    return self.grades

  def get_average(self):        
    return sum(self.grades) / len(self.grades)

class Grade:
  minimum_passing = 65
  
  def __init__(self, score):
    self.score = score

  def is_passing(self):
    if self.score >  minimum_passing:
      return "Passed"
    else:
      return "Failed"  
    
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
pieter.add_grade(Grade(100))
pieter.add_grade(Grade(50))
pieter.add_grade(Grade(40))
print(pieter.print_grades())
print(pieter.get_average())
