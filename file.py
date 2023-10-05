"""
print("Hello world")

x = 10
print(x)
print(type(x))
x = 10.1
print(type(x))
x = True
print(type(x))

x = input('Kolk denarja hočeš? ')
print('Dobiš',x, 'konc mesca')

for number in [1,2,3,4,5,6,7,8]:
    print(number)
"""

#funkcija ki vzame xyz in jih sesteje
def sestevalnik(x,y,z):
    rezultat = x+z+y
    return rezultat

print(sestevalnik(1,2,3))


#printej piramido

def piramida(visina):
    for x in range(visina):
        while x >= 0:

            print("*",end="")
            x-=1
        print("")

piramida(5)