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
	usuarios.add(int(dato[0]))
arch.close()

matriz = zeros((len(usuarios),len(id_movies)))

arch = open('u.dat')
for dato in arch:
	dato = dato.strip().split()
	matriz[int(dato[0])-1,int(dato[1])-1] = int(dato[2])
arch.close()

def compararusuario(idcentral):
	id_vistas= matriz[idcentral,]

def recomendacion_jaccard():
	maximo,aux = 0,[]
	user = int(raw_input('Usuario a recomendar(indice): '))
	for i in usuarios:
		if i == user:
			continue
		new_j,p1,p2 = jaccard(user,i)
		if maximo < new_j:
			parecido = i
			peli_parecido = p2
			maximo = new_j
	peli_parecido_rating = matriz[parecido,:]
	delta_peli = peli_parecido - p1
	maximo = 0
	for i in delta_peli:
		rating = peli_parecido_rating[i-1]
		if maximo <= rating:
			maximo = rating
			ind = i
	return id_movies[str(i)]

def jaccard(u1,u2):
	peliculas1,peliculas2 = set(),set()
	user1 = matriz[u1-1,:]
	user2 = matriz[u2-1,:]
	for i in range(len(user1)):
		if user1[i] != 0:
			peliculas1.add(i+1)
	for i in range(len(user2)):
		if user2[i] != 0:
			peliculas2.add(i+1)
	Jaccard = float(len(peliculas1 & peliculas2))
	Jaccard/= len(peliculas1|peliculas2)
	return Jaccard,peliculas1,peliculas2
