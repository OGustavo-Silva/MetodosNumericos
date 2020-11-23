import sympy
n = int(input('Informe a qtd de pontos: '))

lista_pontos = []
for _ in range(n):
    ponto = list(map(float, input('Informe x,y separados por espaço: ').split(' ')))
    print('ponto adicionado: {}'.format(ponto))
    lista_pontos.append(ponto)

X = sympy.symbols('X')
p = 0
for i in range(n):
    t = 1
    for j in range(n):
        if j != i:
            print('{} * ({} - {}/{} - {})'.format(t, X, lista_pontos[j][0], lista_pontos[i][0], lista_pontos[j][0]))
            t = t*( (X-lista_pontos[j][0])/(lista_pontos[i][0]-lista_pontos[j][0]) )
    p += t*lista_pontos[i][1]
print('--------------------------')
print('Resultado:', sympy.simplify(p))
