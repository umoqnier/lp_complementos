#Universidad Nacional Autonoma de México/ Facultad de Ingeniería
#Lenguajes de programación
#Alumnos:
#-Banda Martínez César Eduardo
#-Barriga Martínez Diego Alberto
#-Quezada Tapia Abraham
#Programa: Conversor de Decimal a C1, C2 y viceversa
#Hecho en Python 3.5

import os

centinela = 1

def haciaBinario(numero):
	"""Funcion que convierte de decimal a binario"""
	binario = []
	while numero != 0:
		binario.append(numero % 2)
		numero = int(numero/2)

	binario.reverse() #Por la naturaleza de la funcion append() se aplica reverse()
	return binario

def complementoA1(base10):
	"""Funcion que aplica el complemento A1 a un numero Base10"""
	binario = [] #Lista que almacena el numero binario
	n = checaBits(base10)
	complementoD = 2 ** n - base10 - 1 #Formula para convertir a complemento A1 un decimal
	binario = haciaBinario(complementoD) #Convierte a binario el decimal en complemento A1
	if(len(binario) != n):#Si el binario es diferente a 8 o 16 bits se agregan 0's a la derecha
		binario = agregaCeros(binario, n)

	return binario

def complementoA2(base10):
	binario = []
	n = checaBits(base10)
	complementoD = 2 ** n - base10 #Formula para obtener complemento A2 de numero decimal
	binario = haciaBinario(complementoD) #Convierte a binario el decimal en complemento A2
	if(len(binario) != n):#Si el binario es diferente a 8 o 16 bits se agregan 0's a la derecha
		binario = agregaCeros(binario, n)

	return binario

def haciaBase10(binario):
	"""Convierte un numero binario a base 10"""
	decimal = 0
	listaBinaria = list(binario)
	listaBinaria.reverse() #Para aprovechar los indices de la lista
	for i in range(len(listaBinaria)):
		if(listaBinaria[i] != "0"):
			decimal += 2 ** int(i)

	return decimal

def a1HaciaDecimal(numero, bits):
	return  2 ** bits-numero-1

def a2HaciaDecimal(numero, bits):
	return  2 ** bits-numero

def compuertaNot(numeroB):#Aun no tiene utilidad, pero la tendrá
	"""Niega de los bits"""
	if(numeroB == 1):
		return 0
	elif(numeroB == 0):
		return 1

def checaBits(base10):
	if(base10 <= 255): #Condicionales necesarios para representar el numero con 8 o 16 bits
		return 8
	elif(base10 > 255 and base10 <= 65535): #Solo representa el complemento maximo de 16 bits
		return 16
	else:
		return 0

def agregaCeros(binario, bits):
	"""Agrega 0's al arreglo para garantizar 8 o 16 bits"""
	for i in range(bits-len(binario)):
		binario.insert(i, 0)

	return binario

def convierteATexto(lista):
	"""Convierte una lista a una cadena de texto"""
	cadena = "".join(str(i) for i in lista)

	return cadena

def imprimeResBinario(base10, binario, op):
	print("\n===========================================================================")
	print("\t\tEl numero", base10, "en complemento", op,"es:", convierteATexto(binario))
	print("===========================================================================\n")

def imprimeResDecimal(base10, binario, op):
	print("\n===========================================================================")
	print("\t\tEl binario ", convierteATexto(binario)+"["+op+"] es en decimal:", base10)
	print("===========================================================================\n")

def main():
	"""Funcion principal, inicia flujo del programa"""
	while centinela != 0:
		print("\t\t*********CONVERSOR DECIMAL-->C1,C2 Y C1,C2->DECIMAL*********")
		print("""
				1-Decimal --> C1
				2-Decimal --> C2
				3-C1 --> Decimal
				4-C2 --> Decimal
				0-Salir
			""")
		opcion = int(input("Selecciona una opcion: "))

		if opcion == 1:
			base10 = int(input("Ingresa el numero entero a convertir: "))
			if( base10 <= 65535):
				binario = complementoA1(base10)
				imprimeResBinario(base10, binario, "A1")
			else:
				print("**ERROR: no se puede operar con numeros mayores a 65535. Intenta un numero menor.")
		elif opcion == 2:
			base10 = int(input("Ingresa el numero entero a convertir: "))
			if( base10 <= 65535):
				binario = complementoA2(base10)	
				imprimeResBinario(base10, binario, "A2")
			else:
				print("**ERROR: no se puede operar con numeros mayores a 65535. Intenta un numero menor.")
		elif opcion == 3:
			binario = input("Ingresa el binario a convertir: ")
			if(len(binario) <= 8):
				binario = agregaCeros(binario, 8)
				complDeci = haciaBase10(binario)
				base10 = a1HaciaDecimal(complDeci, len(binario))
				imprimeResDecimal(base10, binario, "A1")
			elif(len(binario) > 16):
				binario = agregaCeros(binario, 16)
				complDeci = haciaBase10(binario)
				base10 = a1HaciaDecimal(complDeci, len(binario))
				imprimeResDecimal(base10, binario, "A1")
			else:
				print("**ERROR: Solo se aceptan binarios de 1 a 16 bits")
		elif opcion == 4:	
			binario = input("Ingresa el binario a convertir: ")
			if(len(binario) <= 8):
				binario = agregaCeros(binario, 8)
				complDeci = haciaBase10(binario)
				base10 = a2HaciaDecimal(complDeci, len(binario))
				imprimeResDecimal(base10, binario, "A2")
			elif(len(binario) > 16):
				binario = agregaCeros(binario, 16)
				complDeci = haciaBase10(binario)
				base10 = a2HaciaDecimal(complDeci, len(binario))
				imprimeResDecimal(base10, binario, "A2")
			else:
				print("**ERROR: Solo se aceptan binarios de 1 a 16 bits")
		elif opcion == 0:
			os.system("CLS")
			print("""\t____________________________
	< Developed by Ptolomeo Team >
	#-Banda Martínez César Eduardo
	#-Barriga Martínez Diego Alberto
	#-Quezada Tapia Abraham
	 ----------------------------
	        \   ^__^
	         \  (oo)\_______
	            (__)\       )\/
	                ||----w |
	                ||     ||""")
			break
		else:
			print("*Error* Intenta otra opcion *Error*")

os.system("CLS")
main()