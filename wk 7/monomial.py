class Monomial:
    def __init__(self, a, *args):
        self.a = a
        self.k = args
        self.arg1 = 0
        self.arg2 = 0
    
    def is_monomial(self):
        for i in self.k.values():
            if i < 0 or isinstance(i, float):
                self.arg1 += 1
        if self.arg1 != 0:
            return False
        else:
            return True
    
    def highest_exponent(self):
        return max(self.k.values())
    
    def is_constant(self) -> bool :
        return sum(self.k) == 0
    
    def var_count(self):
        return len(self.k)
    
    def __str__(self):
        monomial_str = str(self.a)
        for i, exponent in enumerate(self.k):
            monomial_str += f"x_{i}^{exponent}"
        return monomial_str

a = Monomial(1,2,3,4)
print(a.__str__())
