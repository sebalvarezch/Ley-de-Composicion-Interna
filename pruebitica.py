import cmath
from math import sqrt
a = 10
b = 4
c = 7
mon = a+b
mon1 = a*b
m = 0


# Funciones que permiten el correcto desarrollo del programa


def select():

	while True:
		print("\n¿Desea conocer si se cumple Monoide Asociativo?\nIngrese 1 de ser así.\nIngrese 2 para salir.")

		try:
			seleccion = int(input("Ingrese la opción: "))

			if seleccion == 1:
				return seleccion
				break
			elif seleccion == 2:
				return seleccion
				break
			else:
				print("Ingrese un número que sea 1 ó 2, tal como se indicó anteriormente. Intente nuevamente")

		except ValueError:
			print("\nIngrese una opción válida. La misma debe ser numérica, 1 ó 2. Intente nuevamente.")

#Selección para Grupo
def select2(): 

	while True:
		print("\n¿Desea conocer si su expresión pertenece a un Grupo?\nIngrese 1 si la respuesta es afirmativa. \nIngrese 2 para salir")

		try:
			seleccion = int(input("Ingrese la opción deseada: "))
			if seleccion == 1:
				return seleccion
				break
			elif seleccion == 2:
				return seleccion
				break
			else:
				print("Ingrese un número válido, es decir, 1 ó 2. Intentelo nuevamente.")

		except ValueError:
			print("\nIngrese una opción que sea válida, recuerde que la misma debe ser numérica, 1 ó 2 respectivamente.")

#Selección para grupo Abeliano
def select3():

	while True:
		print("\n¿Desea conocer si su expresión pertenece a un Grupo Abeliano?\nIngrese 1 si es así. \nIngrese 2 para salir y finalizar el programa")

		try:
			seleccion = int(input("Ingrese la opción deseada: "))
			if seleccion == 1:
				return seleccion
				break
			elif seleccion == 2:
				return seleccion
				break
			else:
				print("Ingrese un número válido, es decir, 1 ó 2. Intentelo nuevamente.")

		except ValueError:
			print("\nIngrese una opción que sea válida, recuerde que la misma debe ser numérica, 1 ó 2 respectivamente.")

#Selección para Anillo
def select4():

	while True:

		print("\n¿Deseea conocer si su expresión cumple con los parámetros de ANILLO?\nIngrese 1 si es así.\nIngrese 2 para salir y finalizar el programa")

		try:
			seleccion = int(input("Ingresa la opción deseada: "))
			if seleccion == 1:
				return seleccion
				break
			elif seleccion == 2:
				return seleccion
				break

		except ValueError:
			print("\nIngrese una opción que sea válida, recuerde que la misma debe ser numérica, 1 ó 2 respectivamente.")

#Propiedades
def monoideA(e): # Funcion que demuestra existencia o no del monoide asociativo (a * b) * c = a * (b * c)  [(a * b)]
	#Reemplazando en asociativa

	aso = "(a * b)" # * c
	aso1 = "(a * c)"
	aso3 = "a * b"
	asoR = aso.replace("a * b", expresion) #Sustituyendo a * b por la expresión ingresada
	asoR2 = aso1.replace("a * c", expresion) #Sustituyendo a * c por la expresión ingresada
	asoR3 = asoR2.replace("b", "c")  #Sustituyendo b de la expresión ingresada por c
	asoR4 = asoR3.replace("a","b") #Sustituyendo a de la expresión ingresada por b
	
	#Aplicando segundo reemplazo.
	result = e.replace("b", "c")
	result2 = result.replace("a", asoR ) #2*(2*a - b) - c
	resultado = eval(result2)

	res = asoR.replace("b", "c")
	res1 = res.replace("a", "b")
	res2 = e.replace("b", res1)#2*a - (2*b - c)
	resultado2 = eval(res2)

	print("Procedimiento: \n")
	print("Tenemos que: [",e," = a * b ]")
	print("Aplicamos la propiedad asociativa: ")
	print("En la propiedad asociativa: (a * b) * c = a * (a * c) \n")
	print("Se demuestra:")
	print(asoR, " * c = a * ", asoR4)#primer paso: (2*a - b)  * c = a *  (2*b - c)
	print("Primera igualdad: ")
	print(" a = ", asoR)
	print(" b = c")
	print("Segunda igualdad: ")
	print(" a = a")
	print(" b = ", asoR4)
	print("Con esto podemos entender que: a * b\n")

	if (resultado == resultado2):
		print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
		print(result2, " = ", res2)
		print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
		print()
		print("Queda claro que la sigiente expresión:  (",e,")")
		print("SI CUMPLE, se trata de un monoide asociativo")
		print("Resultado numérico: ")
		print(resultado," = ",resultado2)
		return "1"

	else:
		print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
		print(result2, " = ", res2)
		print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
		print()
		print("Ha sido demostrado que la siquiente expresión: (",e,")")
		print("NO CUMPLE, NO ES monoide asociativo ")
		print("Resultado numerico: ")
		print(resultado," = ",resultado2)

def monoideB(e):
	#aplicamos remplazo en asociativa
	aso = "(a + b)"
	aso1 = "(a + c)"
	aso3 = "a + b"
	asoR = aso.replace("a + b", expresion)
	asoR2 = aso1.replace("a + c", expresion)
	asoR3 = asoR2.replace("b", "c")
	asoR4 = asoR3.replace("a","b")
	
	#aplicamos segundo reemplazo.
	result = e.replace("b", "c")
	result2 = result.replace("a", asoR ) #2*(2*a - b) - c
	resultado = eval(result2)

	res = asoR.replace("b", "c")
	res1 = res.replace("a", "b")
	res2 = e.replace("b", res1)#2*a - (2*b - c)
	resultado2 = eval(res2)

	#2*(2*a - b) - c  =  2*a - (2*b - c)

	print("Muestra del procedimiento: \n")
	print("Tenemos: [",e," = a + b ]")
	print("Aplicamos la propiedad asociativa. . . ")
	print("(a + b) + c = a + (a + c) \n")
	print("Se demuestra la propiedad: ")
	print(asoR, " + c = a + ", asoR4)#primer paso: (2*a - b)  + c = a +  (2*b - c)
	print("Primera igualdad: ")
	print(" a = ", asoR)
	print(" b = c")
	print("Segunda igualdad: ")
	print(" a = a")
	print(" b = ", asoR4)
	print("Es posible dar a entender que: a * b\n")

	if (resultado == resultado2):
		print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
		print(result2, " = ", res2)
		print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
		print()
		print("Se demuestra que la siguiente expresión (",e,")")
		print("SI CUMPLE, ES UN monoide asociativo ")
		print("Resultado numérico: ")
		print(resultado," = ",resultado2)
		return "1"

	else:
		print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
		print(result2, " = ", res2)
		print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
		print()
		print("Se demuestra que la siguiente ecueacion (",e,")")
		print("NO CUMPLE, NO SE TRATA DE UN monoide asociativo ")
		print("Resultado numerico: ")
		print(resultado," = ",resultado2)

#Copia de A
def monoideC(e): # Funcion que demuestra existencia o no del monoide asociativo (a * b) * c = a * (b * c)  [(a * b)]
	#Reemplazando en asociativa

	aso = "(a * b)" # * c
	aso1 = "(a * c)"
	aso3 = "a * b"
	asoR = aso.replace("a * b", e) #Sustituyendo a * b por la expresión ingresada
	asoR2 = aso1.replace("a * c", e) #Sustituyendo a * c por la expresión ingresada
	asoR3 = asoR2.replace("b", "c")  #Sustituyendo b de la expresión ingresada por c
	asoR4 = asoR3.replace("a","b") #Sustituyendo a de la expresión ingresada por b
	
	#Aplicando segundo reemplazo.
	result = e.replace("b", "c")
	result2 = result.replace("a", asoR ) #2*(2*a - b) - c
	resultado = eval(result2)

	res = asoR.replace("b", "c")
	res1 = res.replace("a", "b")
	res2 = e.replace("b", res1)#2*a - (2*b - c)
	resultado2 = eval(res2)

	print("Procedimiento: \n")
	print("Tenemos que: [",e," = a * b ]")
	print("Aplicamos la propiedad asociativa: ")
	print("En la propiedad asociativa: (a * b) * c = a * (a * c) \n")
	print("Se demuestra:")
	print(asoR, " * c = a * ", asoR4)#primer paso: (2*a - b)  * c = a *  (2*b - c)
	print("Primera igualdad: ")
	print(" a = ", asoR)
	print(" b = c")
	print("Segunda igualdad: ")
	print(" a = a")
	print(" b = ", asoR4)
	print("Con esto podemos entender que: a * b\n")

	if (resultado == resultado2):
		print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
		print(result2, " = ", res2)
		print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
		print()
		print("Queda claro que la sigiente expresión:  (",e,")")
		print("SI CUMPLE, se trata de un monoide asociativo")
		print("Resultado numérico: ")
		print(resultado," = ",resultado2)
		return 1
	else:
		print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
		print(result2, " = ", res2)
		print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
		print()
		print("Ha sido demostrado que la siquiente expresión: (",e,")")
		print("NO CUMPLE, NO ES monoide asociativo ")
		print("Resultado numerico: ")
		print(resultado," = ",resultado2)

def monoideD(e):
	#aplicamos remplazo en asociativa
	aso = "(a + b)"
	aso1 = "(a + c)"
	aso3 = "a + b"
	asoR = aso.replace("a + b", e)
	asoR2 = aso1.replace("a + c", e)
	asoR3 = asoR2.replace("b", "c")
	asoR4 = asoR3.replace("a","b")
	
	#aplicamos segundo reemplazo.
	result = e.replace("b", "c")
	result2 = result.replace("a", asoR ) #2*(2*a - b) - c
	resultado = eval(result2)

	res = asoR.replace("b", "c")
	res1 = res.replace("a", "b")
	res2 = e.replace("b", res1)#2*a - (2*b - c)
	resultado2 = eval(res2)

	#2*(2*a - b) - c  =  2*a - (2*b - c)

	print("Muestra del procedimiento: \n")
	print("Tenemos: [",e," = a + b ]")
	print("Aplicamos la propiedad asociativa. . . ")
	print("(a + b) + c = a + (a + c) \n")
	print("Se demuestra la propiedad: ")
	print(asoR, " + c = a + ", asoR4)#primer paso: (2*a - b)  + c = a +  (2*b - c)
	print("Primera igualdad: ")
	print(" a = ", asoR)
	print(" b = c")
	print("Segunda igualdad: ")
	print(" a = a")
	print(" b = ", asoR4)
	print("Es posible dar a entender que: a * b\n")

	if (resultado == resultado2):
		print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
		print(result2, " = ", res2)
		print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
		print()
		print("Se demuestra que la siguiente expresión (",e,")")
		print("SI CUMPLE, ES UN monoide asociativo ")
		print("Resultado numérico: ")
		print(resultado," = ",resultado2)
		return 1

		#Retornando 1 para la comprobación de grupo abeliano

	else:
		print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
		print(result2, " = ", res2)
		print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
		print()
		print("Se demuestra que la siguiente ecueacion (",e,")")
		print("NO CUMPLE, NO SE TRATA DE UN monoide asociativo ")
		print("Resultado numerico: ")
		print(resultado," = ",resultado2)

def neutro(e): # elemento neutro
	for i in e:
		if (i == "/") :
			print("La división no es un operador alojado por el Elemento Neutro.")
			return 0
		elif ( i == "-") or (i == "+"):
			res2 = eval(e)
			neutro = 0
			neutro2 = 'e'
			print("\nProcedimiento :")
			print("Se aplica Elemento Neutro. . . ")
			print("Procedimiento canónico. . .")
			print("a + b => a + ae = a")
			print("ae = a - a")
			print("ae = 0")
			print("e = 0/a")
			print("Propiedad:")
			print("(",e,") + " ,neutro2," = ")
			print("Entones, la igualdad es. . . ")
			print("El valor de la expresión ingresada es: ",res2)
			res = res2 + neutro
			if (res == res2):
				print("\n≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
				print(e, "+", neutro2)
				print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡\n")
				print("Expresión (",e,") posee Elemento Neutro en la Adición (a + b)")
				return 1
			else:
				print("Expresión (",e,") no posee Elemento Neutro en la Adición (a + b)")
				return 0
		elif (i == "*"):
			res2 = eval(e)
			neutro = 1
			neutro2 = 'e'
			print("Aplicando Elemento Neutro. . .")
			print("(",e,") * ",neutro2,"")
			res = res2 * neutro
			print("Entonces, la igualdad es: ")
			if (res == res2):
				print("\n≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
				print(e, "*", neutro2)
				print("\n≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡\n")
				print("La expresión (",e,") SI posee Elemento Neutro en la MULTIPLICACIÓN (a * b)")
				print()
				return 1
			else:
				print("\nLa expresión (",e,") NO posee Elemento Neutro en MULTIPLICACIÓN (a * b)")
				print()
				return 0

# Elemento inverso
def inverso(e):
	#Aditivo inverso
	#Debe dar el elemento neutro
	Inver = "(-(a + b))"
	Inver = Inver.replace("a + b", e)
	res = eval(Inver)
	res2 = eval(e)
	#Aditivo multiplicativo
	Inver2 = "(1/(a + b))"
	Inver2 = Inver2.replace("a + b", e)
	res3 = eval(Inver2)
	res4 = eval(e)
	resT = (res4 * res3)

	print("PROCESO ADITIVO: ")

	print("\n≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
	print("PROCESO MULTIPLICATIVO: ")
	print("Aplicando Elemento Inverso. . . ")

	print("\nTenemos que, la igualdad es: ")
	if ((res2 + res) == 0) and (resT == 1):
		print("\n≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
		print(e, "+", Inver, "ADITIVO")
		print(e, "+", Inver2, "MULTIPLICATIVO")
		print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡\n")
		print("La expresión (",e,") SI tiene Elemento Inverso ADITIVO [",Inver,"]")
		print("La expresión (",e,") SI tiene Elemento Inverso MULTIPLICATIVO [",Inver2,"]")
		print()
		return 1
		# retornando 1 para la comprobacion de grupo abeliano
	else:
		print("La expresión (",e,") NO tiene Elemento Inverso ADITIVO ó MULTIPLICATIVO \n[",Inver,"] o [",Inver2,"]")
		print()
		return 0

 # Verificando si es grupo
def conmutatividad(e): #Grupo
	conmu = e.replace("b","l")
	conmu = conmu.replace("a","b")
	conmu = conmu.replace("l","a")

	print("Procedimiento: ")
	print("Tenemos: (",e," = b + a )")
	print("Aplicamos la propiedad conmutativa: ")
	print("Tenemos: a + b = a + b")
	print("Se demuestra: ")
	print(e, " = ", conmu)
	print("La igualdad es: ")

	if (eval(e) == eval(conmu)):
		print("\n≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
		print(eval(e), " = ", eval(conmu))
		print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡\n")
		print("La siquiente expresión (",e,")")
		print("SI CUMPLE con la Propiedad Conmutativa.")
		print("\nSI es un Grupo Abeliano.")
		print("Resultado: ")
		print(eval(e)," = ",eval(conmu))
	else:
		print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡\n")
		print(eval(e), " = ", eval(conmu))
		print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡\n")
		print("Se de muestra que la siquiente ecueacion (",e,")")
		print("NO CUMPLE con la Propiedad Conmutativa.")
		print("NO es un Grupo Abeliano.")
		print("\nResultado: ")
		print(eval(e)," = ",eval(conmu))

# Obteniendo valor de la segunda expresión 
def segunda_expr():

	while True:

		try:
			expr2 = input("Ingrese la segunda expresión: ")
			resultado2 = eval(expr2)
			return expr2

		except ValueError:
			print("La segunda expresión no es válida. Ingrese nuevamente.")

# Función para la elaboración de la propiedad distributiva
def propiedadDistributiva(e1, e2):
	#a*(b+c)
	elm = e1.replace("b","c")
	elm = elm.replace("a","b")
	dist1 = e2.replace("b","("+elm+")")
	r1 = eval(dist1)

	#a*b+a*c
	dist2 = "(a * b) + (a*c)"
	elm1 = e2.replace("b","c")
	dist2 = dist2.replace("a*b",e2)
	dist2 = dist2.replace("a*c",elm1)
	r2 = eval(dist2)
	print("\nPropiedad Distributiva")
	print(dist1, "debe ser igual a ",dist2)

	if (r1 == r2):
		print("\nLa expresión es anillo.")
		return 1
		# retornando 1 para la comprobacion de cuerpo
	else:
		print("La expresión no es anillo.")

# Comprobación de números reales.
def reales(e):
	#Obteniendo valor numérico de la expresión ingresada
	numerico = eval(e)

	#Comprobando si es real
	if (isinstance(numerico, complex)):
		print("No cumple la Ley de Composición Interna. NO es un número real.")
		return 0
	else:
		print("Cumple con la Ley de Composición Interna. Es un número real.")
		return 1

#Inicio del programa.
print("\nBienvenido a Ley de Composición Interna.\nPrograma elaborado por Sebastián Álvarez y Sebastián Avendaño.\nEstructuras Discretas I. UJAP.")
while True:
	try:
		print("\nEscoja el conjunto numérico con el que desea trabajar:\nTipee 1 para entero.\nTipee 2 para natural\nTipee 3 para real.\nTipee 4 para complejo")
		opcion = int(input("\nIngrese el número correspondiente: "))
		if opcion >= 1 and opcion <= 4:
			##print("San se acabó") En caso de que se cumpla la condición dada, se acaba al ciclo y se procede con la comprobación de la operación
			break
		else:
			print("¡Debe ser un valor entre 1 y 4! Intente nuevamente.")
	except ValueError:
		print("Ingrese un valor válido. Recuerde que debe ser numérico, del 1 al 4 respectivamente.\nIntente nuevamente.")
		#Manejo de excepciones para evitar que el usuario ingrese un valor diferente a uno numérico.
##print("Fuera del ciclo ya.")

#Entero
if opcion == 1:

	while True:
		print("\nHa escogido trabajar con el conjunto de los números enteros. Por favor, ingrese la expresión matemática a comprobar:")

		try:
			expresion = input("Ingrese la expresión: ")
			resultado = eval(expresion)

			if (isinstance(resultado,int)):
				print("La expresión ingresada (",expresion,") cumple la Ley de Composición Interna. \nSu resultado es: ",resultado,"")

				if (select() == 1): #Pregunta si desea comprobar la propiedad asociativa
					monoideA(expresion)
					monoideB(expresion)

					if (select2() == 1): #Pregunta si desea comprobar si es grupo
						if (neutro(expresion) == 1):
							if (inverso(expresion) == 1):
								if (select3() == 1):
									conmutatividad(expresion)

									if (select4() == 1): #Pregunta si desea conocer ANILLO
										expr2 = segunda_expr()
										print("La segunda expresión es: ",expr2)
										resultado2 = eval(expr2)
										if (isinstance(resultado2, int)):
											print("La segunda expresión cumple con la Ley de Composición Interna")
											print("Comprobando MONOIDE ASOCIATIVO. . .")

											if (select() == 1):
												if (monoideC(expr2) == 1):
													m+=1
												if (monoideD(expr2) == 1):
													m+=1	
												if (propiedadDistributiva(expresion, expr2) == 1):
													m+=1
												if (m == 2):
													print("\nLa segunda expresión ingresada es SEMIGRUPO.")
												if (m ==3 ):
													print("\nHay CUERPO. Se cumple tanto GRUPO ABELIANO como PROPIEDAD DISTRIBUTIVA")
												print("Fin del programa.")
										else:
											print("La segunda expresión NO cumple con la Ley de Composición Interna")
										break #Fin del ciclo
								else:
									print("No es Grupo Abeliano. Fin del programa.")
									break
							else:
								print("No se cumple el Elemento Inverso. No pertenece. Fin del programa.")
								break
						else:
							print("No se cumple el Elemento Neutro. No pertenece. Fin del programa")
							break
					else:
						print("Fin del programa.")
						break
				else:
					print("Fin del programa.")
					break
			else:
				print("La expresión ingresada (",expresion,") NO cumple la Ley de Composición Interna. \nSu resultado es: ",resultado," ")
				break
		except NameError:
			print("Expresión ingresada no es válida. Por favor, intente nuevamente.")

#Natural
elif opcion == 2:

	while True:
		print("\nHa escogido trabajar con el conjunto de los números naturales. Por favor, ingrese la expresión matemática a comprobar:")

		try:
			expresion = input("Ingrese la expresión: ")
			resultado = eval(expresion)

			if (resultado >= 0 and isinstance(resultado,int)):
				print("La expresión (",expresion,") cumple con la Ley de Composición Interna.")
				print("Resultado: ",resultado)

				if (select() == 1):
					monoideA(expresion)
					monoideB(expresion)

					if (select2() == 1 ):
						if (neutro(expresion) == 1):
							if (inverso(expresion) == 1):
								print("\nPertenece a grupo.")

								if (select3() == 1):
									conmutatividad(expresion)

									if (select4() == 1):
										expr2 = segunda_expr()
										print("La segunda expresión es: ",expr2)
										resultado2 = eval(expr2)

										if (resultado2 >= 0 and isinstance(resultado2, int)):
											print("La segunda expresión cumple con la Ley de Composición Interna")
											if (select() == 1): 
												if (monoideC(expr2) == 1):
													m+=1
												if (monoideD(expr2) == 1):
													m+=1	
												if (propiedadDistributiva(expresion, expr2) == 1):
													m+=1
												if (m == 2):
													print("\nLa segunda expresión ingresada es SEMIGRUPO.")
												if (m == 3):
													print("Hay CUERPO. Se cumple tanto Grupo Abeliano como Propiedad Distributiva")
												print("Fin del programa.")

										else:
											print("La segunda expresión NO cumple con la Ley de Composición Interna")

									break
								else:
									print("Fin del programa.")
									break
							else:
								print("No se cumple Elemento Inverso. No pertenece. Fin del programa.")
						else:
							print("No se cumple Elemento Neutro. No pertenece. Fin del programa.")
							break

					else:
						print("Fin del programax.")
						break
				else:
					print("Fin del programa.")
					break
			else:
				print("La expresión (",expresion,") no cumple con la Ley de Composición Interna.")
				print("Resultado: ",resultado)
				print("Fin del programa.")
				break
		except NameError:
			print("Expresión ingresada no es válida, intente nuevamente.")

#Real
elif opcion == 3:

	while True:
		print("\nHa escogido trabajar con el conjunto de los números reales. Por favor, ingrese la expresión matemática a comprobar: ")

		try:
			expresion = input("Ingrese la expresión: ")
			resultado = eval(expresion)
			if (isinstance(resultado,complex)):
				print("La expresión ingresada (",expresion,") NO cumple con la Ley de Composición Interna.")
				print("Resultado: ",resultado)
			else:
				print("La expresión ingresada (",expresion,") cumple con la Ley de Composición Interna.")
				print("Resultado: ",resultado)
				if (select() == 1):
					monoideA(expresion)
					monoideB(expresion)
					if (select2() == 1):
						if (neutro(expresion) == 1):
							if (inverso(expresion) == 1):
								if (select3() == 1):
									conmutatividad(expresion)

									if (select4() == 1):
										expr2 = segunda_expr()
										print("La segunda expresión es: ",expr2)
										resultado2 = eval(expr2)
										print("Resultado numérico de la segunda expresión: ",resultado2)
										print("Comprobando si cumple Ley de Composición Interna. . .")

										if (reales(expr2) == 1):
											if (select() == 1): 
												if (monoideC(expr2) == 1):
													m+=1
												if (monoideD(expr2)	== 1):
													m+=1
												if (propiedadDistributiva(expresion, expr2) ==1):
													m+=1
												if (m == 2):
													print("\nLa segunda expresión ingresada es SEMIGRUPO.")
												if (m == 3):
													print("\nHay CUERPO. Se cumple tanto Grupo Abeliano como Propiedad Distributiva")
												print("\nFin del programa.")
												break	
										else:
											print("Fin del programa.")
											break
									else:
										break
								else:
									print("Fin del programa.")
									break
							else:
								print("No se cumple Elemento Inverso. No pertenece. Fin del programa.")
								break
						else:
							print("No se cumple Elemento Neutro. No pertenece. Fin del programa")
							break
					else:
						print("Fin del programa")
						break
				else:
					print("La expresión ingresada (",expresion,") NO cumple con la Ley de Composición Interna.")
					print("Resultado: ",resultado)
					print("Fin del programa.")
					break
		except NameError:
			print("Expresión ingresada no es válida, intente nuevamente.")

#Complejos
elif opcion == 4:

	while True:
		print("\nHa escogido trabajar con el conunto de los números complejos. Por favor, ingrese la expresión matemática a comprobar")

		try:
			expresion = input("Ingrese la expresión: ")
			resultado = eval(expresion)
			if (isinstance(resultado, complex)):
				print("La expresión ingresada (",expresion,") cumple con la Ley de Composición Interna.")
				print("Resultado: ",resultado)

				if (select() == 1):
					monoideA(expresion)
					monoideB(expresion)

					if (select2() == 1):
						if (neutro(expresion) == 1):
							if (inverso(expresion) == 1):
								if (select3() == 1):
									conmutatividad(expresion)

									if (select4() == 1):
										expr2 = segunda_expr()
										print("La segunda expresión es: ",expr2)
										resultado2 = eval(expr2)
										if (isinstance(resultado2, complex)):
											print("La segunda expresión cumple con la Ley de Composición Interna")

											if (select() == 1): 
												if (monoideC(expr2) == 1):
													m+=1
												if (monoideD(expr2) == 1):
													m+=1	
												if (propiedadDistributiva(expresion, expr2) == 1):
													m+=1
												if (m == 2):
													print("\nLa segunda expresión ingresada es SEMIGRUPO.")
												if (m == 3):
													print("\nHay CUERPO. Se cumple tanto Grupo Abeliano como Propiedad Distributiva.")
												print("\nFin del programa.")
									print("Fin del programa.")
									break
							else:
								print("\nNo se cumple Elemento Inverso. No pertenece. Fin del programa.")
								break
						else:
							print("\nNo se cumple Elemento Neutro. No pertenece. Fin del programa.")
							break
					else:
						print("Fin del programa.")
						break
				else:
					print("Fin del programa.")
					break
				print("Fin del programa.")
				break
			else:
				print("La expresión ingresada (",expresion,") NO cumple con la Ley de Composición Interna.")
				print("Resultado: ",resultado)
				print("Fin del programa.")
				break
		except NameError:
			print("Expresión ingresada no es válida, intente nuevamente.")