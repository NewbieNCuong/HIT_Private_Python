class Hiter:
    __id = 0
    def __init__(self, name = "", age = 0, gen=""):
        Hiter.__id += 1
        self.__id = Hiter.__id
        self.__name = name
        self.__age = age
        self.__gen = gen
    
    def Enter(self):
        print(f"Entering Hiter {self.__id}: ")
        self.__name = input("Enter Hiter's name: ")
        self.__gen = input("Enter Hiter's gen: ")
        self.__age = int(input("Enter Hiter's age: "))
    
    def __str__(self):
        return f"Id: {self.__id} \n Name: {self.__name} \n Age: {self.__age} \n Gen: {self.__gen}"
    
    @staticmethod
    def ListHiter(self, a):
        for i in range(len(a)):
            print(f"{i}th member: {print(a[i])}")

class Department:
    def __init__(self, iddepartment = 0, namedepartment = "", chairman = None, members = None):
        self.__iddepartment = iddepartment
        self.__namedepartment = namedepartment
        self.__chairman = chairman
        self.__members = members if members is not None else []
    
    def Enter(self):
        self.__iddepartment = int(input("Enter idderartment: "))
        self.__namedepartment = input("Enter namedepartment: ")
        chairman = Hiter()
        chairman.Enter()
        num_members = int(input("Enter numbers members: "))
        for _ in range(num_members):
            member = Hiter()
            member.Enter()
            self.__members.append(member)
        
    def __str__(self):
        chairman_info = f"\nChairman: {str(self.__chairman)}"
        members_info = "\nMembers:" + "".join([f"\n{str(member)}" for member in self.__members])
        return f"Department ID: {self.__iddepartment}\nDepartment Name: {self.__namedepartment}" \
                f"{chairman_info}{members_info}"
    
    def ListHiterdepartment(self, a):
        for i in range(len(a)):
            print(f"{i}th member: {print(a[i])}")

    def add(self, hiter):
        if hiter in self.__members:
            return f"Hiter in department"
        else:
            self.__members.append(hiter)

    def remove(self, hiter):
        self.__members.remove(hiter)



#Cái nhập em bảo GPT nhập cho nhanh =))

n = int(input("Enter the number of Hiters: "))
hiters = []
for _ in range(n):
    new_hiter = Hiter()
    new_hiter.Enter()
    hiters.append(new_hiter)

# In thông tin n Hiter
print("\nList of Hiters:")
for hiter in hiters:
    print(str(hiter))

# Nhập m Department và in ra thông tin m Department.
m = int(input("\nEnter the number of Departments: "))
departments = []
for _ in range(m):
    new_department = Department()
    new_department.Enter()
    departments.append(new_department)

# In thông tin m Department
print("\nList of Departments:")
for department in departments:
    print(str(department))

# Nhập tên ban và xóa 1 hiter ban đó.
department_name_to_remove_from = input("\nEnter the name of the department to remove a Hiter from: ")
for department in departments:
    if department_name_to_remove_from.lower() == department._Department__namedepartment.lower():
        department.list_hiters()
        hiter_index_to_remove = int(input("Enter the index of the Hiter to remove: "))
        if 0 <= hiter_index_to_remove < len(department._Department__members):
            department.remove_hiter_from_department(department._Department__members[hiter_index_to_remove])
        else:
            print("Invalid index.")
        break
else:
    print(f"Department with name '{department_name_to_remove_from}' not found.")

# Thêm 1 hiter vào ban đó (đảm bảo hiter đó chưa có trong ban và có trong danh sách hiter hiện tại).
department_name_to_add_to = input("\nEnter the name of the department to add a Hiter to: ")
for department in departments:
    if department_name_to_add_to.lower() == department._Department__namedepartment.lower():
        department.list_hiters()
        hiter_index_to_add = int(input("Enter the index of the Hiter to add: "))
        if 0 <= hiter_index_to_add < len(hiters):
            department.add_hiter_to_department(hiters[hiter_index_to_add])
        else:
            print("Invalid index.")
        break
else:
    print(f"Department with name '{department_name_to_add_to}' not found.")

