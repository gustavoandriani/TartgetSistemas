from time import sleep

print('-'*30)
print('EXERCÍCIO 01')
print('-'*30)
indice = int(13)
soma = int(0)
k = int (0)

while k < indice:
    k = k + 1
    soma = soma + k

print(f'O valor da variável SOMA é: {soma}\n\n')

print('-'*30)
print('EXERCÍCIO 02')
print('-'*30)

opcao = ''
while opcao != 'SIM':
    n = int(input('Qual número você deseja saber se está na sequência de Fibonacci?\nR:'))
    t1 = 0
    t2 = 1
    while t1 != n > t1:
        t3 = t1 + t2
        t1 = t2
        t2 = t3
    if t1 == n:
        print(f'O número {n} está presente na sequência de Fibonacci\n\n')
    else:
        print(f'O número {n} não está presente na sequência de Fibonacci\n\n')
    opcao = input('Viu a resposta que queria? SIM/NÃO\nR:').upper()

sleep(1)
print('-'*30)
print('EXERCÍCIO 03')
print('-'*30)

print('a) 1, 3, 5, 7, ___\nNessa sequência cada número é igual ao anterior +2')
t1 = 1
t2 = 2
while t1 <= 9:
    print(f'{t1} ', end='')
    t3 = t1 + t2
    t1 = t3

sleep(3)
print('\n\nb) 2, 4, 8, 16, 32, 64, ____\nNessa sequência cada número é igual ao anterior x2')
t1 = 2
t2 = 2
while t1 <= 128:
    print(f'{t1} ', end='')
    t3 = t1 * t2
    t1 = t3

sleep(3)
print('\n\nc) 0, 1, 4, 9, 16, 25, 36\nNessa sequência cada número é igual ao anterior acrescido de um número ímpar que segue a sequência 1, 3, 5, 7, 9. Realizando a subtração dos dois últimos números, temos que 36 - 25 = 11. Assim, devemos acrescentar 11 + 2 = 13 ao último número, obtendo 36 + 13 = 49.')
t1 = 0
t2 = 1
while t1 <= 49:
    t3 = ((t2 - t1) + 2) + t2
    print(f'{t1} ', end='')
    t1 = t2
    t2 = t3

sleep(3)
print('\n\nd) 4, 16, 36, 64, ____\nCada número é igual ao quadrado dos números pares. Com isso, temos que 64 = 8². Então, o próximo número par é 10, e o seu quadrado é 10² = 100.')
t1 = 2
while t1 <= 10:
    t2 = t1 * t1
    print(f'{t2} ', end='')
    t1 += 2

sleep(3)
print('\n\ne) 1, 1, 2, 3, 5, 8\nCada número é igual à soma do número atual com o número anterior. Assim, o próximo número é igual a 8 + 5 = 13.')
t1 = 0
t2 = 1
while t1 != 13:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(f'{t1} ', end='')

sleep(3)
print('\n\nf) 2, 10, 12, 16, 17, 18, 19\nSequência formada através de todos os números que iniciam com a letra d. Assim, o próximo número em ordem crescente que inicia com a letra d é 200.')
print('2 10 12 16 17 18 19 200')

sleep(3)
print('-'*30)
print('EXERCÍCIO 04')
print('-'*30)

print('Levando em consideração que o carro levaria 54 minutos e 32 segundos para chegar em Franca,\ne o caminhão levaria 1 hora e 15 minutos para fazer o mesmo percurso.')
print('1 hora e 25 minutos se creditarmos os pedágios.\nPela lógica, os dois estarão na mesma distância de Ribeirão, porém estarão mais próximos a Franca do que de Ribeirão.')
print('Cheguei ao resultado do tempo de percurso de ambos utilizando uma ferramenta online de cálculo de distância x velocidade(calkoo.com). A minha conclusão da pergunta remete a minha lógica de raciocínio,\nse os veículos estão se cruzando, logo, ambos estão a mesma distância de qualquer lugar.')

sleep(5)
print('-'*30)
print('EXERCÍCIO 05')
print('-'*30)

string = str(input('Insira algo: '))[::-1]
print(string)
