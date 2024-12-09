#!/usr/bin/python3

def fibonacci(n : int) -> list:
    """
    compute the fibonacci sequence up to the n-th term

    Parameters
    ----------
    n : int
        the n-th term of the sequence

    Returns
    -------
    : list
        a list with all the fibonacci sequence terms
    """
    _fibo=[0,1] #private

    if n==1:
        return _fibo[0]
    elif n==2:
        return _fibo
    else:
        while len(_fibo)<n:
            _fibo.append(_fibo[len(_fibo)-1]+_fibo[len(_fibo)-2])

        return _fibo


if __name__ == '__main__':
    try:
        n=int(input('insert positive integer\n'))
        if n<=0:
            print("Error: not valid input")
            quit()
        fibo=fibonacci(n)
        print(fibo)
    except ValueError:
        print("Error: not valid input")

    fibo_even = [fibo[i] for i in range(0,len(fibo)) if not i%2]
    fibo_odd = [fibo[i] for i in range(0,len(fibo)) if i%2]
    print("even "+str(fibo_even))
    print("odd "+str(fibo_odd))

    
            
