
def menu():
    x = int(input("what would you like to do? \n 1: Binary to number 2: number to binary: \n 3: add 2 binary strings together"))
    if x == 1:
        B2N()
    elif x ==2:
        N2B()
    elif x==3:
        Puttogether()
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
    x,y = ha1b(x,y)
    a,b=ha1b(x,c)
    if y == 1 or b == 1:
        y = 1
        b = 1
    return a,b
  
#make something that is able to add any length of strings using two lists i think is smartest then i can make one that actually is complete
def use_addr():
    setv = []
    str1 = input("what is your first set of bits? please adjust to be same size as second: \n")
    str2 = input("what is your second set of bits? please make same length as first: \n")
    if len(str1) != len(str2):
        print("bruddah get good at counting and make them the same damn length bruddah")
        use_addr()

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
    RA= []
    answer = ""
    c = 0
    for i in setv:
        x , y = setv[n]
        #print(x,y)
        if n == 0:
            x , c = ha1b(x,y)
            #print(x,c)
            x = str(x)
            RA.append(x)
            n +=1
            continue
        else: 
            x , c = fa1b(x,y,c)
            x = str(x)
            RA.append(x)
            n +=1
            continue
    c = str(c)
    RA.append(c)
    # bascially accounts for overflow carry or what ever idk 
    RA.reverse()
    print(RA)
    answer = answer.join(RA)
    print(answer)
    return answer

def Puttogether():
    setv= use_addr()
    print(setv)
    result = ua(setv)
    return result
#do say eqn = puttogether to do the thing and store or just regular. 
