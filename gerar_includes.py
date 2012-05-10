# coding: utf-8

from glob import glob
import os

for path_arq in glob('src-ora/*.py'):
    _, nome_arq = os.path.split(path_arq)
    cap, ex, tit = nome_arq.split('-',2)
    cap = int(cap[2:])
    ex = int(ex)
    tit = tit[:-3].replace('-', ' ').capitalize()
    chamada = '%s.%s. %s' % (cap, ex, tit)
    print chamada
    print '-' * len(chamada)
    print
    print '.. literalinclude::', path_arq
    print '   :linenos:'
    print
    print

