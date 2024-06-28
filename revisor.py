import random, time

print('='*30)
print(' '*10, 'Revisor')
print('='*30)
try:
    contagem_de_questoes = open('contagemdequestoes.txt', 'r')
    linha_contagem_de_questoes = contagem_de_questoes.readlines()
    quantidade_de_questoes = int(linha_contagem_de_questoes[0]) #transformando de str pra int
except:
    quantidade_de_questoes = 0


while True:
    opcao = str(input('deseja criar ou ler:[C/L]'))
    if(opcao == 'c'):
        criar_questão = str(input("escreva algo"))

        # ============ arquivo txt banco de questoes ===============
        arquivo = open('./bancodequestoes.txt', 'a') #escreve mais coisa no bloco de notas sem apagar
        arquivo.write('\n')
        arquivo.write(criar_questão)
        arquivo.close()

        # ============= arquivo txt apenas para a contagem da quantidade de questoes ==============
        quantidade_de_questoes += 1
        arquivo_de_contagem = open('./contagemdequestoes.txt', 'w')  # cria outro arquivo txt apenas para a contagem de questões
        arquivo_de_contagem.write(str(quantidade_de_questoes))
        arquivo_de_contagem.close()


    elif(opcao == 'l'):
        questao_da_linha = random.randint(0, quantidade_de_questoes)
        qual = int(input('qual linha quer ler?'))

        lendo_questao = open('./bancodequestoes.txt', 'r')
        linha = lendo_questao.readlines()
        print(linha[qual])
    else:
        break


