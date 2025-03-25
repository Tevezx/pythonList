'''
#Somar números da lista
A=[3, 4, 5, 10]
soma1 = list()
for i in A:
    soma1 = soma1 + [i+1]
    #soma1.append(i+1)
print(soma1)
'''

'''
#Multiplicar números pares
A = [0, 0, 5, 3, 2, 7, 4, 10, 4, 7]
N = list()
for i in A:
    if i%2 == 0:
        N = N + [i*i]
        #N += [i*i]
print('Valor da lista N:', N)
'''

#Fatorial = !5
#int só pega número inteiro
x = int(input('digite: '))
fat = x
while x > 1:
    fat = fat * (x-1)
    x = x-1
print("Fatorial: ", fat)

