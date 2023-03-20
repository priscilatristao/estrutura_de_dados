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

print(sorted(e1 + e2 + e3 + e4))


'''outra forma'''


Elementos = [[0,1,2,3],
             [11,12,13,4],
             [10,15,14,5],
             [9,8,7,6]]

E = sorted(Elementos[0] + Elementos[1] + Elementos[2] + Elementos[3])

print(E)
