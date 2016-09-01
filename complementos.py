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
	if(base10 <= 255): #Condicionales necesarios para representar el numero con 8 o 16 bits
		n = 8
	elif(base10 > 255 and base10 <= 65535): #Solo representa el complemento maximo de 16 bits
		n = 16

	complementoD = 2 ** n - base10 - 1 #Formula para convertir a complemento A1 un decimal
	print("Complemento de ", base10, "es", complementoD, "base 10")
	binario = haciaBinario(complementoD)

	if(len(binario) != n):#Si el binario es diferente a 8 o 16 bits se agregan 0's a la derecha
		binario = agregaCeros(binario, n)

	return binario

def compuertaNot(numeroB):#Aun no tiene utilidad, pero la tendrá
	"""Niega de los bits"""
	if(numeroB == 1):
		return 0
	elif(numeroB == 0):
		return 1

def agregaCeros(binario, bits):
	"""Agrega 0's al arreglo para garantizar 8 o 16 bits"""
	for i in range(bits-len(binario)):
		binario.insert(i, 0)

	return binario

def convierteATexto(lista):
	"""Convierte una lista a una cadena de texto"""
	cadena = "".join(str(i) for i in lista)

	return cadena

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
			binario = complementoA1(base10)
			print("El numero", base10, "en complemento A1 es:", convierteATexto(binario))
		elif opcion == 2:
			base10 = int(input("Ingresa el numero entero a convertir: "))
			binario = complementoA1(base10)
			
			pass
		elif opcion == 3:
			pass
		elif opcion == 4:	
			pass
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