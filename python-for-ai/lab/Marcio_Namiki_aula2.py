#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'FIAP'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # Exercícios
#%% [markdown]
# ## 1) Escreva uma função que verifique se há uma letra no começo de uma frase. Se houver, retorne True, caso contrário, retorne False. 

#%%
# resposta 1
def comeca_com_letra(frase):
    import re
    return re.search (r'^([a-z]|[A-Z])', frase) != None

# Uso
print(comeca_com_letra('Aprendendo Python para AI'))

#%% [markdown]
# ## 2) Reescreva a seguinte função usando:
#     -> map e lambda
#     -> list comprehension

#%%
# resposta 2-a
# map e lambda
squares = map(lambda num: num**2, range(10))
print(list(squares))


#%%
# resposta 2-b
# list comprehension
s = [x**2 for x in range(10)]
print(s)

#%% [markdown]
# ## 3) Escreva em Python uma função que, dadas duas listas não vazias e de mesmo comprimento, retorne como resultado uma nova lista contendo em cada posição a soma dos elementos correspondentes nas duas listas recebidas.
#     -> l1 = [1,2,3,4,5]
#     -> l2 = [1,2,3,4,5]
#     -> resultado = [2,4,6,8,10]

#%%
# resposta 3
def soma_lista(l1,l2):
    return map(lambda a: sum(a), list(zip(l1,l2)))

#Uso
lista1 = [1,2,3,4,5]
lista2 = [1,2,3,4,5]
print(list(soma_lista(lista1,lista2)))

#%% [markdown]
# ## 4) A amplitude de um vetor 3D é dado pela seguinte fórmula: $\sqrt{x^2 + y^2 + z^2}$
# ## Escreva uma função, usando lambda, que calcule a amplitude dos seguintes vetores:
#     -> (1,1,1) 
#     -> (3,4,5)

#%%
# resposta 4
def amplitude(vetor):
    import math
    return math.sqrt(sum([x**2 for x in vetor]))

#Uso
l = [(1,1,1),(3,4,5)]
for v in l:
    print('A amplitude do vetor %s é %.2f' % (str(v), amplitude(v)))

#%% [markdown]
# ## 5) Use reduce para criar uma função que calcule o fatorial de qualquer número n

#%%
# resposta 5
def fatorial(n):
    from functools import reduce
    return reduce(lambda x, y: x*y, range(2,n+1,1))

#Uso
n = int(input('Calcule o fatorial de : '))
print(fatorial(n))

#%% [markdown]
# ## 6) Reescreva a função abaixo usando list comprehension:

#%%
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
    if word != "the":
        word_lengths.append(len(word))
print(words)
print(word_lengths)


#%%
# resposta 6
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lenghts = []

#solução
[word_lenghts.append(len(word)) for word in words if word != 'the']

print(words)
print(word_lenghts)

#%% [markdown]
# ## 7) Calcule o número de meses desde a data que o brasil foi descoberto. Considere um mês com 30 dias. Dia do descobrimento do Brasil 22/04/1500.

#%%
# resposta 7
import datetime
from datetime import timedelta

desc_brasil = datetime.datetime(1500, 4, 22) #criando uma data com horário
dd = desc_brasil.today() - desc_brasil #cálculo de tempo
print ('Passaram-se %.1f (meses)\n    desde o descobrimento do Brasil em %s \n    até hoje [%s]' % (dd.days/30 , str(desc_brasil.date()), str(desc_brasil.today().date())))

#%% [markdown]
# ## 8) Implementar um programa que receba um nome de arquivo e gere estatísticas sobre o arquivo (número de caracteres, número de linhas e número de palavras)
#     -> verifique a existência do arquivo
#     -> crie um arquivo de texto fictício contendo 10 linhas

#%%
# resposta 8
import traceback
import os.path as osp

# Tente receber o nome do arquivo 'Seculo XXI o Sec da Africa.txt'
try:
    filename = input('Nome do arquivo: ').strip()
    if osp.exists(filename):
        # Numerando as linhas
        infile=open(filename, "r")
        content=infile.read()
        
        saida = [(len(c), len(c.split('\n')), len(c.split(' '))) for c in [content]]
        #print(saida)
        print('Resultado:\n  %d caracteres' % saida[0][0])
        print('  %d linhas' % saida[0][1])
        print('  %d palavras' % saida[0][2])
    else:
        # Arquivo não existe
        print('[!] ERRO CONHECIDO: O arquivo \'%s\' não foi encontrado no diretório\n>>  \'%s\'\n        \nPor favor, verifique e tente novamente.' % (filename, str(os.getcwd())))
except:
    # Mostre na tela
    trace = traceback.format_exc()
    print ('[!] ERRO INESPERADO:\n', trace)
    # Encerre o programa
    raise SystemExit




#%%
