
import sys
import json

editoras = set()

with open(sys.argv[1]) as entrada:
    for num_reg, lin in enumerate(entrada, 1):
        tipo, id_ol, versao, data, reg = lin.split('\t')
        reg = json.loads(reg)
        pubs = reg.get('publishers', [])
        for pub in pubs:
            editoras.add(pub)
            
print num_reg, ' registros lidos'
print len(editoras), ' editoras distintas'
for ed in sorted(editoras):
    print ed
