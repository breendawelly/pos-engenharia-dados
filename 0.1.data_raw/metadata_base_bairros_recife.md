

  "metadados": {
    "cabecalho": {
      "titulo": "Área urbana",
      "descricao": "Este conjunto descreve dados sobre a área espacial da cidade do Recife, incluindo dados sobre divisões do espaço físico da cidade",
      "categoria_vcge": "http://vocab.e.gov.br/2011/03/vcge#governo-municipal",
      "fonte_dados": "http://dados.recife.pe.gov.br",
      "licenca": "Open Database License (ODbL)",
      "responsavel_dados": "Secretaria de Infraestrutura e Serviços Urbanos",
      "responsavel_disponibilizar": "EMPREL",
      "frequencia_atualizacao": "Anual",
      "endereco_dataset": "http://dados.recife.pe.gov.br/dataset/area-urbana",
      "status": "ativo",
      "endereco_dataset_substituto": "",
      "granularidade": "Dados sobre as áreas urbanas",
      "etiquetas": "Bairro, face de quadra, quadra, lote, parques, praças, área verde"
    },
    "recursos": [
      {
        "identificador": "http://dados.recife.pe.gov.br/dataset/area-urbana/resource/e43bee60-9448-4d3d-92ff-2378bc3b5b00",
        "titulo": "Bairros do Recife",
        "formato": "csv",
        "descricao": "Identifica os bairros do Recife, com a localização geográfica e a associação com a RPA (Região Político Administrativa) e a Microregião onde o bairro está inserido"
      }
    ],
    "campos": [
      {
        "codigo": "bairro_codigo",
        "descricao": "Código do bairro",
        "tipo": "Num",
        "tamanho": 9,
        "valores_permitidos": ""
      },
      {
        "codigo": "bairro_nome_ca",
        "descricao": "Bairro da cidade do recife",
        "tipo": "Char",
        "tamanho": 100,
        "valores_permitidos": ""
      },
      {
        "codigo": "rpa",
        "descricao": "Região Politico Administrativa",
        "tipo": "Num",
        "tamanho": 1,
        "valores_permitidos": ""
      },
      {
        "codigo": "microrregiao",
        "descricao": "Subdivisão de Região Político-Administrativa (Microrregião)",
        "tipo": "Num",
        "tamanho": 1,
        "valores_permitidos": ""
      },
      {
        "codigo": "bairro_nome",
        "descricao": "Nome do Bairro Oficial",
        "tipo": "Num",
        "tamanho": 21,
        "valores_permitidos": ""
      },
      {
        "codigo": "geometry",
        "descricao": "Dados Geométricos do bairro",
        "tipo": "Json",
        "tamanho": null,
        "valores_permitidos": ""
      }
    ]
  }
}

