class Student_info():
	def __init__(self, name, level, course):

		self.student_name = name
		self.student_level = level
		self.student_field = course
		self.student_CGPA = 4.0
	
	def get_student_description(self):
		print(self.student_name," is a ",self.student_level,"level student of", self.student_field)
	
	def get_student_CGPA(self):
		print(self.student_name,"'s CGPA is ",self.student_CGPA)
        
student1 = Student_info("Godson",400,"Chemical Engineering")

student1.get_student_description()
 
student1.get_student_CGPA()                     