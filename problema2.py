from numpy import *

id_movies = dict()
usuarios = set()

arch = open('movies.dat')
for movie in arch:
	movie = movie.strip().split()
	id_movies[movie[0]] = ' '.join(movie[1:])
arch.close()

arch = open('u.dat')
for dato in arch:
	dato = dato.strip().split()
	usuarios.add(dato[0])
arch.close()

matriz = zeros((len(usuarios),len(id_movies)))

arch = open('u.dat')
for dato in arch:
	dato = dato.strip().split()
	matriz[int(dato[0])-1,int(dato[1])-1] = int(dato[2])
arch.close()

def correlacion(id_central,id_otro):
	rat_central=list(matriz[id_central,:])
	rat_otro=list(matriz[id_otro,:])
	comun=0
	largo=len(rat_central)
	prom_central=0
	prom_otro=0
	for i in range(largo):
		if rat_central[i] != 0 and rat_otro[i] != 0:
			comun += 1
		if rat_central[i] != 0:
			prom_central+=1
		if rat_central[i] != 0:
			prom_otro+=1

	if comun >= 2:
		suma_arriba=list()
		suma_abajo_1=list()
		suma_abajo_2=list()
		prom_central=sum(rat_central)/float(prom_central)
		prom_otro=sum(rat_otro)/float(prom_otro)
		for i in range(largo):
			rat_a=rat_central[i]
			rat_b=rat_otro[i]
			suma_arriba.append((rat_a-prom_central)*(rat_b-prom_otro))
			suma_abajo_1.append((rat_a-prom_central))
			suma_abajo_2.append((rat_b-prom_otro))
			suma_abajo_1=abs(sum(suma_abajo_1))
			suma_abajo_2=abs(sum(suma_abajo_2))
			return suma_arriba/(suma_abajo_1*suma_abajo_2)
	return 0

		

			

