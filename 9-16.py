#Definite = We know how many times we want it to run
#Indefinite = We don't know how many times it will run

#definite

for counter in range(0, 101, 5): #Definite
    print (counter) #You can use i but counter makes since

#indefinite
age = int(input("How old are you?"))
print (age)

while age < 0:
    print("you have not been born yet :0")
    age = int(input("How old are you?"))

    if (age == 15):
        continue