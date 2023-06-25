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
    
    def var_count(self):
        return len(self.k)
    
    def __str__(self):
        # Start building the string representation with the coefficient
        monomial_str = str(self.a)

        # Iterate over the exponents and add them to the string representation
        for exponent in self.k:
            monomial_str += f" * x^{exponent}"

        return monomial_str

a = Monomial(19,3,4,5,6)
print(a)