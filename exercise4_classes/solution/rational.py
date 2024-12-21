#!/usr/bin/python3

import math as mt
from deco import prime_division as pd

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
        
        if precision < 0 or precision > 1 :
            print("Error: invalid precision")
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

    @classmethod
    def _initnumdem(cls, n: int, d: int) -> "Rational":
        """
        Alternative constructor to create a Rational instance directly
        from a numerator and denominator
            
        Parameters
        ----------
        n : int
            Numerator of the rational number
        d : int
            Denominator of the rational number
            numerator should be put !=0

        Returns
        -------
        instance_rat : Rational
            return an istance of the class
        """
        if d == 0:
            print("Error: denoiminator = 0")
            return None
            
        instance_rat = cls()
        instance_rat.n = n
        instance_rat.d = d
        instance_rat.real = float(n) / float(d)
        instance_rat.precision = None
        return instance_rat

    #function used for the class arithmetical procedures
    @classmethod
    def _counter_elements(cls, numbers : list) -> dict :
        """
        create a dictionary that count the number of same elements
        present. Used for the mcm computation

        Parameters
        ----------
        numbers : list
            list for which we creaty dictionary

        Returns
        -------
        count : dict
            dictionary contains number of elements
            in the list and the number of appearence
        """
        count = {}
        for _number in numbers:
            if _number not in count:
                count[_number] = 1
            else:
                count[_number] += 1

        return count

    #mcmc computation
    @classmethod
    def mcm(cls, obj1 : int, obj2 : int) -> int :
        """
        compute the mcm given two numbers int

        Parameters
        ----------
        obj1 : int
        obj2 : int

        Returns
        -------
        mcm : int
            mcm for the two denominators
        """

        mcm = 1
        _d1_deco = pd(obj1)
        _d2_deco = pd(obj2)
        _c1 = cls._counter_elements(_d1_deco)
        _c2 = cls._counter_elements(_d2_deco)
        _primes_c1c2 = set(_c1.keys()).union(set(_c2.keys()))

        for _number in _primes_c1c2:
            _element_freq_1 = _c1.get(_number, 0)
            _element_freq_2 = _c2.get(_number, 0)
            _maximum_freq = max(_element_freq_1, _element_freq_2)

            for _ in range(_maximum_freq):
                mcm *= _number

        return mcm

    #MCD computation
    @classmethod
    def MCD(cls, obj1 : int, obj2 : int) -> int :
            """
            compute the MCD given two numbers int
    
            Parameters
            ----------
            obj1 : int
            obj2 : int
    
            Returns
            -------
            MCD : int
                MCD for the two denominators
            """
    
            MCD = 1
            _d1_deco = pd(obj1)
            _d2_deco = pd(obj2)
            _c1 = cls._counter_elements(_d1_deco)
            _c2 = cls._counter_elements(_d2_deco)
            _primes_c1c2 = set(_c1.keys()).intersection(set(_c2.keys()))
    
            for _number in _primes_c1c2:
                _element_freq_1 = _c1.get(_number, 0)
                _element_freq_2 = _c2.get(_number, 0)
                _maximum_freq = min(_element_freq_1, _element_freq_2)
    
                for _ in range(_maximum_freq):
                    MCD *= _number
    
            return MCD
    


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

    def __abs__(self) -> "Rational" :
        """
        return the absolute value of the rational
        """
        return self._initnumdem(abs(self.n),abs(self.d))

    # arithmetical operators
   
    def __add__(self, other) -> "Rational" : 
        """
        return the sum of two rational
        """
        _mcm = self.mcm(self.d,other.d)
        _num = int((_mcm/self.d)*self.n+(_mcm/other.d)*other.n)
        return self._initnumdem(_num,_mcm)

    def __sub__(self, other) -> "Rational" :
        """
        return the subtraction of two rational
        """
        _mcm = self.mcm(self.d,other.d)
        _num = int((_mcm/self.d)*self.n-(_mcm/other.d)*other.n)
        return self._initnumdem(_num,_mcm)

    def __mul__(self, other) -> "type(self)" :
        """
        return the multiplication of two rational
        """
        _MCD_up = self.MCD(self.d,other.n)
        _MCD_down = self.MCD(self.n,other.d)
        _num = int((self.n/_MCD_down) * (other.n/_MCD_up))
        _den = int((self.d/_MCD_up) * (other.d/_MCD_down))
        return self._initnumdem(_num,_den)

    def __truediv__(self, other) -> "type(self)" :
        """
        return the division of two rational
        """
        _MCD_up = self.MCD(self.d,other.d)
        _MCD_down = self.MCD(self.n,other.n)
        _num = int((self.n/_MCD_down) * (other.d/_MCD_up))
        _den = int((self.d/_MCD_up) * (other.n/_MCD_down))
        return self._initnumdem(_num,_den)

    # comparison operators

    def __eq__(self, other) -> bool :
        """
        = operator, return true or false if equal or not
        """
        return True if self.n==other.n and self.d==other.d else False

    def __lt__(self, other) -> bool :
        _diff = self - other
        return True if _diff.n<0 else False

    def __le__(self, other) -> bool :
        _diff = self - other
        return True if _diff.n<=0 else False

    def __ne__(self, other) -> bool :
        return True if self.n!=other.n or self.d!=other.d else False

    def __gt__(self, other) -> bool :
        _diff = self - other
        return True if _diff.n>0 else False

    def __ge__(self, other) -> bool :
        _diff = self - other
        return True if _diff.n>=0 else False

    #hash method
    def __hash__ (self) :
        return hash((self.n, self.d))

    #optional methods

    def to_integer_low (self) -> int :
        """Documentation of function `to_integer_low`"""
        return int(self.real//1)
    
    def to_integer_upp (self) -> int :
        """Documentation of function `to_integer_upp`"""
        return int(self.real//1 + 1)
            
            


if __name__ == "__main__":
    ernesto = Rational(-5)
    franco = Rational(2.5)
    beppe = Rational(2.33)
    gigio = Rational(2.33)
    anto = franco
    pipi = Rational._initnumdem(10,-33)
    print(Rational.mcm(30,49))
    print(abs(pipi))
    print(ernesto)
    print(str(franco)+" + "+str(beppe)+" = "+str(franco+beppe))
    print(str(franco)+" - "+str(beppe)+" = "+str(franco-beppe))
    print(str(franco)+" * "+str(beppe)+" = "+str(franco*beppe))
    print(str(franco)+" / "+str(beppe)+" = "+str(franco/beppe))
    print(franco==beppe)
    print(franco!=beppe)
    print(beppe<franco)
    print(beppe>franco)
    print(franco<=anto)
    print(hash(beppe),hash(gigio))
    alfonso={gigio,beppe}
    print(str(alfonso))
    print(franco.to_integer_low())
    print(franco.to_integer_upp())
    
