print("hola")

# Procesamiento de texto
txt = "texto abc d f gd gd"
ps = set(txt.split(" "))
i = range(0, len(ps))
it = dict(zip(ps, i))
print(it.get('abc'))
