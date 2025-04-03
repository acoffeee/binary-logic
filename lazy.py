
def menu():
    x = int(input("what would you like to do? \n 1: Binary to number 2: number to binary: "))
    if x == 1:
        B2N()
    else:
        N2B()
#answer = 
#b2n is binary to normal
# NP = 0
def B2N():
    x = str(input("type your string of binary to be translated: \n "))
    NP = 0
    output = 0
    x = reversed(x)
    for i in x:
        i = int(i)
        value = 2 ** NP
        NP += 1
        output += i * value
        #print(output)
    print(output)
#like yea theres the bin() function, but what fun is that lmao
def N2B():
    x = int(input("type your number to become binary: \n "))
    t = 0
    real_output=""
    output = ""
    x = int(x)
    while x > 0:
        t = x % 2 
        t=str(t)
        x = x // 2
        output = output + t
        #print(output)
    real_output ="".join(reversed(output))
    print(real_output)
 #ha = half adder and 1b is 1 bit
 # it takes 2 bits, runs them through a xor gate and if its a total of 1 then a light will go on other wise itll go to carry.
 
def ha1b(x,y):
    if x == 0 and y ==0:
        return x,y
    if x^y == 1:
        x = 1
        y = 0
        return x,y
    elif x == 1 and y == 1:
        x = 0
        y = 1
        return x,y
#full 1 bit adder
def fa1b(x,y,c):
    x,y = ha1b(0,1)
    a,b=ha1b(x,1)
    if y == 1 or b == 1:
        y = 1
        b = 1
    #x and y initaly are the two inputs, and c is the carry then they reasigned as x is sum and y is carry, which x and carry get put into nexcxt adder and y gets saved to compare.
