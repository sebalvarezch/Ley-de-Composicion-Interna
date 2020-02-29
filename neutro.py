a = 2
b = 10
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

expresion = input("Ingrese una expresión: \n")
neutro(expresion)

##Probando si se esta cumpliendo este peo 
sexo = sexo 