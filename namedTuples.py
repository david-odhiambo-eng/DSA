import collections
Student = collections.namedtuple('Student', ['name', 'age', 'index'])

student = Student(name='David', age=23, index='ENE221-0135/2022')
print(f'Name: {student.name}, Age: {student.age}, Index: {student.index}')