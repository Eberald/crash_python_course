#!/usr/bin/python3

import math as mt
import sys
from deco import prime_division as pd

class Rational():
    """
    class representing the rational numbers
    """
    def __init__(self, num = 0, precision = 1.e-5) :
        """
        constructur of the class, convert num in a rational

        Parameters
        ----------
        num : float,int
            number to be converted in rational

        precision : float (1.e-5 default)
            precision of the conversion
        """

        #check precision range
        if precision < 0 or precision > 1 :
            print("Error: invalid precision")
            return None

        #algorithm rationals approximation
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

        #saving class object variables
        self.n, self.d = _n[_], _d[_]
        self.real, self.precision = float(num), float(precision)
        self.real_appr = float(self.n/self.d)
        self.deco_d = pd(abs(self.d))
        self.deco_n = pd(abs(self.n))
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
        #check reasonable denominator
        if d == 0:
            print("Error: denoiminator = 0")
            return None

        #to be consistent to the tratment of the main constructur, put negative
        #the numerator
        if d < 0 :
            d = -d
            n = n*(-1)

        #constructor
        if n == 0 :
            instance_rat = cls()
            instance_rat.n = n
            instance_rat.d = 1
            instance_rat.real = 0.
            instance_rat.real_appr = 0.
            #in this case, the precision is the float precision of python
            instance_rat.precision = sys.float_info.epsilon
            instance_rat.deco_d = pd(abs(1))
            instance_rat.deco_n = pd(abs(n))
            return instance_rat
        else:
            instance_rat = cls()
            _MCD = cls.MCD(n,d)
            instance_rat.n = int(n/_MCD)
            instance_rat.d = int(d/_MCD)
            instance_rat.real = float(n) / float(d)
            instance_rat.real_appr = float(n) / float(d)
            #in this case, the precision is the float precision of python
            instance_rat.precision = sys.float_info.epsilon
            instance_rat.deco_d = pd(abs(int(d/_MCD)))
            instance_rat.deco_n = pd(abs(int(n/_MCD)))
            return instance_rat              
    



    #function used for the class arithmetical procedures
    @classmethod
    def _counter_elements(cls, numbers : list) -> dict :
        """
        create a dictionary that count the number of same elements
        present. Used for the mcm and MCD computation

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
    def mcm(cls, obj1 : int, obj2 : int, deco1 = [], deco2 = []) -> int :
        """
        compute the mcm given two numbers int.

        Parameters
        ----------
        obj1 : int
        obj2 : int
        deco1 : list
            this one in case of objects and not number, to make fast the
            arithmetic operations giving the prime decomposition
            (self variable of the class objects). Null list if not. 
        deco2 : list
            this one in case of objects and not number, to make fast the
            arithmetic operations giving the prime decomposition
            (self variable of the class objects). Null list if not.            

        Returns
        -------
        mcm : int
            mcm for the two denominators
        """

        mcm = 1
        _d1_deco, _d2_deco = [], []

        #check if present already the decomposition
        #reduce computation time
        if deco1 != [] and deco2 != []:
            _d1_deco = deco1
            _d2_deco = deco2
        else:
            _d1_deco = pd(abs(obj1))
            _d2_deco = pd(abs(obj2))
        
        _c1 = cls._counter_elements(_d1_deco)
        _c2 = cls._counter_elements(_d2_deco)
        #union because mcm take all the prime numbers of decomposition
        #maximum one in frequency
        _primes_c1c2 = set(_c1.keys()).union(set(_c2.keys()))

        #cycle for getting the maximum prime present between the two
        #decomposed numbers, and compute mcm
        for _number in _primes_c1c2:
            _element_freq_1 = _c1.get(_number, 0)
            _element_freq_2 = _c2.get(_number, 0)
            _maximum_freq = max(_element_freq_1, _element_freq_2)

            for _i in range(_maximum_freq):
                mcm *= _number

        return mcm

    #MCD computation
    @classmethod
    def MCD(cls, obj1 : int, obj2 : int, deco1 = [], deco2 = []) -> int :
        """
        compute the MCD given two numbers int.
    
        Parameters
        ----------
        obj1 : int
        obj2 : int
        deco1 : list
            this one in case of objects and not number, to make fast the
            arithmetic operations giving the prime decomposition
            (self variable of the class objects). Null list if not. 
        deco2 : list
            this one in case of objects and not number, to make fast the
            arithmetic operations giving the prime decomposition
            (self variable of the class objects). Null list if not. 
    
        Returns
        -------
        MCD : int
            MCD for the two denominators
        """
    
        MCD = 1
        _d1_deco, _d2_deco = [], []

        #check if present already the decomposition
        #reduce computation time       
        if deco1 != [] and deco2 != []:
            _d1_deco = deco1
            _d2_deco = deco2
        else:
            _d1_deco = pd(abs(obj1))
            _d2_deco = pd(abs(obj2))
            
        _c1 = cls._counter_elements(_d1_deco)
        _c2 = cls._counter_elements(_d2_deco)
        #intersection because MCD take the prime present in both the 
        #decomposition the minimum one
        _primes_c1c2 = set(_c1.keys()).intersection(set(_c2.keys()))

        #same mcm but getting the minimum one
        for _number in _primes_c1c2:
            _element_freq_1 = _c1.get(_number, 0)
            _element_freq_2 = _c2.get(_number, 0)
            _maximum_freq = min(_element_freq_1, _element_freq_2)
    
            for _i in range(_maximum_freq):
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
        _mcm = self.mcm(self.d,other.d,self.deco_d,other.deco_d)
        _num = int((_mcm/self.d)*self.n+(_mcm/other.d)*other.n)
        return self._initnumdem(_num,_mcm)

    def __sub__(self, other) -> "Rational" :
        """
        return the subtraction of two rational
        """
        _mcm = self.mcm(self.d,other.d,self.deco_d,other.deco_d)
        _num = int((_mcm/self.d)*self.n-(_mcm/other.d)*other.n)
        return self._initnumdem(_num,_mcm)

    def __mul__(self, other) -> "Rational" :
        """
        return the multiplication of two rational
        """
        _MCD_up = self.MCD(self.d,other.n,self.deco_d,other.deco_n)
        _MCD_down = self.MCD(self.n,other.d,self.deco_n,other.deco_d)
        _num = int((self.n/_MCD_down) * (other.n/_MCD_up))
        _den = int((self.d/_MCD_up) * (other.d/_MCD_down))
        return self._initnumdem(_num,_den)

    def __truediv__(self, other) -> "Rational" :
        """
        return the division of two rational
        """
        _MCD_up = self.MCD(self.d,other.d,self.deco_d,other.deco_d)
        _MCD_down = self.MCD(self.n,other.n,self.deco_n,other.deco_n)
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
        """
        < operator
        """
        _diff = self - other
        return True if _diff.n<0 else False

    def __le__(self, other) -> bool :
        """
        <= operator
        """
        _diff = self - other
        return True if _diff.n<=0 else False

    def __ne__(self, other) -> bool :
        """
        != operator
        """
        return True if self.n!=other.n or self.d!=other.d else False

    def __gt__(self, other) -> bool :
        """
        > operator
        """
        _diff = self - other
        return True if _diff.n>0 else False

    def __ge__(self, other) -> bool :
        """
        >= operator
        """
        _diff = self - other
        return True if _diff.n>=0 else False

    #castings
    def __float__(self):
        """
        casting float number corresponding to rational (the precisios appr. corresponding)
        """
        return self.real_appr

    def __int__(self):
        """
        casting integer number, using the well-known approximations
        """
        if abs(self.real_appr-self.to_integer_low()) < 0.5:
            return self.to_integer_low()
        else:
            return self.to_integer_upp()

    #hash method
    def __hash__ (self) :
        """
        hash method for the class, if same numerator and same
        denominator, hash equal (always true because of semplification)
        of all the object applied in the class
        """
        return hash((self.n, self.d))

    #optional methods

    def to_integer_low (self) -> int :
        """
        return the approximation in defect of the rational
        """
        return int(self.real_appr//1)
    
    def to_integer_upp (self) -> int :
        """
        return the approximation in excess of the rational
        """
        return int(self.real_appr//1 + 1)
            
            


if __name__ == "__main__":
    #objects
    negative = Rational(-5.32)
    positive = Rational(6.44)
    very_long_float = Rational(11.128273982)
    zero = Rational(0)
    n_d_direct = Rational._initnumdem(100,-35)
 
    print(str(negative.real)+" is "+str(negative)+" corresponding to " \
    +str(negative.real_appr)+" because of precision of conversion "+str(negative.precision))
    
    print(str(positive.real)+" is "+str(positive)+" corresponding to " \
    +str(positive.real_appr)+" because of precision of conversion "+str(positive.precision))
    
    print(str(very_long_float.real)+" is "+str(very_long_float)+" corresponding to " \
    +str(very_long_float.real_appr)+" because of precision of conversion "+str(very_long_float.precision))
    
    print(str(zero.real)+" is "+str(zero))
    
    print(str(n_d_direct.real)+" is "+str(n_d_direct)+" corresponding to " \
    +str(n_d_direct.real_appr)+" because of precision of conversion "+str(n_d_direct.precision)+"\n")

    #test castings
    print("integer of "+str(positive)+" is "+str(int(positive)))
    print("integer of "+str(negative)+" is "+str(int(negative)))
    print("float of "+str(positive)+" is "+str(float(positive)))
    print("float of "+str(negative)+" is "+str(float(negative)))

    #tests arithmetic and comparison operators   
    print("|"+str(negative)+"| = "+str(abs(negative)))
    print(str(positive)+" + "+str(negative)+" = "+str(positive+negative))
    print(str(positive)+" - "+str(negative)+" = "+str(positive-negative))
    print(str(positive)+" * "+str(negative)+" = "+str(positive*negative))
    print(str(positive)+" / "+str(negative)+" = "+str(positive/negative)+"\n")
    print(str(positive)+" == "+str(negative)+" "+str(positive==negative))
    print(str(positive)+" != "+str(negative)+" "+str(positive!=negative))
    print(str(positive)+" < "+str(negative)+" "+str(positive<negative))
    print(str(positive)+" > "+str(negative)+" "+str(positive>negative))
    print(str(positive)+" <= "+str(negative)+" "+str(positive<=negative))
    positive2 = Rational(6.44)
    print(str(positive)+" >= "+str(positive2)+" "+str(positive>=positive2)+"\n")

    #test hash and optional methods
    set_belo={positive, negative, positive2}
    print(str(set_belo))
    print("lower integer to "+str(positive)+" is "+str(positive.to_integer_low()))
    print("upper integer to "+str(negative)+" is "+str(negative.to_integer_upp()))
    
