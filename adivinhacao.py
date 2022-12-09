import random


def receber_numero_secreto(rodada, total_de_tentativas):
    print(f"Tentativa: {rodada} de {total_de_tentativas}")
    chute = int(input("Digite o seu número entre 1 e 100: "))
    print("Você digitou ", chute)
    return chute


def jogar():
    print("********************************")
    print("Bem vindo ao jogo de advinhação!")
    print("********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina um nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    elif (nivel == 3):
        total_de_tentativas = 5
    else:
        print("Valor inválido!")

    for rodada in range(1, total_de_tentativas + 1):
        chute = receber_numero_secreto(rodada, total_de_tentativas)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        chute_maior = chute > numero_secreto
        chute_menor = chute < numero_secreto
        if (acertou):
            print(f"Você acertou e fez {pontos} pontos!")
            break
        else:
            if (chute_maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif (chute_menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()
