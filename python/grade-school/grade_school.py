# '''
# The test code is not good I think...
# when concept by dictinoary datastructure like {'student_name' : 'grade'}, Can make duplicate in name
# ex) "Alice" is 1st grade, also same name in 3rd grade, 4th grade ...
#
# And then, I concept by list datastructure.
# '''
#
# class School:
#     def __init__(self):
#         self.grade_1 = []
#         self.grade_2 = []
#         self.grade_3 = []
#
#     def add_student(self, name, grade):
#         if not hasattr(self, "grade_"+str(grade)):  # check instance has "grade_(grade_number)" instance variable
#             setattr(self,"grade_"+str(grade),[])    # ? No -> make instance variable
#         getattr(self,"grade_" + str(grade)).append(name)
#         getattr(self, "grade_" + str(grade)).sort() # sort when new data inserted
#
#     def roster(self):
#         ## think more pythonic.....
#         all_student = []
#         for n in self.__dict__.values():
#             all_student.extend(n)
#         return all_student
#
#     def grade(self, grade_number):
#         return self.__getattribute__("grade_" + str(grade_number))
#
#
# '''
# refer URLs
# ## How to check instance vairable
# # https://stackoverflow.com/questions/17996570/whats-the-best-way-to-check-if-class-instance-variable-is-set-in-python
#
# ## How to check local variables
# # https://www.geeksforgeeks.org/how-to-check-if-a-python-variable-exists/
#
# ## How to Get a List of Class Attributes in Python
# # https://www.blog.pythonlibrary.org/2013/01/11/how-to-get-a-list-of-class-attributes/
# '''

from collections import defaultdict

class School(object):
    def __init__(self):
        self.db = defaultdict(set)

    def grade(self, n):
        return sorted(list(self.db[n])) or []

    def add_student(self, name, grade):
        self.db[grade].add(name)

    def roster(self):
        return [name
                for k, v in sorted(self.db.items())
                for name in sorted(v)
                ]