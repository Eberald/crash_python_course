#!/usr/bin/python3

def division(n : int, m : int) -> tuple:
    """
    Check if n is divisble for m and vice-versa

    Parameters
    ----------
    n : int
        dividend/divisor
    m : int
        divisor/dividend

    Returns
    -------
    : tuple
        tuple of boolean associated to the divisibility
        (n%m,m%n) True divisible, False not divisible
    """
    if (n%m == 0 and m%n == 0):
        return (True,True)
    elif (n%m == 0 and m%n != 0): 
        return (True, False)
    elif (n%m != 0 and m%n == 0):
        return (False,True)
    else:
        return (False,False)

if __name__ == '__main__' :
    try:
        n = int(input("insert two integers\n"))
        m = int(input())
        if n<=0 or m<=0:
            print("Error: invalid input")
            quit()
        results=division(n,m)
        print(str(n)+"/"+str(m)+" "+str(results[0])+"\n"+str(m) \
            +"/"+str(n)+" "+str(results[1]))
    except ValueError:
        print("Error: invalid input")        
    
