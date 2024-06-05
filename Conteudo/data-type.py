inum = 330
fnum = 33.0
st = "33"

newnum = inum + fnum #Inplicit Type Conversion

newnum = int(newnum) #Explicit Type Conversion. Casting Type é o mesmo, mas usando funções e pode ocorrer perda de memoria.
st = float(st)

print(type(st))
print(type(inum))
print(type(fnum))
print(type(newnum))