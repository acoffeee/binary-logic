x = str(input("enter first string of bits here to be added: "))
y = str(input("enter second string, should be same size as first string: "))
NP = 0
eqn1 = 0
eqn2 = 0
#answer = 
#b2n is binary to normal
def B2N(input,output):
    for i in input:
        i = int(i)
        value = 2 ** NP
        NP += 1
        output += i * value
        print(output)

def N2B(input,output):
    for i in 100:
        