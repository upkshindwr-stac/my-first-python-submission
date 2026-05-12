students = ["John" , "Sarah" , "Mike"]
students.append("Patrick")
#print(students)
#students[0]="Simon"
print(students)
students.remove("Mike")
#print("John" in students)
print(students.index("Sarah"))
sarah_pos = students.index("Sarah")
students[sarah_pos]="Mary"
print(students)
