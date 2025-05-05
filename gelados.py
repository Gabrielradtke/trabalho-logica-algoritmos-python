print('Bem-vindo à Loja de Gelados Gabriel Radtke!')
print('-----------------Cardápio------------------')
print('-------------------------------------------')
print('---| Tamanho | Cupuaçu(CP) | Açaí (AC) |---')
print('---|    P    |  R$  9.00   | R$ 11.00  |---')
print('---|    M    |  R$ 14.00   | R$ 16.00  |---')
print('---|    G    |  R$ 18.00   | R$ 20.00  |---')
print('-------------------------------------------')

total = 0

while True:
    sabor = input('Digite o sabor desejado (CP / AC): ').upper()
    # Apresentar erro ao digitar sabor diferente
    if sabor != 'CP' and sabor != 'AC':
        print('Sabor inválido! Tente novamente.\n')
        continue

    tamanho = input('Digite o tamanho desejado (P / M / G): ').upper()

    if sabor == 'CP':
        if tamanho == 'P':
            preco = 9.00
        elif tamanho == 'M':
            preco = 14.00
        elif tamanho == 'G':
            preco = 18.00
        else:
            print('Tamanho inválido! Tente novamente.\n')
            continue
    elif sabor == 'AC':
        if tamanho == 'P':
            preco = 11.00
        elif tamanho == 'M':
            preco = 16.00
        elif tamanho == 'G':
            preco = 20.00
        else:
            print('Tamanho inválido! Tente novamente.\n')
            continue

    total = total + preco
    print(f'Produto adicionado! Total parcial: R$ {total:.2f}\n')

    continuar = input('Deseja adicionar mais algum item? (S/N): ').upper()
    if continuar == 'N':
        break

print(f'O total do pedido é de R$ {total:.2f}\n')
