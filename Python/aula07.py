# FUNÇÕES EM PYTHON
# COLEÇÃO DE CÓDIGO/LÓGICA
""" def bigmac():
    print('Sanduíche Big Mac Picanha')
print('Início')
bigmac()
print('Fim') """

def fazer_big_mac(nome):
    print(f"Sanduíche Big Mac {nome}")
    
fazer_big_mac('Roger')
fazer_big_mac('Cris')
fazer_big_mac('João')

def maior_num(lista_num):
    lista_num.sort()
    lista_num.reverse()
    maior_num = lista_num[0]
    return maior_num

resultado = maior_num([312,912,418,412,617,867,575,1028,-8,-10,382])
print(resultado)
