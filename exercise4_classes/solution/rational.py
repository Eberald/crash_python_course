#!/usr/bin/python3

import math as mt

class Rational():
    """
    class representing the rational numbers
    """
    def __init__(self, num, precision = 1.e-5) :
        """
        constructur of the class, convert num in a rational

        Parameters
        ----------
        num : float,int
            number to be converted in rational

        precision : float (1.e-5 default)
            precision of the conversion
        """
        if precision < 0 or precision > 1 :
            print("Error: invalid precision")
            pass

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
        self.real, self.precision = num, precision
        pass

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
        return type(self)(abs(self.real),self.precision)
   
    def __add__(self, other) -> "type(self)" : 
        """
        return the sum of two rational
        """
        pass
            
            


if __name__ == "__main__":
    franco = Rational(-2.5)
    print(abs(franco))
    
    
