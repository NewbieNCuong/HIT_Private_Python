class Job:
    def __init__(self, codejob=0, namejob="", namemajor="", salary=0):
        self.__codejob = codejob
        self.__namejob = namejob
        self.__namemajor = namemajor
        self.__salary = salary

    def evaluate(self):
        average_score = sum(self.skills.values()) / len(self.skills)
        if average_score > 9.0:
            return "Rất phù hợp"
        elif average_score > 7.0:
            return "Phù hợp"
        elif average_score > 5.0:
            return "Tạm được"
        elif average_score > 3.0:
            lacking_skills = [skill for skill, score in self.skills.items() if score < 4.0]
            return f"Cần bổ sung thêm kiến thức ({', '.join(lacking_skills)})"
        else:
            return "Cần học lại kiến thức base"

    def __str__(self):
        return f"Job Name: {self.__namejob}\nMajor: {self.__namemajor}\nSalary: ${self.__salary}\nEvaluation: {self.evaluate()}"


class AI(Job):
    def __init__(self, codejob=0, namejob="", namemajor="", salary=0, pythonskill=0, mlskill=0, deepskill=0, mathskill=0):
        super().__init__(codejob, namejob, namemajor, salary)
        self.skills = {"Python": pythonskill, "ML": mlskill, "Deep": deepskill, "Math": mathskill}

    def __str__(self):
        return super().__str__() + f"\nSkills: {self.skills}"


class Backend(Job):
    def __init__(self, codejob=0, namejob="", namemajor="", salary=0, sqlskill=0, oopskill=0, apiskill=0, javaskill=0):
        super().__init__(codejob, namejob, namemajor, salary)
        self.skills = {"SQL": sqlskill, "OOP": oopskill, "API": apiskill, "Java": javaskill}

    def __str__(self):
        return super().__str__() + f"\nSkills: {self.skills}"


class Frontend(Job):
    def __init__(self, codejob=0, namejob="", namemajor="", salary=0, htmlskill=0, cssskill=0, nodejsskill=0, uxskill=0, uiskill=0):
        super().__init__(codejob, namejob, namemajor, salary)
        self.skills = {"HTML": htmlskill, "CSS": cssskill, "Nodejs": nodejsskill, "UX": uxskill, "UI": uiskill}

    def __str__(self):
        return super().__str__() + f"\nSkills: {self.skills}"


class Fullstack(Backend, Frontend):
    def __init__(self, codejob=0, namejob="", namemajor="", salary=0,
                 sqlskill=0, oopskill=0, apiskill=0, javaskill=0,
                 htmlskill=0, cssskill=0, nodejsskill=0, uxskill=0, uiskill=0):
        Backend.__init__(self, codejob, namejob, namemajor, salary,
                         sqlskill, oopskill, apiskill, javaskill)
        Frontend.__init__(self, codejob, namejob, namemajor, salary,
                          htmlskill, cssskill, nodejsskill, uxskill, uiskill)

    def __str__(self):
        return super().__str__()


ai_job = AI(codejob=1, namejob="AI Developer", namemajor="AI", salary=10000, pythonskill=9.5, mlskill=8.5, deepskill=9.0, mathskill=8.0)
frontend_job = Frontend(codejob=2, namejob="Frontend Developer", namemajor="Web Development", salary=8000, htmlskill=8.0, cssskill=9.0, nodejsskill=8.5, uiskill=9.0)
backend_job = Backend(codejob=3, namejob="Backend Developer", namemajor="Web Development", salary=8500, sqlskill=8.5, oopskill=9.0, apiskill=8.0, javaskill=8.0)
fullstack_job = Fullstack(codejob=4, namejob="Fullstack Developer", namemajor="Web Development", salary=9500,
                          sqlskill=8.0, oopskill=8.5, apiskill=8.5, javaskill=8.0,
                          htmlskill=9.0, cssskill=9.0, nodejsskill=8.5, uxskill=8, uiskill=8.5)


print("AI Job:")
print(ai_job)

print("\nFrontend Job:")
print(frontend_job)

print("\nBackend Job:")
print(backend_job)

print("\nFullstack Job:")
print(fullstack_job)
