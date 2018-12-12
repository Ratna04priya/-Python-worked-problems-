#Creating Dictionaries - User Defined

num_students = 5


print "you have to enter details of  %s students" %num_students
student_info = {}
student_data = [ 'Age : ', 'address : ','class : ','mobile_1','mobile_2','sub_taken']
for i in range(0,1):
    student_name = raw_input("Name :")
    student_info[student_name] = {}
    for entry in student_data:
        student_info[student_name][entry] = raw_input(entry) 
#storing the marks entered as integers to perform arithmetic operations later on.
#print student_info
print"Please enter student name ?"
name = raw_input("Student name : ")
if name in student_info.keys():
	print "The details are : "
	print( student_info[student_name][mobile_2])
else:
    print "please enter valid name"
