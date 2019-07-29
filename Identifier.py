from enum import Enum
from PIL import Image
from scipy.misc import imsave
import os
import numpy 
import webbrowser
import pytesseract
import time
import pyautogui
from datetime import datetime

startTime = datetime.now()


class TipoDocumento(Enum):
    Nao_Encontrado = 0
    Consulta_SPC_pg_1 = 1
    Consulta_SPC_pg_2 = 2
    Notificação_Manutenção_pg_1 = 3
    Notificação_Manutenção_pg_2 = 4
    Proposta_Adesao_pg_1 = 5
    Proposta_Adesao_pg_2 = 6
    Proposta_Adesao_Coletivo_pg_1 = 7
    Proposta_Adesao_Coletivo_pg_2 = 8
    Proposta_Contratacao_pg_1 = 9
    Proposta_Contratacao_pg_2 = 10
    Proposta_Contratacao_Individual_pg_1 = 11
    Proposta_Contratacao_Individual_pg_2 = 12
    Proposta_Inscricao_pgbl_pg_1 = 13
    Proposta_Inscricao_pgbl_pg_2 = 14
    Proposta_Inscricao_vgbl_pg_1 = 15
    Proposta_Inscricao_vgbl_pg_2 = 16
    Proposta_Inscricao_vgbl_pg_3 = 17
    
#Define o caminho para o pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
#Vai até o caminho onde todos documentos se encontram
DIR_NAME = "C:/Users/3muri/Desktop/ITPower/Projetos/ITAU - DIP (18.10)/Sistema/DIP_OCR/OCR_DATABOOK/DOCS"
#Lista todos arquivos dentro da pasta definida
files = os.listdir(DIR_NAME) 
#Separa os arquivos dentro de um array
files = sorted(files)

#Faz um loop entre os nomes de todos arquivos
for file in files:
    startTimeDocument = datetime.now()
    #Abre a imagem do documento dentro de uma variável
    Imagem_Upload = Image.open(DIR_NAME + "/" + file)
    #Executa o pytesseract para converter a imagem em texto
    Texto_Doc = pytesseract.image_to_string(Imagem_Upload, lang="por")

    #Condições para definir qual tipo de documento é
    if Texto_Doc.upper().find('CLICK') != -1: #Consulta SPC - pg 1
        
        #Define a váriavel de controle de documento pelo enumerador do documento específico
        TipoDocumentoAtual = TipoDocumento.Consulta_SPC_pg_1

    elif Texto_Doc.upper().find('PESSOAL PLUS') != -1: #Consulta SPC - pg 2   
        #print(file + ': Consulta SPC - pg 2')
        #Define a váriavel de controle de documento pelo enumerador do documento específico
        TipoDocumentoAtual = TipoDocumento.Consulta_SPC_pg_2

    elif Texto_Doc.upper().find('DESTINATÁRIO DO OBJETO / DESTINATAIRE') != -1: #Notificação Manutenção - pg 1
        #print(file + ': Notificação Manutenção - pg 1')
        #Define a váriavel de controle de documento pelo enumerador do documento específico
        TipoDocumentoAtual = TipoDocumento.Notificação_Manutenção_pg_1

    elif Texto_Doc.upper().find('SULAMERICA SEGUROS DE PESSOAS E PREVIDENCIA') != -1 and Texto_Doc.upper().find('R.') != -1: #Notificação Manutenção - pg 2
        #print(file + ': Notificação Manutenção - pg 2')
        #Define a váriavel de controle de documento pelo enumerador do documento específico
        TipoDocumentoAtual = TipoDocumento.Notificação_Manutenção_pg_2

    elif Texto_Doc.upper().find('PROPOSTA DE ADESÃO') != -1 and Texto_Doc.upper().find('DADOS DO ESTIPULANTE') != -1: #Proposta de Adesão - pg 1
        #print(file + ': Proposta de Adesão - pg 1')
        #Define a váriavel de controle de documento pelo enumerador do documento específico
        TipoDocumentoAtual = TipoDocumento.Proposta_Adesao_pg_1

    elif Texto_Doc.upper().find('PROPOSTA DE ADESÃO') != -1 and Texto_Doc.upper().find('FORMA DE CUSTEIO') != -1: #Proposta de Adesão - pg 2
        #print(file + ': Proposta de Adesão - pg 2')
        #Define a váriavel de controle de documento pelo enumerador do documento específico
        TipoDocumentoAtual = TipoDocumento.Proposta_Adesao_pg_2

    elif Texto_Doc.upper().find('PROPOSTA DE ADESÃO') != -1 and Texto_Doc.upper().find('DADOS DO PROPONENTE PRINCIPAL') != -1: #Proposta de Adesão Coletivo - pg 1
        #print(file + ': Proposta de Adesão Coletivo - pg 1')
        #Define a váriavel de controle de documento pelo enumerador do documento específico
        TipoDocumentoAtual = TipoDocumento.Proposta_Adesao_Coletivo_pg_1

    elif Texto_Doc.upper().find('PROPOSTA DE ADESÃO') != -1 and Texto_Doc.upper().find('TEM OU TEVE PROBLEMAS NAS') != -1: #Proposta de Adesão Coletivo - pg 2
        #print(file + ': Proposta de Adesão Coletivo - pg 2')
        #Define a váriavel de controle de documento pelo enumerador do documento específico
        TipoDocumentoAtual = TipoDocumento.Proposta_Adesao_Coletivo_pg_2

    elif Texto_Doc.upper().find('PROPOSTA INDIVIDUAL') != -1 and Texto_Doc.upper().find('GBL)') != -1 and Texto_Doc.upper().find('DADOS DA PROPOSTA') != -1: #Proposta de Contratação - pg 1
        #print(file + ': Proposta de Contratação - pg 1')
        #Define a váriavel de controle de documento pelo enumerador do documento específico
        TipoDocumentoAtual = TipoDocumento.Proposta_Contratacao_pg_1

    elif Texto_Doc.upper().find('PROPOSTA INDIVIDUAL') != -1 and Texto_Doc.upper().find('TABELA REGRESSIVA') != -1: #Proposta de Contratação - pg 2
        #print(file + ': Proposta de Contratação - pg 2')
        #Define a váriavel de controle de documento pelo enumerador do documento específico
        TipoDocumentoAtual = TipoDocumento.Proposta_Contratacao_pg_2

    elif Texto_Doc.upper().find('PROPOSTA INDIVIDUAL') != -1 and Texto_Doc.upper().find('FORMA DE PAGAMENTO') != -1: #Proposta de Contratação individual - pg 1
        #print(file + ': Proposta de Contratação individual - pg 1')
        #Define a váriavel de controle de documento pelo enumerador do documento específico
        TipoDocumentoAtual = TipoDocumento.Proposta_Contratacao_Individual_pg_1

    elif Texto_Doc.upper().find('PROPOSTA DE CONTRATAÇÃO') != -1 and Texto_Doc.upper().find('ESTA DECLARAÇÃO DEVERÁ') != -1: #Proposta de Contratação individual - pg 2
        #print(file + ': Proposta de Contratação individual - pg 2')
        #Define a váriavel de controle de documento pelo enumerador do documento específico
        TipoDocumentoAtual = TipoDocumento.Proposta_Contratacao_Individual_pg_2

    elif Texto_Doc.upper().find('PGBL') != -1 and Texto_Doc.upper().find('DADOS DA PROPOSTA') != -1: #Proposta de Inscrição PGBL - pg 1
        #print(file + ': Proposta de Inscrição PGBL - pg 1')
        #Define a váriavel de controle de documento pelo enumerador do documento específico
        TipoDocumentoAtual = TipoDocumento.Proposta_Inscricao_pgbl_pg_1

    elif Texto_Doc.upper().find('PGBL') != -1 and Texto_Doc.upper().find('DECLARAÇÃO DE ACEITE') != -1: #Proposta de Inscrição PGBL - pg 2
        #print(file + ': Proposta de Inscrição PGBL - pg 2')
        #Define a váriavel de controle de documento pelo enumerador do documento específico
        TipoDocumentoAtual = TipoDocumento.Proposta_Inscricao_pgbl_pg_2

    elif Texto_Doc.upper().find('VGBL') != -1 and Texto_Doc.upper().find('DADOS DA PROPOSTA') != -1: #Proposta de Inscrição VGBL - pg 1
        #print(file + ': Proposta de Inscrição VGBL - pg 1')
        #Define a váriavel de controle de documento pelo enumerador do documento específico
        TipoDocumentoAtual = TipoDocumento.Proposta_Inscricao_vgbl_pg_1

    elif Texto_Doc.upper().find('VGBL') != -1 and Texto_Doc.upper().find('TAF') != -1: #Proposta de Inscrição VGBL - pg 2
        #print(file + ': Proposta de Inscrição VGBL - pg 2')
        #Define a váriavel de controle de documento pelo enumerador do documento específico
        TipoDocumentoAtual = TipoDocumento.Proposta_Inscricao_vgbl_pg_2

    elif Texto_Doc.upper().find('VGBL') != -1 and Texto_Doc.upper().find('ELEGIBILIDADE AO') != -1: #Proposta de Inscrição VGBL - pg 3
        #print(file + ': Proposta de Inscrição VGBL - pg 3')
        #Define a váriavel de controle de documento pelo enumerador do documento específico
        TipoDocumentoAtual = TipoDocumento.Proposta_Inscricao_vgbl_pg_3

    else:
        #print(file + ': Não encontrado')
        TipoDocumentoAtual = TipoDocumento.Nao_Encontrado


    print(file + ': ' + str(TipoDocumentoAtual) + "    //Tempo de Processamento: " + str(datetime.now() - startTimeDocument))
    


print("Tempo de duração total: " + str(datetime.now() - startTime))
