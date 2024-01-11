# Metadados para o conjunto de dados de Acidente de Transito 

## Descrição Geral
Neste conjunto de dados há informações sobre acidades que ocorreram no período dos anos de 2015 a 2022 na cidade do Recife, Pernambuco, Brasil.

## Fontes de dados
- **Título:**"Acidentes de Trânsito com Vítimas",
- **Descrição:**"Dados dos acidentes do trânsito de Recife, disponibilizados pela CTTU",
- **Categoria VCGE:** "http://vocab.e.gov.br/2011/03/vcge#transportes-transito",
- **Licença:** "Open Database License (ODbL)",
- **Responsável pelos dados:**"CTTU",
- **Responsável por dizponibilizar:**"Emprel",
- **Frequencia de atualização:**"Semestral",
- **Endereço do dataset:** [http://dados.recife.pe.gov.br/dataset/acidentes-de-transito-com-e-sem-vitimas],
- **Status:**"ativo",
- **Granularidade:**"Por Ano",
- **Etiquetas:**"acidente, acidentes, animal, bicicleta, caminhão,ônibus, ciclista, cttu, mobilidade, taxi, transito, trânsito,vitimas"

## Recursos
**Acidentes de transito em 2015**
- **Identificador:** ["http://dados.recife.pe.gov.br/dataset/acidentes-de-transito-com-e-sem-vitimas/resource/db610fdc-18fa-41a1-9b26-72038c56ffc8"],
- **Formato:** "csv",
- **Descrição:**"Acidentes de Trânsito com e sem vitimas do ano 2015"
#
**Acidentes de transito em 2018**
- **Identificador:**["http://dados.recife.pe.gov.br/dataset/44087d2d-73b5-4ab3-9bd8-78da7436eed1/resource/2485590a-3b35-4ad0-b955-8dfc36b61021"],
- **Formato:**"csv",
- **Descrição:**"Acidentes de Trânsito com e sem vitimas do ano 2018"

**Acidentes de transito em 2019**
- **Identificador:**["http://dados.recife.pe.gov.br/dataset/44087d2d-73b5-4ab3-9bd8-78da7436eed1/resource/3531bafe-d47d-415e-b154-a881081ac76c"],
- **Formato:**"csv",
- **Descrição:**"Acidentes de Trânsito com e sem vitimas do ano 2019"

**Acidentes de transito em 2020**
- **Identificador:**["http://dados.recife.pe.gov.br/dataset/44087d2d-73b5-4ab3-9bd8-78da7436eed1/resource/fc1c8460-0406-4fff-b51a-e79205d1f1ab"],
- **Formato:**"csv",
- **Descrição:**"Acidentes de Trânsito com e sem vitimas do ano 2020"

**Acidentes de transito em 2021**
- **Identificador:**["http://dados.recife.pe.gov.br/dataset/44087d2d-73b5-4ab3-9bd8-78da7436eed1/resource/2caa8f41-ccd9-4ea5-906d-f66017d6e107"],
- **Formato:**"csv",
- **Descrição:**"Acidentes de Trânsito com e sem vitimas do ano 2021"

**Acidentes de transito em 2022**
- **Identificador:**["http://dados.recife.pe.gov.br/dataset/44087d2d-73b5-4ab3-9bd8-78da7436eed1/resource/971e0228-fa9c-4a42-b360-c842b29d2f56"],
- **Formato:**"csv",
- **Descrição:**"Acidentes de Trânsito com e sem vitimas do ano 2022"

## Campos

**tipo**
- **Código:** tipo,
- **Descrição:** Tipo do Acidente se foi com ou sem vitimas,
- **Tipo:** Char,
- **Tamanho:** 100,


**situacao**
- **Código:** situacao,
- **Descrição:** Situação do atendimento,
- **Tipo:** Char,
- **Tamanho:** 50

**data**
- **Código:** data,
- **Descrição:** data do atendimento,
- **Tipo:** date,
- **Tamanho:** 10

**hora**
- **Código:** hora
- **Descrição:** hora do atendimento,
- **Tipo:** num,
- **Tamanho:** 20

**bairro**
- **Código:** bairro
- **Descrição:** Bairro do acidente,
- **Tipo:** Char,
- **Tamanho:** 50

**endereco**
- **Código:** endereco
- **Descrição:** Número do acidente,
- **Tipo:** num,
- **Tamanho:** 10

**complemento**
- **Código:** complemento
- **Descrição:** Complemento do acidente,
- **Tipo:** Char,
- **Tamanho:** 50

**natureza**
- **Código:** natureza
- **Descrição:** Tipo de Ocorrencia,
- **Tipo:** Char,
- **Tamanho:** 50

**descricao**
- **Código:** descricao
- **Descrição:** Descrição do acidente,
- **Tipo:** Char,
- **Tamanho:** 250

**auto**
- **Código:** auto
- **Descrição:** Quantidade de automoveis no acidente,
- **Tipo:** Num,
- **Tamanho:** 20

**moto**
- **Código:** moto
- **Descrição:** Quantidade de motos no acidente,
- **Tipo:** Num,
- **Tamanho:** 20

**ciclom**
- **Código:** ciclom
- **Descrição:** Quantidade de ciclomotor no acidente,
- **Tipo:** Num,
- **Tamanho:** 20

**ciclista**
- **Código:** ciclista
- **Descrição:** Quantidade de bicicleta no acidente,
- **Tipo:** Num,
- **Tamanho:** 20
  

**pedestre**
- **Código:** pedestre
- **Descrição:** Quantidade de pedestres no acidente,
- **Tipo:** Num,
- **Tamanho:** 20
  
  
**onibus**
- **Código:** onibus
- **Descrição:** Quantidade de onibus no acidente,
- **Tipo:** Num,
- **Tamanho:** 20
  
  
**caminhao**
- **Código:** caminhao
- **Descrição:** Quantidade de caminhão no acidente,
- **Tipo:** Num,
- **Tamanho:** 20
  
  
**viatura**
- **Código:** viatura
- **Descrição:** Quantidade de viaturas no acidente,
- **Tipo:** Num,
- **Tamanho:** 20
  
  
**outros**
- **Código:** outros
- **Descrição:** Quantidade de outros veiculos no acidente,
- **Tipo:** Num,
- **Tamanho:** 20
  
  
**vitimas**
- **Código:** vitimas
- **Descrição:** Quantidade de vitimas no acidente. A partir de 2017 essa coluna contém apenas as vítimas não fatais,
- **Tipo:** Char,
- **Tamanho:** 3
  
      
**vitimas fatais**
- **Código:** vitimasfatais
- **Descrição:** Quantidade de vitimas fatais no acidente,
- **Tipo:** Num,
- **Tamanho:** 3
  
## Unidades de medida

- As datas estão no formato 'YYYY-MM-DD'
- As horas estão no formato 'HH:MM'