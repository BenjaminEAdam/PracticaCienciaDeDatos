print("hola")

# Procesamiento de texto
txt = "texto abc d f gd gd"
ps = set(txt.split(" "))
i = range(0, len(ps))
it = dict(zip(ps, i))
print(it.get('abc'))

## Compresion de listas

y = [t**2 for t in i if t > 2] #devuelve la lista con los elementos al cuadrado para los t > 2
print(y)

## Bigrama con comprension de listas

z = [x for x in zip(ps, ps[1:])]
print(z)

## Abrir archivo, w ubica el puntero al principio asi q sobreescribe el archivo.

a = open('prueba.txt', 'w', encoding='utf-8')

