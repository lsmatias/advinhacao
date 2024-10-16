from random import randint

print('#### Iniciando Jogo ####')
nivel = input('Escolha o nível de dificuldade (fácil, médio, difícil): ').lower()

if nivel == 'fácil':
    max_num, tentativas = 50, 15
elif nivel == 'médio':
    max_num, tentativas = 100, 10
else:
    max_num, tentativas = 200, 5

random_num = randint(0, max_num)

for chances in range(tentativas, 0, -1):
    chute = input(f'Chute um número entre 0 e {max_num}: ')
    if chute.isnumeric() and (chute := int(chute)) == random_num:
        print(f'\nParabéns, você venceu! O número era {random_num} e você ainda tinha {chances - 1} chances.\n')
        break
    elif chute.isnumeric():
        print(f'\nVocê errou!!! Dica: É um número {"menor" if chute > random_num else "maior"}.')
        print(f'Você ainda possui {chances - 1} chances.\n')
    else:
        print('Por favor, insira um número válido.')
else:
    print(f'\nSuas chances acabaram, você perdeu! O número era {random_num}.\n')

print('#### Fim do Jogo ####')
