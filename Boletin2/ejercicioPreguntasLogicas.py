"""
# coding: utf-8
 @autor: Sandra Ruiz Jimenez
 @fecha: Oct 26, 2021
 @nombre: PREGUNTAS DEL TEMA 1
"""
 
 
""" 
1. Resolver las siguientes cuestiones:
1. Calcular el resultado de las siguientes expresiones lógicas:
a) 7>=27 AND NOT (7<=2) --> F and NOT F --> F and V --> F
b) 24>5 AND 10<=10 OR 10=5 --> V and V or F --> V or F --> V
c) (10>=15 OR 23=13) AND NOT(8=8) --> (F or F) AND NOT V --> F and F --> F
d) NOT (6/3>3) OR 7>7 --> NOT F or F --> V or F --> V


2. Calcular el valor de las siguientes expresiones aritméticas:
a) 27 mod 4 + 15\4 --> 
b) 37\4^2–2 --> 
c) 9*2/3*10*3 --> 18/60 --> 
d) (7*3–4*4)^2\4*2 -->


3. Escribir una expresión lógica que cumpla:
a) Debe ser Verdadera si el contenido de la variable entera precio es igual o superior a 60
euros pero igual o inferior a 420 euros.
precio>=60 or precio<=420

b) Debe ser Verdadera si el numero contenido en la variable entera numero es impar.
num%2!=0
num%2==1

c) Debe ser Verdadera si las dos variables enteras saldo de una cuenta, y dineroSacar son
válidas.
saldo>0 and saldo>=dineroSacar
#De esta forma ya se indica que dineroSacar debe ser mayor que 0.

d) Debe ser Verdadera si las variables enteras hora y minutos son correctas, es decir, que
estén comprendidas entre 0:0 y 23:59.
hora>=0 and hora<24 and minutos>=0 and minutos<60

e) Debe ser Verdadera si la variable estadoCivil que almacena el estado civil de una
persona no es correcta (S-Soltero, C-Casado, V-Viudo, D-Divorciado).
NOTA: Además siempre debe ser Falsa en el caso contrario al que se formula.
estadoCivil not in {"S", "C", "V", "D"}
not (estadoCivil=="S" or estadoCivil=="C" or estadoCivil=="V" or estadoCivil=="D")
estadoCivil!="S" and estadoCivil!="C" and estadoCivil!="V" and estadoCivil=="D"


4. Escribir una expresión lógica que cumpla:
a) Debe ser Falsa cuando la variable cantidad que contiene la cantidad a sacar de un cajero
es superior a 300 euros o negativa.
not (cantidad>300 or cantidad<=0)
cantidad<=300 and cantidad>0

b) Debe ser Falsa si la persona es un adolescente, es decir, la variable edad está entre 16-22
años.
not (edad>=16 and edad<=22)
edad<16 or edad>22

c) Debe ser Falsa si la variable respuesta a una pregunta de tipo (S/N) es válida.
not (respuesta=="S" or respuesta=="N")
respuesta!=S and respuesta!="N"

d) Debe ser Falsa si el número contenido en la variable entera numero es múltiplo de 7 o de 3.
NOTA: Además siempre debe ser Verdadera en el caso contrario al que se formula.
not (numero%7==0 or numero%3==0)
numero%7!=0 and numero%3!=0


5. Escribir la tabla de verdad para las siguientes expresiones lógicas:
a) (A OR B) AND NOT(A):
- si A es True and B es True --> V or V and not(V) --> V and F --> F
- si A es True and B es False --> V or F and not(V) --> V and F --> F
- si A es False and B es True --> F or V and not(F) --> V and V --> V
- si A es False and B es False --> F or F and not(V) --> F and F --> F

b) NOT (A OR B) AND B:
- si A es True and B es True --> NOT (V or V) and V --> NOT V and V --> F and V --> F
- si A es True and B es False --> NOT (V or F) and F --> NOT V and F --> F and F --> F
- si A es False and B es True --> NOT (F or V) and V --> NOT V and V --> F and V --> F
- si A es False and B es False --> NOT (F or F) and F --> NOT F and F --> V and F --> F

c) A OR NOT (B):
- si A es True and B es True --> V or not V --> V or F --> V
- si A es True and B es False --> V or not F --> V or V --> V
- si A es False and B es True --> F or not V --> F or F --> F
- si A es False and B es False --> F or not F --> F or V --> V

d) NOT ((A AND B) AND (B OR A)):
- si A es True and B es True --> NOT ((V AND V) AND (V OR V)) --> NOT (V AND V) --> NOT V --> F
- si A es True and B es False --> NOT ((V AND F) AND (F OR V)) --> NOT (F AND V) --> NOT F --> V
- si A es False and B es True --> NOT ((F AND V) AND (V OR F)) --> NOT (F AND V) --> NOT F --> V
- si A es False and B es False --> NOT ((F AND F) AND (F OR F)) --> NOT (F AND F) --> NOT F --> V
 """