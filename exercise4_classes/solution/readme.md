# Rational Class

In the file [rational_solution.py](rational_solution.py), you can find the solution to the exercise, i.e., the class implementation.  
The file [tests.py](tests.py) contains the tests for the class.  
The package corresponds to Exercise 3.

## Structure of the Class (Documentation in a Nutshell)

The main idea of the class is to avoid using real numbers to implement arithmetic operations. This requires the use of the least common multiple (LCM, mcm in italian) and greatest common divisor (GCD, MCD in italian).

### Constructor(s)

First of all, the constructor of the class includes the implementation of an algorithm to approximate a real number as a rational number with a certain precision:

```python
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

```

The constructor first checks that the precision provided by the user is valid (i.e., \(0 < p < 1\)). After this validation, the algorithm is implemented.  
The attributes stored in the object include:  

- **Numerator and denominator**  
- **The real number provided by the user**  
- **The real number resulting from the approximation**  
- **The precision specified by the user**  
- **The prime factorization of the numerator and denominator**  

The prime factorization was included to reduce computational time during arithmetic operations by avoiding on-the-fly factorization.  

An alternative constructor has also been introduced, allowing a Rational object to be declared using only the numerator and denominator. In this case, the system precision of Python's float type is assumed.  


```python
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
```

### MCD and mcm Methods

To perform operations using mcm and MCD, I have implemented two methods: MCD and mcm.  
The underlying idea is straightforward:

1. Decompose two numbers into their prime factors.  
2. Create a dictionary that stores the frequency of each prime factor in the decomposition (via the _counter_elements function).  
3. Use a set to compute the union (for mcm) and intersection (for MCD) of the two dictionaries, based on the definitions of mcm and MCD.  
4. Compute the resulting value.  

The methods are designed to be as general as possible. The function arguments also allow the direct input of the prime factorizations of the two numbers, minimizing calls to the deco function in the package_excercise.  

```python
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

```

### Operators

The arithmetic operators behave as expected, following the classical rules for rational numbers, with the use of mcm and MCD.  
It is worth noting the implementation of validation checks:  

```python
        if isinstance(other,(int,float)):
            other = Rational(other,sys.float_info.epsilon)

```
this permit to use the operators also with integers and floats, thanks to a on-the-fly declaration of the corresponding rational.

## Tests

The [tests.py](tests.py) contains the tests of the class. Here is reported the code and the corresponding output:

```python
#!/usr/bin/python3

from rational_solution import Rational

#tests
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
    print(str(positive)+" + "+str(10)+" = "+str(positive+10))
    print(str(positive)+" - "+str(negative)+" = "+str(positive-negative))
    print(str(positive)+" - "+str(10)+" = "+str(positive-10))
    print(str(positive)+" * "+str(negative)+" = "+str(positive*negative))
    print(str(positive)+" * "+str(10)+" = "+str(positive*10))
    print(str(positive)+" / "+str(negative)+" = "+str(positive/negative)+"\n")
    print(str(positive)+" / "+str(10)+" = "+str(positive/10)+"\n")
    print(str(positive)+" == "+str(negative)+" "+str(positive==negative))
    print(str(positive)+" == "+str(10)+" "+str(positive==10))
    print(str(positive)+" != "+str(negative)+" "+str(positive!=negative))
    print(str(positive)+" != "+str(10)+" "+str(positive!=10))
    print(str(positive)+" < "+str(negative)+" "+str(positive<negative))
    print(str(positive)+" < "+str(10)+" "+str(positive<10))
    print(str(positive)+" > "+str(negative)+" "+str(positive>negative))
    print(str(positive)+" > "+str(10)+" "+str(positive>10))
    print(str(positive)+" <= "+str(negative)+" "+str(positive<=negative))
    print(str(positive)+" <= "+str(10)+" "+str(positive<=10))
    positive2 = Rational(6.44)
    print(str(positive)+" >= "+str(positive2)+" "+str(positive>=positive2)+"\n")

    #test hash and optional methods
    set_belo={positive, negative, positive2}
    print(str(set_belo))
    print("lower integer to "+str(positive)+" is "+str(positive.to_integer_low()))
    print("upper integer to "+str(negative)+" is "+str(negative.to_integer_upp()))

```
output:


```
-5.32 is -133/25 corresponding to -5.32 because of precision of conversion 1e-05
6.44 is 161/25 corresponding to 6.44 because of precision of conversion 1e-05
11.128273982 is 3817/343 corresponding to 11.128279883381925 because of precision of conversion 1e-05
0.0 is 0/1
-2.857142857142857 is -20/7 corresponding to -2.857142857142857 because of precision of conversion 2.220446049250313e-16

integer of 161/25 is 6
integer of -133/25 is -5
float of 161/25 is 6.44
float of -133/25 is -5.32
|-133/25| = 133/25
161/25 + -133/25 = 28/25
161/25 + 10 = 411/25
161/25 - -133/25 = 294/25
161/25 - 10 = -89/25
161/25 * -133/25 = -21413/625
161/25 * 10 = 322/5
161/25 / -133/25 = -23/19

161/25 / 10 = 161/250

161/25 == -133/25 False
161/25 == 10 False
161/25 != -133/25 True
161/25 != 10 True
161/25 < -133/25 False
161/25 < 10 True
161/25 > -133/25 True
161/25 > 10 False
161/25 <= -133/25 False
161/25 <= 10 True
161/25 >= 161/25 True

{rational( -5.32, precision= 1e-05 ), rational( 6.44, precision= 1e-05 )}
lower integer to 161/25 is 6
upper integer to -133/25 is -5


```







