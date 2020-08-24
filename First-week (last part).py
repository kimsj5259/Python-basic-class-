#Class Assignment
'''
class Database:
  def __init__(self,name,size): ##생성자
    self.name = name
    self.size = size
    self.db   = {}
    
  def insert(self, field, value): ##메소드
    if len(self.db) < self.size:
      self.db[field] = value
      
  def select(self, field):
    if field in self.db:
      return self.db[field]
    else:
      return None
    
  def update(self, field, value):
    if field in self.db:
      self.db[field] = value
  
  def delete(self, field):
    if field in self.db:
      del self.db[field]
'''

#class 상속
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def say_hello(self, to_name):
    print("안녕, " + to_name + " 나는 " +self.name)

  def introduce(self):
    print("내이름은 " + self.name + " 그리고 나는 " + str(self.age) + " 살이야")

class Police(Person):
  def arrest(self, to_arrest):
    print("넌 체포됐다, " + to_arrest)

class Programmer(Person):
  def program(self, to_program):
    print("다음엔 뭘 만들지? 아 이걸 만들어야겠다: " + to_program)

wonie = Person("워니", 20)
jenny = Police("제니", 21)
michael = Programmer("마이클", 22)

wonie.introduce()
jenny.arrest("워니")
michael.introduce()
michael.program("이메일 클라이언트")

wonie.arrest("제니")


