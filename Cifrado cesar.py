
alfabeto_min = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z") #Alfabbeto en minisculas
alfabeto_May = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z") #Alfabbeto en ayusculas

salida="" #texto sobre el que trabajar

original=str(input("Introduce la oración a cifrar: "))	#texto
clave=int(input("Introduce el codigo: "))				#numero de posiciones a mover


for n in original:
	if n is " ":		#comprueba si es un espacio y lo añade
		salida+=" "
		
	elif n == n.upper():
		try:
			salida+=alfabeto_May[alfabeto_May.index(n)+clave]		#añade la letra que esta a x posiciones de n en el alfabeto
		except IndexError:	
			salida+=alfabeto_May[27-(alfabeto_May.index(n)+clave)]	#si llega al final de la lista vuelve al principio y se mueve el numero restante
		
	elif n == n.lower():
		try:
			salida+=alfabeto_min[alfabeto_min.index(n)+clave]		#añade la letra que esta a x posiciones de n en el alfabeto
		except IndexError:	
			salida+=alfabeto_min[27-(alfabeto_min.index(n)+clave)]	#si llega al final de la lista vuelve al principio y se mueve el numero restante
		

print(salida)	#imprime texto final