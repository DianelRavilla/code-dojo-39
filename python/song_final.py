print("Lista 7 animales")
animales=[]
for i in range(eval(7)):
    animal_entrada = input()
    animales.append(animal_entrada)

def ultimaLinea():
    print("I don't know why she swallowed a " + animales[0] + " - perhaps she'll die!")

def primeraLinea(pos):
    print("There was an old lady who swallowed a " + animales[pos])

primeraLinea(0)
ultimaLinea()

primeraLinea(1)
print("That wriggled and wiggled and tickled inside her.")
print("She swallowed the " + animales[1]+ " to catch the " + animales[0])
ultimaLinea()

primeraLinea(2)
print("How absurd to swallow a " + animales[2])
print("She swallowed the " + animales[2]+ " to catch the " + animales[1])
print("She swallowed the " + animales[1]+ " to catch the " + animales[0])
ultimaLinea()

primeraLinea(3)
print("Fancy that to swallow a " + animales[3])
print("She swallowed the " + animales[3]+ " to catch the " + animales[2])
print("She swallowed the " + animales[2]+ " to catch the " + animales[1])
print("She swallowed the " + animales[1]+ " to catch the " + animales[0])
ultimaLinea()

primeraLinea(4)
print("What a hog, to swallow a dog! " + animales[4])
print("She swallowed the " + animales[4]+ " to catch the " + animales[3])
print("She swallowed the " + animales[3]+ " to catch the " + animales[2])
print("She swallowed the " + animales[2]+ " to catch the " + animales[1])
print("She swallowed the " + animales[1]+ " to catch the " + animales[0])
ultimaLinea()

primeraLinea(5)
print("I don't know how she swallowed a cow! " + animales[5])
print("She swallowed the " + animales[5]+ " to catch the " + animales[4])
print("She swallowed the " + animales[4]+ " to catch the " + animales[3])
print("She swallowed the " + animales[3]+ " to catch the " + animales[2])
print("She swallowed the " + animales[2]+ " to catch the " + animales[1])
print("She swallowed the " + animales[1]+ " to catch the " + animales[0])
ultimaLinea()

print("There was an old lady who swallowed a " + animales[6] + "\n ...She's dead, of course!")