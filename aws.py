import json
import pandas as pd  
import unidecode 
import boto3 
from io import StringIO
import logging



def lambda_handler(event, context):
    try:
         # Configuração do logging
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        
        #criando um cliente S3
        s3 = boto3.client('s3')
        
            
        #lendo o arquivo CSV do S3
        s3_bucket = 's3-recife-accidents-data'
        s3_key = '2.depara/rpa_regiao_mapping.csv'
        response = s3.get_object(Bucket=s3_bucket, Key=s3_key)
        content = response['Body'].read().decode('utf-8')
        
        # criando dataframe a partir dos dados do csv
        regiao = pd.read_csv(StringIO(content), delimiter=",")
        
        #Bases de acidentes de transito
        df_2019 = pd.read_csv("http://dados.recife.pe.gov.br/dataset/44087d2d-73b5-4ab3-9bd8-78da7436eed1/resource/3531bafe-d47d-415e-b154-a881081ac76c/download/acidentes-2019.csv", delimiter=";")
        df_2020 = pd.read_csv("http://dados.recife.pe.gov.br/dataset/44087d2d-73b5-4ab3-9bd8-78da7436eed1/resource/fc1c8460-0406-4fff-b51a-e79205d1f1ab/download/acidentes_2020-novo.csv", delimiter=";")
        df_2021 = pd.read_csv("http://dados.recife.pe.gov.br/dataset/44087d2d-73b5-4ab3-9bd8-78da7436eed1/resource/2caa8f41-ccd9-4ea5-906d-f66017d6e107/download/acidentes2021.csv", delimiter=";")
        df_2022 = pd.read_csv("http://dados.recife.pe.gov.br/dataset/44087d2d-73b5-4ab3-9bd8-78da7436eed1/resource/971e0228-fa9c-4a42-b360-c842b29d2f56/download/acidentes2022.csv", delimiter=";")
        
        #Base com codigos dos bairros do Recife
        bairros_recife = pd.read_csv("http://dados.recife.pe.gov.br/dataset/c1f100f0-f56f-4dd4-9dcc-1aa4da28798a/resource/698d8fe1-d30a-485f-8d5d-307d46163d0c/download/bairro.csv", delimiter=";")
    
        
        # Base de relação dos codigos RPA e regiao dos bairros do recife
        #regiao = pd.read_csv("rpa_regiao_mapping.csv", delimiter=",")
        
        # TRATAMENTOS 2019
        
        # Colunas selecionadas para o estudo na base de 2019
        colunas_selecionadas_2019 = [ "DATA", "hora", "natureza_acidente","situacao","bairro", "auto", "moto", "ciclom",	"ciclista",	"pedestre",	"onibus",	"caminhao",	"viatura",	"outros",	"vitimas", "tempo_clima","sinalizacao",	"condicao_via",	"conservacao_via","mao_direcao" ]
        
        df_2019_sot = df_2019[colunas_selecionadas_2019]
        
        #Tratamento para valores nulos 
        valores_nulos_2019 = {"hora": '00:00', "natureza_acidente":'OUTROS', "situacao":'OUTROS',"bairro":'OUTROS', "auto":'0', "moto":'0', "ciclom":'0', "ciclista":'0',	"pedestre":'0',"onibus":'0', "caminhao":'0', "viatura":'0',	"outros":'0', "vitimas":'0', "tempo_clima":'OUTROS',"sinalizacao":'OUTROS',	"condicao_via":'OUTROS',	"conservacao_via":'OUTROS',"mao_direcao":'OUTROS'  }
        
        df_2019_sot = df_2019_sot.fillna(valores_nulos_2019)
        
        # Convertendo colunas para inteiros
        int_columns_2019 = ['auto', 'moto', 'ciclom', 'ciclista', 'pedestre', 'onibus', 'caminhao', 'viatura', 'outros', 'vitimas']
        df_2019_sot[int_columns_2019] = df_2019_sot[int_columns_2019].fillna(0).astype(int)
        
        # tratamento de mudar o tipo de dado do campo DATA
        df_2019_sot['DATA'] = pd.to_datetime(df_2019_sot['DATA'])
        
        #Deixando todas as colunas em maiusculo
        df_2019_sot.columns = df_2019_sot.columns.str.upper()
        
        
        # TRATAMENTOS 2020
        
        # Colunas selecionadas para o estudo na base de 2020
        colunas_selecionadas_2020 = ['data', 'hora', 'natureza_acidente', 'situacao', 'bairro', 'tipo', 'auto', 'moto', 'ciclom', 'ciclista', 'pedestre', 'onibus', 'caminhao', 'viatura', 'outros', 'vitimas', 'acidente_verificado', 'tempo_clima', 'sinalizacao', 'condicao_via', 'conservacao_via', 'mao_direcao']
        
        df_2020_sot = df_2020[colunas_selecionadas_2020]
        
        #Tratamento para valores nulos 
        valores_nulos = { "natureza_acidente":'OUTROS', "situacao":'OUTROS',"bairro":'OUTROS', "auto":'0', "moto":'0', "ciclom":'0', "ciclista":'0',	"pedestre":'0',"onibus":'0', "caminhao":'0', "viatura":'0',	"outros":'0', "vitimas":'0', "tempo_clima":'OUTROS',"sinalizacao":'OUTROS',	"condicao_via":'OUTROS', "acidente_verificado":'Outros'	,"conservacao_via":'OUTROS',"mao_direcao":'OUTROS'}
        df_2020_sot = df_2020_sot.fillna(valores_nulos)
        
        # Convertendo colunas para inteiros
        int_columns = ['auto', 'moto', 'ciclom', 'ciclista', 'pedestre', 'onibus', 'caminhao', 'viatura', 'outros', 'vitimas']
        df_2020_sot[int_columns] = df_2020_sot[int_columns].fillna(0).astype(int)
        
        # Convertendo colunas para string
        str_columns = ['hora', 'natureza_acidente', 'situacao', 'bairro', 'tipo', 'tempo_clima', 'condicao_via', 'conservacao_via', 'mao_direcao']
        df_2020_sot[str_columns] = df_2020_sot[str_columns].astype(str).apply(lambda x: x.str.upper())
        
        # tratamento de mudar o tipo de dado do campo DATA
        df_2020_sot['data'] = pd.to_datetime(df_2020_sot['data'])
        
        #Deixando todas as colunas em maiusculo
        df_2020_sot.columns = df_2020_sot.columns.str.upper()
        
        
        
        # TRATAMENTOS 2021
        
        # Colunas selecionadas para o estudo na base de 2021
        colunas_selecionadas_2021 = ['data', 'hora', 'natureza_acidente', 'situacao', 'bairro', 'tipo', 'auto', 'moto', 'ciclom', 'ciclista', 'pedestre', 'onibus', 'caminhao', 'viatura', 'outros', 'vitimas', 'acidente_verificado', 'tempo_clima', 'sinalizacao', 'condicao_via', 'conservacao_via', 'mao_direcao']
        
        df_2021_sot = df_2021[colunas_selecionadas_2021]
        
        #Tratamento para valores nulos 
        valores_nulos_2021 = {"bairro":'OUTROS', "tipo":'OUTROS',"acidente_verificado":'Outros',	"tempo_clima":'OUTROS',"sinalizacao":'OUTROS',	"condicao_via":'Outros',"conservacao_via":'OUTROS',"mao_direcao":'OUTROS'}
        
        df_2021_sot = df_2021_sot.fillna(valores_nulos_2021)
        
        # Convertendo colunas para inteiros
        int_columns_2021 = ['auto', 'moto', 'ciclom', 'ciclista', 'pedestre', 'onibus', 'caminhao', 'viatura', 'outros', 'vitimas']
        df_2021_sot[int_columns_2021] = df_2021_sot[int_columns_2021].fillna(0).astype(int)
        
        # Convertendo colunas para string
        str_columns_2021 = ['hora', 'natureza_acidente', 'situacao', 'bairro', 'tipo', 'tempo_clima', 'condicao_via', 'conservacao_via', 'mao_direcao']
        df_2021_sot[str_columns_2021] = df_2021_sot[str_columns_2021].astype(str).apply(lambda x: x.str.upper())
        
        # tratamento de mudar o tipo de dado do campo DATA
        df_2021_sot['data'] = pd.to_datetime(df_2021_sot['data'])
        
        #Deixando todas as colunas em maiusculo
        df_2021_sot.columns = df_2021_sot.columns.str.upper()
        
        
        # tratamento 2022
        
        # Colunas selecionadas para o estudo na base de 2022
        colunas_selecionadas_2022 = ['data', 'hora', 'natureza', 'situacao', 'bairro', 'tipo', 'auto', 'moto', 'ciclom', 'ciclista', 'pedestre', 'onibus', 'caminhao', 'viatura', 'outros', 'vitimas', 'acidente_verificado', 'tempo_clima', 'sinalizacao', 'condicao_via', 'conservacao_via', 'mao_direcao']
        df_2022_sot = df_2022[colunas_selecionadas_2022]
        
        #Tratamento para valores nulos 
        valores_nulos_2022 = {"bairro":'OUTROS', "tipo":'OUTROS', "tempo_clima":'OUTROS', "sinalizacao":'OUTROS', "condicao_via":'Outros',"conservacao_via":'OUTROS',"mao_direcao":'OUTROS', "acidente_verificado":'Outros'}
        
        df_2022_sot = df_2022_sot.fillna(valores_nulos_2022)
        
        # Convertendo colunas para inteiros
            # Lista de colunas que você deseja converter para inteiros
        int_columns_2022 = ['auto', 'moto', 'ciclom', 'ciclista', 'pedestre', 'onibus', 'caminhao', 'viatura', 'outros', 'vitimas']
        
            # Substituir vírgulas por pontos e converter para float
        df_2022_sot[int_columns_2022] = df_2022_sot[int_columns_2022].replace(',', '.', regex=True).astype(float)
        
            # Converter para inteiros
        df_2022_sot[int_columns_2022] = df_2022_sot[int_columns_2022].fillna(0).astype(int)
        
        # Convertendo colunas para string
        str_columns_2022 = ['hora', 'natureza', 'situacao', 'bairro', 'tipo', 'tempo_clima', 'condicao_via', 'conservacao_via', 'mao_direcao']
        
        df_2022_sot[str_columns_2022] = df_2022_sot[str_columns_2022].astype(str).apply(lambda x: x.str.upper())
        
        # tratamento de mudar o tipo de dado do campo DATA
        df_2022_sot['data'] = pd.to_datetime(df_2022_sot['data'])
        
        #Mudança do nome do campo natureza para natureza_acidente
        df_2022_sot = df_2022_sot.rename(columns={'natureza': 'natureza_acidente'})
        
        #no campo acidente_verificado onde tiver nao informado transformar para outros
        df_2022_sot['acidente_verificado'] = df_2022_sot['acidente_verificado'].replace('Não informado', 'OUTROS')
        
        #Deixando todas as colunas em maiusculo
        df_2022_sot.columns = df_2022_sot.columns.str.upper()
        
        # TRATAMENTO BAIRROS-RECIFE
        
        #transformação do campo de bairro em string, sem acentos e maiuculo
        bairros_recife['Bairro'] = bairros_recife['Bairro'].astype(str).apply(lambda x: unidecode.unidecode(x).upper())
        
        #Deixando todas as colunas em maiusculo
        bairros_recife.columns = bairros_recife.columns.str.upper()
        
        
        # Crie uma lista com os DataFrames
        dfs = [df_2019_sot, df_2020_sot, df_2021_sot, df_2022_sot]
        
        # Use a função concat para empilhar verticalmente os DataFrames
        df_total = pd.concat(dfs, ignore_index=True)
        
        
        # Unir os DataFrames com base no campo "BAIRROS" e "BAIRRO"
        df_unido = pd.merge(df_total, bairros_recife, how='left', left_on='BAIRRO', right_on='BAIRRO')
        
        
        # Unir os DataFrames com base no campo "RPA"
        df_final = pd.merge(df_total, regiao, how='left', left_on='RPA', right_on='RPA')
        
        #Salvar dados no csv
        s3_output_path = '1.data_processed/spec_acidentes_transito_recife.csv'
        bucket = 's3-recife-accidents-data'
        csv_buffer = StringIO()
        df_final.to_csv(csv_buffer)
        s3_resource = boto3.resource('s3')
        s3_resource.Object(s3_bucket, s3_output_path).put(Body=csv_buffer.get_object())
        
        
        except Exception as e:
            logger.info(e)
     
    
    
    
        return {
            'statusCode': 200,
            'body': json.dumps(f'Especializada de acidentes de trânsito salva em {s3_output_path}')
    }
    
    