
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
    if x^y == 1:
        x = 1
        c = 0
        return x,c
    elif x == 1 and y == 1:
        x = 1
        c = 1
        return state 
# to make a full gate we need to add filtering this is best done by first putting the two inputs through a xor gate to already filter their result where it changes is you then have to account for the carry in, so your creating two new possibilites. to check how the carry could be activated ( a +b B+c or a and b.)
# basically your nesting the half adders and once 2bits are on or like an adder should carry, it turns off so that the next adder knows "oh hey, i should add this place anymore sincec i added it before and its moved up"
#full adder 1 bit
def fa1b(x,y,c):
    a = ha1b(x,y)
    b = 
    
