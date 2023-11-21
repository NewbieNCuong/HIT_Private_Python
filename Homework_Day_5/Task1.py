code_studentone = set([int(i) for i in input().split()])
code_studenttwo = set([int(i) for i in input().split()])
list1, list2, list3 = code_studentone & code_studenttwo, code_studentone | code_studenttwo, code_studentone - code_studenttwo
print("At two tables, List of students register: ", list1 if len(list1) > 0 else "No students registered")
print("List of students register at two tables: ", list2)
print("List of students register at desk one without register desk two: ", list3)
print("List of students register at desk one: ", list3)