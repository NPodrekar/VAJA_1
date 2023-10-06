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

###DOMAČA NALOGA1###

########### 1 ###########
n = int(input('Vnesite katerokoli celo število: '))

print("Spremenljivka je tipa ",type(n), "in ima vrednost " ,n)
n=float(n)
print("Spremenljivka je SEDAJ tipa ",type(n), "in ima vrednost " ,n)
print("\n")


########### 2 ###########
x = [0,1,2,3,4,5,6,7,8,9]
y = [9,8,7,6,5,4,3,2,1,0]
z = []

for i in range(len(x)):
    z.append(x[i]+y[i])
print(z)
print("\n")


########### 3 ###########
num1 = input("Vnesite celoštevilsko vrednost: ")
num2 = input("Vnesite še eno celoštevilsko vrednost: ")
num3 = input("Vnesite še zadnjo celoštevilsko vrednost: ")
print("Vnesli ste", num1, num2, "in", num3)
test = lambda num1, num2, num3:  num1 == num2 , num1 >= num3
print(test)
print("\n")


########### 4 ###########

def izpisi_trikotnik(visina):
    for x in range(visina):
        while x >= 0:

            print("*",end="")
            x-=1
        print("")



izpisi_trikotnik(5)
print("\n")