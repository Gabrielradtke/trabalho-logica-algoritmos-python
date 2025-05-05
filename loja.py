print('Bem-vindo à loja GABRIEL RADTKE') 

valor = float(input('Digite o valor do produto: ')) 
quantidade = int(input('Digite a quantidade de produto(s): ')) 

preco_total = valor * quantidade 
preco_total_desc = 0 

    # calculo com a margem baseados em cada faixa de valor 
if preco_total > 0 and preco_total < 2500: 
    print(f'O preço total SEM desconto é de R$ {preco_total:.2f}') 
    print(f'O preço total COM desconto é de R$ {preco_total_desc:.2f}') 
elif preco_total >= 2500 and preco_total < 6000: 
    # 4% de desconto 
    preco_total_desc = preco_total * 0.96 
    print(f'O preço total SEM desconto é de R$ {preco_total:.2f}') 
    print(f'O preço total COM desconto é de R$ {preco_total_desc:.2f}') 

elif preco_total > 6000 and preco_total < 10000: 
    # 7% de desconto 
    preco_total_desc = preco_total * 0.93 
    print(f'O preço total SEM desconto é de R$ {preco_total:.2f}') 
    print(f'O preço total COM desconto é de R$ {preco_total_desc:.2f}') 
elif preco_total > 10000: 
    # 11% de desconto 
    preco_total_desc = preco_total * 0.89 
    print(f'O preço total SEM desconto é de R$ {preco_total:.2f}') 
    print(f'O preço total COM desconto é de R$ {preco_total_desc:.2f}') 
else: 
    # Informando que foi inserido um valor inválido 
    print('Valor inválido') 
