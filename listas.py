compras = ['leite', 'couve', 'tomate']
compras.append('frango')
print(compras)
['leite', 'couve', 'tomate', 'frango']


compras = ['leite', 'couve', 'tomate']
compras.insert(1, 'queijo')
print(compras)
['leite', 'queijo', 'couve', 'tomate']

compras = ['leite', 'couve', 'tomate']
compras.extend(['sal', 'arroz', 'ovos'])
print(compras)
['leite', 'couve', 'tomate', 'sal', 'arroz', 'ovos']

compras1 = ['leite', 'couve', 'tomate']
compras2 = ['sal', 'arroz', 'ovos']
compras = compras1 + compras2
print(compras)
['leite', 'couve', 'tomate', 'sal', 'arroz', 'ovos']


compras = ['leite', 'couve', 'tomate']
del(compras[2])
print(compras)
['leite', 'couve']

compras = ['leite', 'couve', 'tomate']
print(compras.pop(0))
leite
print(compras)
['couve', 'tomate']

compras = ['leite', 'couve', 'tomate']
compras[:2] = []
print(compras)
['tomate']


compras = ['leite', 'couve', 'tomate']
print('leite' in compras)
True
print('ovos' in compras)
False