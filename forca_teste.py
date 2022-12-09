
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    palavra_secreta_oculta = list("*" * len(palavra_secreta))

    enforcou = False
    acertou = False

    while (not enforcou and not acertou):
        print(f"A palavra é: {palavra_secreta_oculta}")

        chute = input("Qual letra? ").lower()

        index = 0
        for letra in palavra_secreta:
            if (chute == letra):
                palavra_secreta_oculta[index].replace("*", chute)
                print(f"Encontrei a letra {letra} na posição {index}")
            index += 1

    print("Fim do jogo!")


if (__name__ == "__main__"):
    jogar()
