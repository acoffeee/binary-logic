
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
 

menu()

