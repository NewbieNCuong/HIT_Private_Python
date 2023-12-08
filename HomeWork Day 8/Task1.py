class Pycon:
    id = 0
    def __init__(self, name = "", age = 0):
        Pycon.id += 1
        self.id = Pycon.id
        self.__name = name
        self.__age = age

    def Enter(self):
        self.__name = input("Enter name: ")
        self.__age = int(input("Enter age: "))
    
    def __str__(self):
        return f"Id: {self.id} || Name: {self.__name} || Age: {self.__age}"
    
    @classmethod
    def averAge(cls, arr):
        total_age = sum(i.__age for i in arr)
        return total_age / len(arr)


n = int(input("Enter numbers of pycon: "))
a = []
for i in range(n):
    tmp = Pycon()
    tmp.Enter()
    a.append(tmp)

for i in a:
    print(i)

average = Pycon.averAge(a)
print(f"Average of age: {average}")
