
import sys
import json

obras_set = set()

with open(sys.argv[1]) as entrada:
    for num_reg, lin in enumerate(entrada, 1):
        tipo, id_ol, versao, data, reg = lin.split('\t')
        reg = json.loads(reg)
        obras = reg.get('works', [])
        for obra in obras:
            obras_set.add(obra['key'])
            
print num_reg, ' registros lidos'
print len(obras_set), ' obras distintas'
for obra in sorted(obras_set):
    print obra
