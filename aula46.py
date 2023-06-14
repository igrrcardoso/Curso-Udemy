for i in range(0, 100, 3):
    if i == 2:
        print('i é', i, 'pulando...')
        continue

    if i == 8:
        print('i é', i, 'seu else não será executado.')
        break

    for j in range(1, 4):
        print(i, j)

else:
    print('For completo com sucesso!')
