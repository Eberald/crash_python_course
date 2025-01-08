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
