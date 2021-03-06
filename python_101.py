# -*- coding: utf-8 -*-
"""python 101.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PnhEiPtTd_s_Chx9MxwYKJ1DgIE94JbX

# Tipos de dados

## Números

alguns tipos de números
"""

num_1 = 1
num_2 = 1.0
num_3 = 2

"""quais os tipos de números?"""

# use o comando aqui para descobrir qual o tipo desses números 
# digite type(num)

"""para converter os números em outras classes, use os comandos 

        int(num)  # converte o número na sua parte inteira
        float(num) # converte o número em float

algumas funções úteis para operar números

        abs(num) #valor absoluto do número
        ceil(num) #próximo número inteiro
        floor(num) #número inteiro 
   
"""

num3 = 3.14159
print(num3, '\n', type(num3))
print('uso da função int(num3):', int(num3), '\n tipo de número da função ', type( int( num3 ) ) )

"""agora faça o mesmo com a função float na célula abaixo """

#escreva aqui

"""agora teste as funções que operam os números e descreva o resultado delas. 

não esqueça de verificar a classe resultante de cada função

*   abs(x)
*   ceil(x)
*   floor(x)

## strings

strings são textos colocados entre aspas simples
"""

string1 = 'isto aqui é uma string'
string2 = 'isto aqui tbm é uma string'
print(string2)
print(string1)

"""uma string permite a seleção do seu componente, conforme o exemplo abaixo

observe que a contagem sempre começa a partir do zero

- elemento 1 = 0
- elemento 2 = 1
- elemento n = n-1
"""

#seleção do primeiro elemento da string1
elem1 = string1[0]
print(elem1)

#seleção do último elemento de uma string
elem2 = string1[-1]
print(elem2)

#para selecionar uma slice(fatia) da string
meu_nome = 'felipe'
elem3 = meu_nome[0:3]
print(elem3)

#não é possível adicionar um elemento novo dentro da string
#rode a célula e leia "typeError"
meu_nome[2] = 'r'
print(meu_nome)

"""as strings possuem uma propriedade chamadas built-in methods, que são funções que já vieram atreladas a classe string e que nos facilitam trabalhar com elas

para acessar essas funções, digite '.' após o nome da string, conforme abaixo
"""

print(meu_nome)
print( meu_nome.capitalize() )

print(meu_nome.isalnum())
meu_aniversario = '30-dezembro-1997'
print(meu_aniversario.isalnum())

"""operações com strings usando símbolos matematicos

veja o que ocorre se vc utilizar 

        + 
        * 
com as duas strings

combine as duas strings com esses operadores!
"""

#digite aqui

"""agora veja um exemplo com o operador 

        in
        
"""

print( 'f' in meu_nome )
print( 'f' not in meu_nome)

"""porque isso aqui resultou em False?"""

'fe ' in meu_nome

"""para saber o tamanho de uma string, use o método 
        
        len(string)
"""

len(meu_nome)

"""agora crie duas strings e faça o que eu peço

        nome
        sobrenome

qual o último elemento de cada string?
"""



"""qual o tamanho de cada string?"""



"""selecione o terceiro elemento do nome,  o quarto elemento de  sobrenome 

junte eles numa variável única e imprima o resultado

"""



"""## bool

True or False

note que é preciso usar maiúscula inicial

rode a celula abaixo e veja o que acontece 
"""

a = 10
b = true

"""agora coloque do jeito certo e veja o que acontece"""



"""vamos fazer comparações para obter booleanos"""

a = 10
b = 11

"""aqui eu fiz uma comparação entre dois valores (a e b) e então joguei o resultado dessa comparação para a variável resposta1


"""

resposta1 = a < b
print(resposta1)

"""agora veja qual o tipo de variável é resposta1"""

a == 11

"""para fazer uma comparação do tipo 

numero_1 é igual a numero_2 

use 

        num1 == num2

compare a e b

# if elif else

para tomar decisões
"""



"""# loops

## for loop
"""



"""## while loop"""



"""# Listas"""



"""# tuple"""



"""# dictionary"""



"""# Funções"""

