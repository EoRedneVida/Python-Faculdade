import random
escolhidos = [0, 0, 0, 0, 0, 0]
indice = 0
while indice < 6:
    escolhidos[indice] = int(input('Tente a sorte! Escolha um número de 1 a 60: '))
    indice += 1

resultado = [0, 0, 0, 0, 0, 0]
i = 0
while i < 6:
    resultado[i] = random.randint(1, 60)
    i += 1

acertos = 0
i = 0
while i < 6:
    j = 0
    while j < 6:
        if escolhidos[i] == resultado[j]:
            acertos += 1
            break
        j += 1    
    i += 1

print(f'Os números escolhidos por você foram {escolhidos} e os números sorteados foram {resultado}, você acertou {acertos}!!')