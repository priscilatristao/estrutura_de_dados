# Estrutura de Dados - Projeto P1


![image](https://user-images.githubusercontent.com/125207561/227806419-e7b414db-a97d-4a29-a3a3-4f82564f32e1.png)



ENGENHARIA DE SOFTWARE – 3º Período

Disciplina: Estrutura de Dados

Prof.: Márcio Alexandre Dias Garrido
-----------------------

Membros da Equipe: Angélica Gomes da Silva, Gabriel Silva Provietti da Costa, Priscila Paula Lima Tristão, Quézia Trindade Moura e Robson Ceia de Oliveira.
-----------------------

MARICÁ - RJ
2023
-----------------------

PROJETO

 - Tendo em vista o conjunto de elementos abaixo, criar um algoritimo que seja capaz de ordenar de forma crescente e decrescente, assim como imprimir de forma gráfica a notação Big’O do seu resultado
//Entrada
elementos = [[0,1,2,3],[11,12,13,4],[10,15,14,5],[9,8,7,6],]
//Saída
[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15];
------------------------

CÓDIGO

 - 1ª Forma:
Foram criadas 4(quatro) variáveis, cada uma recebendo uma lista contendo 4(quatro) números dispostos aleatoriamente, e uma variável que recebe uma lista vazia. Logo abaixo foi usado o método .append, para adicionar os elementos de cada lista na lista vazia.

![image](https://user-images.githubusercontent.com/125207561/227806621-d0e9d99e-de2e-4bfd-b3da-78b936bf8d13.png)


Para organizar todos os elementos em ordem crescente foi utilizada a função sorted(), especificando a posição(índice) de cada lista dentro da matriz. E em seguida é dado o print da variável que recebe estas informações, como mostra a imagem abaixo.

![image](https://user-images.githubusercontent.com/125207561/227806633-83240b66-b127-4c6e-b3b1-435ffabd81a9.png)

-----------------------


 - 2ª Forma:
Nesta outra forma em que o código foi feito, o início permanece o mesmo. A mudança, no entanto, começa na linha após o uso do append, onde ao invés de 1(uma) variável para receber as informações organizadas, 4(quatro) variáveis são criadas, cada uma recebendo um índice diferente disposto na lista elementos, que representam as listas iniciais. E para finalizar, é usado o print com a função sorted somando as quatro variáveis.

![image](https://user-images.githubusercontent.com/125207561/227806657-3b666706-885c-4b0f-ba1e-28c75ffe8c69.png)


-------------------------


NOTAÇÃO BigO’

A notação destes algoritmos é O(n log n) já que o tempo de execução cresce conforme a entrada de dados vão aumentando.
A atividade mais significativa do código é a função sorted e conforme a entrada de dados for maior ela "trabalhará" mais, já que tem que ordenar mais elementos.
São 4 entradas de 4 elementos cada, logo, 4*4=16, a notação será O(16log16).
16log16 = 16 * 4 = 64.
Resultado final da notação O(64).






