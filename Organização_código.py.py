#Tendo em vista o conjunto de elementos abaixo, criar um algoritimo que seja capaz de ordenar de forma crescente e decrescente, 
#assim como imprimir de forma gráfica a notação Big’O do seu resultado //Entrada elementos = [[0,1,2,3],[11,12,13,4],[10,15,14,5],[9,8,7,6],]
#//Saída [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15];



'''elementos = [[0,1,2,3],[11,12,13,4],[10,15,14,5],[9,8,7,6],]
//Saida
[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15];'''

elementos = [[0,1,2,3],
             [11,12,13,4],
             [10,15,14,5],
             [9,8,7,6]]

e1 = elementos[0]
e2 = elementos[1]
e3 = elementos[2]
e4 = elementos[3]

e = sorted(e1 + e2 + e3 + e4)

print(f'Ordem Crescente: {e}')

e.reverse()

print(f'Ordem Decrescente: {e}')


