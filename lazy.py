
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
# to make a full gate we need to add filtering this is best done by first putting the two inputs through a xor gate to already filter their result where it changes is you then have to account for the carry in, so your creating two new possibilites. to check how the carry could be activated ( a +b B+c or a and b.)
# basically your nesting the half adders and once 2bits are on or like an adder should carry, it turns off so that the next adder knows "oh hey, i should add this place anymore sincec i added it before and its moved up"
#full adder 1 bit(x,y) #outputs into b the originor 
def fa1b(x,y,c):
    x,y = ha1b(0,1)
    a,b=ha1b(x,1)
    if y == 1 or b == 1:
        y = 1
        b = 1
    return a,b
#make something that is able to add any length of strings using two lists i think is smartest then i can make one that actually is complete
def use_addr():
    setv = []
    str1 = input("what is your first set of bits? please adjust to be same size as second")
    str2 = input("what is your second set of bits? please make same length as first")
    n = int(0)
    for i in str1:
        i = int(i)
        setv.append(i)
    for i in str2:
        i = int(i)
        setv[n] = setv[n],i
        n += 1
    setv.reverse()
    return setv

#stands for unlimited addr idk so future would be like use_addr then ua() where ua woould use use_adder output for its iputs and it basically should be
# it should decode and loop 1bit
def ua(setv):
    #n is simply a pointer to point at your placec.
    n = 0
    for i in setv:
        fa = ""
        x,y = setv[n]
        if n == 0:
            s,c = ha1b(x,y)
            s = str('{s}')
            fa.join(s)
            continue
        else: 
            s,c = fa1b(x,y,c)
            fa.join(s)
        n += 1
    return fa

setv= use_addr()
result = ua(setv)
print(result)