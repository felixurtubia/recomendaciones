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

def compararusuario(idcentral):
	id_vistas= matriz[idcentral,]
