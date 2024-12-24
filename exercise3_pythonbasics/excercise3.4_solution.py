#!/usr/bin/python3

def Eratosthenes_alghoritm(n : int) -> list:
    """
    Give as a set the list of the prime numbers until number n 

    Parameters
    ----------
    n : int
        maximum number reached in explore prime numbers

    Returns
    -------
    _prime : list
        a list containing all the prime number
    """
    if n == 1:
        _prime=[1]
        return _prime
    
    _prime=[int(i) for i in range(1,n+1)]
    _=1
    _current_prime=_prime[_]
    
    while list(_prime)[-1]!=_current_prime:
        _remove=[int(i) for i in range(2*_current_prime,n+1,_current_prime)]
        _prime=sorted(list(set(_prime)-set(_remove)))
        _=_+1
        _current_prime=_prime[_]

    return _prime
    

if __name__=="__main__":
    try:
        n=int(input('insert positive integer\n'))
        if n<=0:
            print("Error: not valid input")
            quit()
        Era=Eratosthenes_alghoritm(n)
        print(Era)
    except ValueError:
        print("Error: not valid input")
