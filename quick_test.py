def palavra_oculta(input, palavra, palavra_formada):
    pt = ""
    for i in range(len(palavra)):
        if (palavra[i] == input or palavra[i] == palavra_formada[i]):
            pt += palavra[i]
        else:
            pt += "*"
    return pt


pa = "banana"
pb = "*" * len(pa)
tentativas = 5

print(f"Game iniciado, palavra é: {pb}")

while(tentativas > 0):
    letra_usuario = input("Digite uma letra: ").lower()
    pb = palavra_oculta(letra_usuario, pa, pb)
    if(pa == pb):
        print(f"Game finalizado, palavra completa: {pb.capitalize()}")
        exit()
    print(pb)
    tentativas -= 1
