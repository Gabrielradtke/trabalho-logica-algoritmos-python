def menu_inicial():
    print('Bem-vindo à Copiadora Gabriel Radtke')
    print('-----------Menu de Opções-----------')
    print('      DIGITE A OPÇÃO DESEJADA!      ')
    print('------------------------------------')
    print('DIG - Digitalização                 ')
    print('ICO - Impressão Colorida            ')
    print('IPB - Impressão Preto e Branco      ')
    print('FOT - Fotocópia                     ')
    print('------------------------------------')

def escolha_servico():
    while True:
        servico = input('Digite o serviço solicitado: ').upper()
        precos = {
            'DIG': 1.10,
            'ICO': 1.00,
            'IPB': 0.40,
            'FOT': 0.20
        }
        if servico in precos:
            return servico, precos[servico]
        else:
            print('Serviço inválido, tente novamente!\n')

def num_pagina():
    while True:
        try:
            quant_pag = int(input('Digite o número de páginas: '))
            if quant_pag <= 0:
                print('O número de páginas não pode ser 0 ou negativo! :(\n')
            elif quant_pag > 20000:
                print('Não atendemos esse volume de cópias! :(\n')
            else:
                return quant_pag
        except ValueError:
            print('Por favor, digite um número válido.\n')

def calculo_desc(quant_pag):
    if 20 <= quant_pag < 200:
        return 0.15
    elif 200 <= quant_pag < 2000:
        return 0.20
    elif 2000 <= quant_pag < 20000:
        return 0.25
    return 0.00

def servico_extra():
    print(' Bem-vindo à Copiadora Gabriel Radtke ')
    print('-------------Encadernação-------------')
    print('       DIGITE A OPÇÃO DESEJADA!       ')
    print('--------------------------------------')
    print('1. Encadernação Simples (R$ 15.00)    ')
    print('2. Encadernação Capa Dura (R$ 40.00)  ')
    print('0. Nenhum adicional                   ')

    while True:
        opcao = input('Digite a opção acima: (0, 1, 2): ')
        if opcao == '0':
            return 0
        elif opcao == '1':
            return 15
        elif opcao == '2':
            return 40
        else:
            print('Opção inválida, tente novamente!\n')

def tela_final(servico, quant_pag, desconto, encadernacao, valor_total, valor_servico):
    print('------------------------------')
    print(f'Serviço: {servico}')
    print(f'Páginas: {quant_pag}')
    print(f'Desconto: {desconto * 100:.0f}%')
    print(f'Encadernação: R$ {encadernacao:.2f}')
    print(f'Valor sem encadernação: R$ {valor_servico:.2f}')
    print(f'TOTAL A PAGAR: R$ {valor_total:.2f}')
    print('------------------------------')

# Fluxo do programa
menu_inicial()
servico, preco_pag = escolha_servico()
quant_pag = num_pagina()
desconto = calculo_desc(quant_pag)
encadernacao = servico_extra()

valor_servico = (quant_pag * preco_pag) * (1 - desconto)
valor_total = valor_servico + encadernacao

tela_final(servico, quant_pag, desconto, encadernacao, valor_total, valor_servico)
