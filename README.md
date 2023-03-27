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

![image](https://user-images.githubusercontent.com/125207561/228072963-85cc22d0-555f-4b97-aca0-d5f52805a792.png)


Em seguida, 4(quatro) variáveis são criadas, cada uma recebendo um índice diferente disposto na matriz elementos, representando as listas dentro dela. Depois é criado uma nova variável que recebe a junção das variáveis anteriores, utilizando a função sorted para organizar todos os elementos em ordem crescente. E assim, é dado o print da nova variável, como mostra a imagem abaixo.

![image](https://user-images.githubusercontent.com/125207561/228073004-ed508dd8-df82-43aa-8b26-2d291937d5db.png)


E para criar a ordem decrescente,  a mesma variável foi reutilizada porém agora junta a função reverse(), que inverte a ordem de uma lista. Logo em seguida é dado o print.

![image](https://user-images.githubusercontent.com/125207561/228073055-db02ee5e-8541-4163-acd8-68244fc31a4d.png)

-----------------------


 - 2ª Forma:
Nesta outra forma em que o código foi feito, o início permanece o mesmo. A mudança, no entanto, começa após a matriz, onde ao invés de criar 4(quatro) variáveis para receber uma lista cada, é apenas criada 1(uma) variável que recebe a junção dos índices da matriz utilizando a função sorted para colocar em ordem crescente. Finalizando com um print da variável. E para inverte a ordem foi feito o mesmo processo que o código anterior.

![image](https://user-images.githubusercontent.com/125207561/228073103-205fde32-a28a-4ba5-8f7e-731ae481e5ef.png)

-------------------------


NOTAÇÃO BigO’

A notação destes algoritmos é O(n²) já que o tempo de execução cresce conforme a entrada de dados vão aumentando.
A atividade mais significativa do código é a função sorted e conforme a entrada de dados for maior ela "trabalhará" mais, já que tem que ordenar mais elementos.
São 4 entradas de 4 elementos cada, logo, 4*4=16, a notação será O(16²).
16² = 16 * 16 = 64.
Resultado final da notação O(256).

Ferramenta utilizada para a pesquisa sobre a notação:

https://www.freecodecamp.org/portuguese/news/o-que-e-a-notacao-big-o-complexidade-de-tempo-e-de-espaco/

Neste artigo, nas primeiras colocações é exibido um exemplo onde o mesmo também utiliza o método sort.

Neste artigo também é classificado cada notação, segue uma interesante imagem tirada do mesmo.

![BigO'cheatsheet](https://user-images.githubusercontent.com/82628852/228044983-aa7f05ee-9306-4be8-ba8e-75884eaf79bd.png)

Nesta imagem é possível classificar as notações e seu nível de complexidade.
