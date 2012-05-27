
========================
Códigos de Áreas do IBGE
========================

Conforme a página oficial do IBGE_:

  A Tabela de Códigos de Municípios, elaborada pelo IBGE, apresenta a lista
  dos municípios brasileiros associados a um código composto de 7 dígitos, 
  sendo os dois primeiros referentes ao código do estado.

.. _IBGE: http://www.ibge.gov.br/concla/cod_area/cod_area.php

Na prática, os dados encontrados em formato .DBF contém mais do que os
municípios, mas também distritos, subdistritos, bairros e setores, em
uma hierarquia de códigos de 7 a 15 dígitos, respectivamente.

Fonte dos dados:

ftp://geoftp.ibge.gov.br/organizacao_territorial/localidades/Shapefile_SHP/BR_Localidades_2010_v1.dbf

Descrição dos Campos
====================

Descrição dos Campos Finais para Features Geomedia, Shape e KML de Pontos de
Localidades 2010 em 28/11/2011. 

Tabela convertida da Planilha .XLS encontrada em: 
ftp://geoftp.ibge.gov.br/organizacao_territorial/localidades/descritivo_campos_localidades_2010.xls

== ============== ========== ========== ====== =================================================================
#  Geomedia e KML Shape      Tipo       Tam.   Descrição                                                          
== ============== ========== ========== ====== =================================================================
1  ID             ID         Autonumber -      Contagem automárica de geometrias ponto oriundas de setor           
2  CD_GEOCODIGO   CD_GEOCODI Text       20     Geocódigo do setor (15 dígitos numéricos)                         
3  TIPO           TIPO       Text       10     Classificação de Tipo (Urbano ou Rural, 6 dígitos alfa-numéricos)
4  CD_GEOCODBA    CD_GEOCODB Text       20     Geocódigo do bairro (12 dígitos numéricos)                        
5  NM_BAIRRO      NM_BAIRRO  Text       60     Nome do bairro                                                       
6  CD_GEOCODSD    CD_GEOCODS Text       20     Geocódigo do subdistrito (11 dígitos numéricos)                   
7  NM_SUBDISTRITO NM_SUBDIST Text       60     Nome do subdistrito                                                  
8  CD_GEOCODDS    CD_GEOCODD Text       20     Geocódigo do distrito (9 dígitos numéricos)                       
9  NM_DISTRITO    NM_DISTRIT Text       60     Nome do distrito                                                     
10 CD_GEOCODMU    CD_GEOCODM Text       20     Geocódigo do Município (7 dígitos numéricos)                     
11 NM_MUNICIPIO   NM_MUNICIP Text       60     Nome do Município                                                   
12 NM_MICRO       NM_MICRO   Text       100    Nome Micro-região                                                   
13 NM_MESO        NM_MESO    Text       100    Nome Meso-região                                                    
14 NM_UF          NM_UF      Text       60     Nome da UF                                                           
15 CD_NIVEL       CD_NIVEL   Text       1      Código do Nível da Localidade                                      
16 CD_CATEGORIA   CD_CATEGOR Text       5      Código da Categoria da Localidade                                   
17 NM_CATEGORIA   NM_CATEGOR Text       50     Nome da Categoria da Localidade                                      
18 NM_LOCALIDADE  NM_LOCALID Text       60     Nome da Localidade                                                   
19 LONG           LONG       Double     6 dec. Longitude da Localidade em grau decimal                              
20 LAT            LAT        Double     6 dec. Latitude da Localidade em grau decimal                               
21 ALT            ALT        Double     2 dec. Altitude da Localidade, oriunda de SRTM em metros                    
== ============== ========== ========== ====== =================================================================


=====================
Testes com o Mongo DB
=====================


Carga para o MongoDB
====================

Conversão de .DBF para JSON pronto para importar::

	$ python dbf2mongo.py > localidades.mongoimport

Contagem do número de linhas::

  $ wc -l localidades.mongoimport 
     21886 localidades.mongoimport

Importação::

  $ mongoimport -d ibge -c localidades localidades.mongoimport







