#criar um leitor xml que joga em um arquivo excel

import xmltodict
import os
import pandas as pd



def pegar_infos(arquivo,valores):
    # print(f"pegou a info da {arquivo}")
    with open(f'nfs/{arquivo}', 'rb') as arquivo_xml: 
        dic_arquivo = xmltodict.parse(arquivo_xml)
        # print(dic_arquivo)
        if "NFe" in dic_arquivo:
            info_nf = dic_arquivo["NFe"]["infNFe"]
        else:   
            info_nf = dic_arquivo['nfeProc']["NFe"]["infNFe"] 
        numero_nota = info_nf['@Id']
        empresa_emissora= info_nf['emit']['xNome']
        nome_cliente= info_nf['dest']['xNome']
        endereco= info_nf['dest']['enderDest']
        if "vol" in info_nf['transp']:
            peso=info_nf['transp']['vol']['pesoB']
        else:
            peso = "Peso nao informado"   
        valores.append([numero_nota,empresa_emissora,nome_cliente,endereco,peso])

lista_arquivo = os.listdir('nfs') 

colunas =['numero_nota','empresa_emissora','nome_cliente','endereco','peso']
valores =[]

for arquivo in lista_arquivo:
    pegar_infos(arquivo, valores)
    

tabela = pd.DataFrame(columns=colunas,data=valores)    
# print(tabela)
tabela.to_excel("notasfiscais.xlsx", index=False)