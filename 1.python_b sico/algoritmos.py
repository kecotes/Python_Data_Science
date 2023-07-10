

def Suma(parametro1, parametro2):
    resultado = parametro1 + parametro2
    return resultado

argumento1 = 10
argumento2 = 20
print(Suma(argumento1, argumento2))



# Sentencia simple
print ("Hola Mundo, estoy programando en Python!")

# Imprimir varias lineas
print ("""
-¿Tú conoces a Pin Pon?
-¿A Pin Pon?
-Si, Pin Pon.
-Sí... es un muñeco muy guapo y de cartón.
-Sí, se lava su carita con agua y con jabón.
-¡¿Con agua y con jabón?
- ¡Sí, se lava la caritaǃ
—Se lava la carita con agua y con jabón...
""")

# Anidando comillas dentro de otras      
print ('Hola "carambolas"')
num1 = 200000000003124513512465346346365374587465848
print(type(num1))


""" matriz = [[1,2], [3,4], [5,6]]

for f in range(3):
    for c in range(2):
        print(matriz[f][c], end= ' ')
    print() """


a=[]
m=3
n=2
for f in range(m): # Vamos a recorrer for hasta m
    a.append([]) # En cada fila voy a agregar una lista
    for c in range(n):
        a[f].apprend(None)

for f in range(m):
    for c in range(n):
        print(a[f][c], end=' ')


