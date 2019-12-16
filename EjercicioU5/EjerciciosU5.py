import re

path = "textoU5.txt"

try:
	archivo = open(path,'r')
except:
	print("El archivo no se encuentra")
	quit()

texto = ""
 
for linea in archivo:
	texto += linea

#1	Sentencia de asignación. Ejemplo: suma = 0, factorial = 1, vidas = cont, etc.
regexasignacion = r'([a-z0-9]+\s*[=]+\s*[a-z0-9+]+)'
resultasignacion = re.findall(regexasignacion,texto)
print("\n Las sentencias de asignacion son:\n", resultasignacion)



#2	Operaciones aritméticas básicas. Ejemplo: suma = 2.7 + 3, cont = cont + 1, etc.
regexparametrico = r'([A-Za-z0-9-_]+\s*[=]+\s*[A-Za-z0-9-_|0-9.0-9]+\s*[\+,\-,\*,\/,\%]+\s*[A-Za-z0-9-_|0-9.0-9]+)'
resultparametrico = re.findall(regexparametrico,texto)
print("\n Las operaciones aritmeticas son:\n", resultparametrico)



#3	Expresiones booleanas básicas. Ejemplo: edad >= 5, suma != 0, etc.
regexbooleano = r'([A-Za-z0-9]+\s*[|<|>|!|<=|>=]=+\s*[A-Za-z0-9])'
resultbooleano = re.findall(regexbooleano, texto)
print("\nLas operaciones booleanas son:\n", resultbooleano)



#4	Formulas más complejas del tipo c = a op ( b op d)
regexcomplejo = r'([A-Za-z0-9]+\s*=+\s*[A-Za-z0-9]+\s*[|<|>|!|<=|>=|\+|\-\*\/]\s*[(]+\s*[A-Za-z0-9]+\s*[|<|>|!|<=|>=|\+|\-\*\/]+\s*[A-Za-z0-9]+\s*[)])'
resultcomplejo = re.findall(regexcomplejo,texto)
print("\n La formula compleja es:\n", resultcomplejo)



#5	El encabezado de estructura de control. if, while, for, etc.
regexfor = r'(for+\s*[A-Za-z0-9-_]+\s*[in]+\s*[A-Za-z0-9-_]+\s*:)'
regexwhile = r'(while+\s*[A-Za-z0-9-_]+\s*[|<|>|!|<=|>=]=+\s*[A-Za-z0-9-_]+\s*:)'
regexif = r'(if+\s*[A-Za-z0-9-_]+\s*[|<|>|!|<=|>=]=+\s*[A-Za-z0-9-_]+\s*:)'
regextry = r'(try:+\s*[A-Za-z0-9-_]+\s*except+\s*[A-Za-z0-9-_]+\s*:)'

resultfor = re.findall(regexfor, texto)
resultwhile = re.findall(regexwhile,texto)
resultif = re.findall(regexif,texto)
resulttry = re.findall(regextry,texto)

print("\n Operaciones de FOR son:\n", resultfor)
print("\n Operaciones de WHILE son:\n", resultwhile)
print("\n Operaciones de IF son:\n", resultif)
print("\n Operaciones de TRY son:\n", resulttry)
