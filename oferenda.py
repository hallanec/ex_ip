D = int(input())

ARTHUR = int(input())
LUIZ = int(input())
PEDRO = int(input())

valores = [("Arthur", ARTHUR), ("Luiz", LUIZ), ("Pedro", PEDRO)]

# Valores maiores ou iguais a D
validos = [v for v in valores if v[1] >= D]

if validos:
    dono, valor = min(validos, key=lambda x: x[1])
else:
    # Se não tiver nenhum >= D, pega o maior valor menor que D
    validos = [v for v in valores if v[1] < D]
    dono, valor = max(validos, key=lambda x: x[1])

print(dono)
