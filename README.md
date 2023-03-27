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
O código começa com uma variável que recebe uma matriz. Dentro há 4(quatro) listas, cada uma contendo 4(quatro) números dispostos aleatoriamente.

![image](https://user-images.githubusercontent.com/125207561/227814356-4778a3b0-212e-405d-9dc2-2f7afbb329f5.png)


Em seguida, 4(quatro) variáveis são criadas, cada uma recebendo um índice diferente disposto na matriz elementos, representando as listas dentro dela. E assim, é dado o print da soma das variáveis que recebe estas informações, utilizando a função sorted para organizar todos os elementos em ordem crescente, como mostra a imagem abaixo.

![image](https://user-images.githubusercontent.com/125207561/227814376-8bd9ec36-ba7b-4961-b1d2-eca958ffaaca.png)

-----------------------


 - 2ª Forma:
Nesta outra forma em que o código foi feito, o início permanece o mesmo. A mudança, no entanto, começa após a matriz, onde ao invés de criar 4(quatro) variáveis para receber uma lista cada, é apenas criada 1(uma) variável que recebe a somatória dos índices da matriz utilizando a função sorted para colocar em ordem crescente. Finalizando com um print da variável.

![image](https://user-images.githubusercontent.com/125207561/227814322-f1df34d0-884a-46dc-904a-a49307552ec0.png)

-------------------------


NOTAÇÃO BigO’

A notação destes algoritmos é O(n log n) já que o tempo de execução cresce conforme a entrada de dados vão aumentando.
A atividade mais significativa do código é a função sorted e conforme a entrada de dados for maior ela "trabalhará" mais, já que tem que ordenar mais elementos.
São 4 entradas de 4 elementos cada, logo, 4*4=16, a notação será O(16log16).
16log16 = 16 * 4 = 64.
Resultado final da notação O(64).

Ferramenta utilizada para a pesquisa sobre a notação:

https://www.freecodecamp.org/portuguese/news/o-que-e-a-notacao-big-o-complexidade-de-tempo-e-de-espaco/

Neste artigo, nas primeiras colocações é feita um exemplo onde o mesmo utiliza o método sort, porém diferente do nosso projeto, no codepen foi utilizado uma quantidade fixa de elementos (de 1 a 8) assim tornando a notação O(n²).

Neste artigo também é classificado cada notação, segue uma interesante imagem tirada do mesmo.

![image](https://user-images.githubusercontent.com/82628852/228040972-a34cbf99-d8a7-40a6-8bd7-9e722a8e65e2.png)

Nesta imagem é possível classificar as notações e seu nível de complexidade.
