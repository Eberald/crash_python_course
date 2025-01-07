#!/usr/bin/python3

import package_excercise.prime as prime
import package_excercise.div as div

def prime_division(n : int) -> list:
    """
    returns the prime number decomposition of an integer n

    Parameters
    ----------
    n : int
        number for which I want the decomposition

    Returns
    -------
    _deco : list
        list of all the prime number of the decomposition
    """

    if n==0:
        return [0]

    _prime=prime.Eratosthenes_alghoritm(n)
    _divisor=[]
    for i in _prime:
        if div.division(n,i)[0]:
            _divisor.append(i)

    _=1
    _n=n
    _deco=[]
    while _n!=1:
        if not _n%_divisor[_]:
            _n=_n/_divisor[_]
            _deco.append(_divisor[_])
        else:
           _=_+1

    return _deco 


if __name__=="__main__":
    try:
        n=int(input('insert positive integer\n'))
        if n<0:
            print("Error: not valid input")
            quit()
        deco=prime_division(n)
        print(deco)
    except ValueError:
        print("Error: not valid input")
