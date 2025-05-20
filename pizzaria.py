#você esta processo seletivo para ser dev jr. E recebeu o teste para desenvolver. Sera um programa para pizzaria, no qual recebera: nome do cliente, endereço, opções (mussarela, calabreza, portuguesa, marguerita ), devera imprimir o nome do cliente, endereço e sabor escolhido 

#passo 1.nome do cliente 
nome_do_cliente = input("seja bem vindo! qual o  seu nome por favor ?")

#passo 2. endereço 
endereço = input('endereço de entrega :')

#passo 3. receber o pedido 
pedido = input ('digite qual o sabor para sua pizza : \n'
'(mussarela | calabreza | portuguesa | marguerita) :')

#passo 4.opçoes (elif traduçao para pt-br senao entao)
if pedido == "mussarela":
    print(f'sr(a){nome_do_cliente}, o seu pedido sera entregue no {endereço},sabor escolhido é :{pedido}')
elif pedido == "portuguesa":
    print(f'muito obrigado pelo seu pedido, {nome_do_cliente}. Nosso já está a caminho do {endereço}, com a sua pizza de {pedido}')
elif pedido =="calabreza":
    print(f'excelente escolha {nome_do_cliente}, a nossa pizza{pedido} chegara em breve na {endereço}')
else:
    print(f'oba! a pizza {pedido}, chegara quentinho na sua casa {endereço}, agradecemos pelo pedido ')