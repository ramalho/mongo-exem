
import sys
import json

autores_set = set()

with open(sys.argv[1]) as entrada:
    for num_reg, lin in enumerate(entrada, 1):
        tipo, id_ol, versao, data, reg = lin.split('\t')
        reg = json.loads(reg)
        autores = reg.get('authors', [])
        for autor in autores:
            autores_set.add(autor['key'])
            
print num_reg, ' registros lidos'
print len(autores_set), ' autores distintos'
for au in sorted(autores_set):
    print au
