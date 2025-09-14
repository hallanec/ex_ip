
def valida_caracteres_permitidos(texto):
    for caractere in texto:
        if caractere.isalnum() or caractere == '_':
            pass
        else:
            return False
    return True

N = str(input("Digite o seu nome"))
S = str(input("Digite o seu nome"))


if len(N and S ) > 3 and len(N and S) < 16:
    if valida_caracteres_permitidos(N and S):
        print("Nickname válido:", (N+S))
    else:
        print("Nickname inválido! Use só letras, números e underlines.")
else:
    print("Nickname inválido: deve ter mais que 3 e menos que 16 caracteres")

