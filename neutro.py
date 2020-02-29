a = 2
b = 10
c = 5
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
#neutro(expresion)

# Funcion que me permite ver si expresion ingresada es real

#def reales(e):
	#Obteniendo valor numérico de la expresión ingresada
	#numerico = eval(e)

	#Comprobando si es real
	#if (isinstance(numerico, complex)):
	#	print("Cumple la Ley de Composición Interna. Es un número real")
	#	return 1
	#else:
	#	print("No cumple con la Ley de Composición Interna. No es un número real.")
	#	return 0

expresion2 = input("Ingrese la segunda expresión a evaluar: ")
def distributiva(e1, e2):
	#a*(b+c) 
        elm = e1.replace("b","c")
        elm = elm.replace("a","b")
        dist1 = e2.replace("b","("+elm+")")
        r1 = eval(dist1)
        #a*b + a*c
        dist2 = "(a*b)+(a*c)"
        elm1 = e2.replace("b","c")
        dist2 = dist2.replace("a*b",e2)
        dist2 = dist2.replace("a*c",elm1)
        r2 = eval(dist2)
        print(dist1,"debe ser igual a", dist2)
        if r1 == r2:
            print("es anillo")
        else:
            print("no es anillo")

distributiva(expresion, expresion2)