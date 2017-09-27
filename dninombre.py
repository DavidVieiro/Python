# dos listas vacias
# nombres, dni
# 8 elementos cada lista
# se va a crear una lista nueva y en la lista nueva se van a visualizar los dni, segundo los nombres y por tercero todo el contenido de la lista.


a = []

b = []

a.append('pepe')
a.append('manuel')
a.append('jose')
a.append('marta')
a.append('carla')
a.append('david')
a.append('pablo')
a.append('juan')

b.append('12345678A')
b.append('12345678B')
b.append('12345678C')
b.append('12345678D')
b.append('12345678E')
b.append('12345678F')
b.append('12345678G')
b.append('12345678H')

c = [a, b]

print ""
print "--Lista de nombres--"
print c[0]
print ""

print "--Lista de DNIs--"
print c[1]
print ""

#c.extend(a)
#c.extend(b)

print "--Lista de Nombres y DNIs--"
print c
print ""
