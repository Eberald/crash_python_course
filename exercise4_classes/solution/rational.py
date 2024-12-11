#!/usr/bin/python3

import math as mt

class Rational():
    """
    class representing the rational numbers
    """
    def __init__(self, num = 0, precision = 1.e-5, n_def = 1, d_def = 0) :
        """
        constructur of the class, convert num in a rational

        Parameters
        ----------
        num : float,int
            number to be converted in rational

        precision : float (1.e-5 default)
            precision of the conversion

        n_def : int (1 default)
            numerator, if not inserted togheder with denominator
            is constructing the rational from num

        d_def : int (0 default)
            denominator, if choosen the construction with
            numerator should be put !=0
        """
        self.n=n_def
        self.d=d_def
        self.precision=precision
        self.real=num
        
        if precision < 0 or precision > 1 :
            print("Error: invalid precision")
            return None

        if d_def!=0 :
            self.n, self.d = n_def, d_def
            self.precision = precision
            self.real = float(n_def)/float(d_def)
            return None   

        _a = mt.floor(num)
        _decimals = num - _a
        _n = [1,_a]
        _d = [0,1]
        _ = 1

        while abs((_n[_] / _d[_]) - num) > precision:
            _a = mt.floor(1 / _decimals)
            _decimals = (1 / _decimals) - _a
            _n.append(_a * _n[_] + _n[_ - 1])
            _d.append(_a * _d[_] + _d[_ - 1])
            _ = _ + 1     

        self.n, self.d = _n[_], _d[_]
        self.real, self.precision = float(num), float(precision)
        return None

    def __str__(self) -> str :
        """
        print the ratinal number in the format n/d

        """
        return str(self.n)+"/"+str(self.d)

    def __repr__(self) -> str :
        """
        type of object, real number representing, precision
        """
        return "rational( "+str(self.real)+", precision= "+str(self.precision)+" )"

    def __abs__(self) -> "type(self)" :
        """
        return the absolute value of the rational
        """
        return type(self)(abs(self.real), self.precision)

    # arithmetical operators
   
    def __add__(self, other) -> "type(self)" : 
        """
        return the sum of two rational
        """
        return type(self)(self.real+other.real, min(self.precision, other.precision))

    def __sub__(self, other) -> "type(self)" :
        """
        return the subtraction of two rational
        """
        return type(self)(self.real-other.real, min(self.precision, other.precision))

    def __mul__(self, other) -> "type(self)" :
        """
        return the multiplication of two rational
        """
        return type(self)(self.real*other.real, min(self.precision, other.precision))

    def __truediv__(self, other) -> "type(self)" :
        """
        return the division of two rational
        """
        return type(self)(self.real/other.real, min(self.precision, other.precision))

    def __pow__(self, other) -> "type(self)" :
        """
        return the division of two rational
        """
        return type(self)(self.real**other.real, min(self.precision, other.precision))

    # comparison operators

    def __eq__(self, other) -> bool :
        """
        = operator, return true or false if equal or not
        """
        return True if self.n==other.n and self.d==other.d else False
            
            


if __name__ == "__main__":
    franco = Rational(2.5)
    beppe = Rational(2.33)
    anto = franco
    pippo = Rational(n_def=10,d_def=3)
    print(pippo)
    print(str(franco)+" + "+str(beppe)+" = "+str(franco+beppe))
    print(str(franco)+" - "+str(beppe)+" = "+str(franco-beppe))
    print(str(franco)+" * "+str(beppe)+" = "+str(franco*beppe))
    print(str(franco)+" / "+str(beppe)+" = "+str(franco/beppe))
    print(str(franco)+" ** "+str(beppe)+" = "+str(franco**beppe))
    print(franco==beppe)
    print(anto==franco)
    
    
