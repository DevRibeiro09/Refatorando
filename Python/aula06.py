# LISTAS E TUPLES
familia = ['Samuel','Aldeci','Simone','Tays','Gustavo','Aylla']
# AS LITAS COMEÇAM DO [0 AO --]
#             0         1        2       3       4        5       6
print(familia[0]) #SOMENTE O PRIMEIRO NOME
print(familia[2]) # SIMONE
print(familia[2:5]) # SIMONE, TAYS E GUSTAVO 

# familia[4] = "José" # NO PRINT VAI APARECER 'JOSÉ' 
# print(familia[4])

familia.extend(['Sara','Washington']) # ADICIONA MAIS PESSOAS À LISTA
print(familia) # TODOS APARECEM

familia.append('Bela') #ADICIONAR O MASCOTE
# NO 'APPEND' SÓ É ACEITO 01 ARGUMENTO
                       
familia.insert(2,'Max') # ELE VIRA O ÍNDICE QUE ESCOLHEU (A POSIÇÃO RELATIVA AO '2')
print(familia)

familia.pop() # REMOVE SEMPRE O ÚLTIMO ÍNDICE
familia.remove('Tays') # REMOVE O NOME DA LISTA - CASO NÃO TENHA, DÁ ERRO
print(familia.count('Max')) # PRINTA QUANTOS 'NOMES/VALORES' TEM IGUAIS A ESSE NA LISTA
print(familia.index('Aylla')) # PRINTA A POSIÇÃO QUE ESTÁ O NOME
#familia.clear() --- REMOVE TUDO DA LISTA


idade_familia = [18,50,48,27,23,0,23,52]
idade_familia.sort() #ORDENA A FAMÍLIA DE ACORDO COM A NUMERAÇÃO/ORDEM ALFABÉTICA
print(idade_familia) 
familia.sort() #ORDENA DE TRÁS PRA FRENTE TAMBÉM
familia.reverse() #ORDENA A FAMILIA DE TRÁS PRA FRENTE
print(familia) #PRINTADA AO CONTRÁRIO E EM ORDEM ALFABÉTICA
familia.copy() #COPIA A LISTA

TimeoutError()
print('ERROR')


