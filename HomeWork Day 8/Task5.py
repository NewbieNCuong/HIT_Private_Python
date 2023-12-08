from Math import gcd
class Fraction:
    def __init__(self, Ts = 0, Ms = 1):
        self.__Ts = Ts
        self.__Ms = Ms

    @staticmethod
    def Transfer(self, a, b, c):
        return f"{c * a + b} / {c}"
        

class mixed:
    def __init_(self, Pn = 0, Ts = 0, Ms = 1):
        self.__Pn = Pn
        self.__Ts = Ts
        self.__Ms = Ms
    
    @staticmethod
    def Transfer2(self, a, b):
        if a < b: return f"0 / {a} / {b}"
        else:
            c = a % b
            d = a // b
            return f"{d} / {c} / {b}"


class Math(Fraction, mixed):
    def __init__(self, a):
        self.a = a
    
    def compact(self):
        pass