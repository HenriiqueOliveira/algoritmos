# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo
"""
valor1= input("Digite um valor:")
valor1= int(valor1)

if valor1 > 0:
    print("O Valor é Positivo!")

elif valor1 < 0:
    print("O Valor é Negativo!")

else:
    print("O Valor é 0!")

"""


# Faça um Programa que peça dois números e imprima o maior deles.
"""
num1= input("digite um numero:")
num1= int(num1)

num2= input ("digite outro numero:")
num2= int(num2)

if num1 > num2:
    print("primeiro número é maior!")

elif num1 < num2:
    print("Segundo número é maior!")

else:
    print("Os Números são iguais!")

"""


#Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que C.
"""
n1= input("Valor A:")
n1= int(n1)

n2= input("Valor B:")
n2= int(n2)

n3= input("Valor C:")
n3= int(n3)

if n1+n2 < n3:
    print("C é menor!")
else:
    print("é falso")

"""

#Faça um Programa que verifique o sexo de uma pessoa. O usuário deve informar ‘F’ ou ‘M’
#e o programa deve escrever “Feminino” ou “Masculino”, conforme a letra digitada.
"""
sexo = input("Digite m para Masculino e f para feminino: ")

if sexo == "m":
    print("M - Masculino")

else:
    print("F - Feminino")
"""

#Faça um Programa que peça um número inteiro e determine se ele é par ou ímpar.
#Dica: utilize o operador módulo (resto da divisão).
"""
num= input("Digite um Número Inteiro:")
num= int(num)

if num % 2 ==0:
    print("O número é par!")

else:
    print("O número é impar!")
"""

#Faça um algoritmo que peça um número e se ele for par some 5, se não, some 8.

a= input("Digite um número:")
a= int(a)

if a % 2 == 0:
    a= a+5
    print(a)

else:
    a= a+8
    print(a)
