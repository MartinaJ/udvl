class Formula:
    def __init__(self, subformulas):
        self.subforms = subformulas

    def toString(self):
        pass

    def eval(self, i):
        pass

    def subf(self):
        return self.subforms


class Variable(Formula):
    def __init__(self, name):
        Formula.__init__(self, [])
        self.m_name = name

    def toString(self):
        return self.name()

    def eval(self, i):
        return i[self.name()]        

    def name(self):
        return self.m_name


class Negation(Formula):
    def __init__(self, orig):
        Formula.__init__(self, [orig])

    def originalFormula(self):
        return self.subf()[0]

    def toString(self):
        return '-' + self.originalFormula().toString()

    def eval(self, i):
        return not self.originalFormula().eval(i)

    
class Conjunction(Formula):
    def __init__(self, formuly):
        Formula.__init__(self, formuly)
        
    def toString(self):
        pole = []
        for formulka in self.subf():
            pole.append(formulka.toString())
        return '(' + '&'.join(pole) + ')'
    
    def eval(self, i):
        for formulka in self.subf():
            if formulka.eval(i) == False:
                return False
        return True


class Disjunction(Formula):
    def __init__(self, formuly):
        Formula.__init__(self, formuly)
        
    def toString(self):
        pole = []
        for formulka in self.subf():
            pole.append(formulka.toString())
        return '(' + '|'.join(pole) + ')'
    
    def eval(self, i):
        for formulka in self.subf():
            if formulka.eval(i) == True:
                return True
        return False

    
class Implication(Formula):
    def __init__(self, a, b):
        Formula.__init__(self, [a,b])

    def leftSide(self):
        return self.subf()[0]
    
    def rightSide(self):
        return self.subf()[1]
    
    def toString(self):
        return '(' + self.leftSide().toString() + '=>' + self.rightSide().toString() + ')'
      
    def eval(self, i):
        if (self.leftSide().eval(i) == True) and (self.rightSide().eval(i) == False):
            return False
        return True
    
   
class Equivalence(Formula):
    def __init__(self, a, b):
        Formula.__init__(self, [a,b])
        
    def leftSide(self):
        return self.subf()[0]
    
    def rightSide(self):
        return self.subf()[1]
        
    def toString(self):
        return '(' + self.leftSide().toString() + '<=>' + self.rightSide().toString() + ')'
    
    def eval(self, i):
        if ((self.leftSide().eval(i) == True) and (self.rightSide().eval(i) == False)) or ((self.leftSide().eval(i) == False) and (self.rightSide().eval(i) == True)):
            return False
        return True
