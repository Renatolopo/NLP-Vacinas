# NLP-Vacinas

![NLP-Vacinas](https://www.camara.leg.br/midias/image/2021/06/img20201022140139807-768x512.jpg

Este repositório contém os scripts e arquivos necessários para o projeto de monitoramento e análise de notícias sobre vacinas. O projeto envolve a coleta, análise e visualização de dados, utilizando diversas técnicas de ciência de dados e aprendizado de máquina.

## Estrutura do Repositório

- **data/**: Contém os modelos salvos em formato `.pkl`. Estes modelos são o resultado do treinamento de algoritmos de aprendizado de máquina e são utilizados para fazer previsões e análises nos dados coletados.
- **img/**: Contém os gráficos dos resultados gerados em formato de imagem. Estes gráficos ajudam a visualizar os insights obtidos a partir dos dados analisados.
- **src/**: Contém todos os scripts utilizados no projeto. Cada script tem uma função específica e é executado separadamente.
  - **Classificacao_dados.ipynb**: Script que realiza a classificação dos dados. Este notebook aplica algoritmos de classificação para categorizar os dados de acordo com diferentes critérios.
  - **analise_de_sentimento.ipynb**: Script onde é feito o modelo de análise de sentimento. Este notebook treina e aplica modelos de análise de sentimento para determinar a polaridade (positiva, negativa ou neutra) dos textos analisados.
  - **analise_exploratoria.ipynb**: Realiza a análise exploratória dos dados. Este notebook investiga os dados para identificar padrões, tendências e possíveis anomalias.
  - **conect_db.py**: Faz a conexão com o banco de dados. Este script estabelece a conexão com o banco de dados onde os dados são armazenados.
  - **data_preprocessing.py**: Executa o pré-processamento dos dados. Este script limpa e prepara os dados para serem utilizados nos modelos de análise.
  - **data_view.ipynb**: Visualização dos dados. Este notebook cria visualizações gráficas para facilitar a interpretação dos dados analisados.
  - **db_to_csv.py**: Exporta arquivos do banco de dados para CSV. Este script extrai os dados do banco e os salva em arquivos CSV para facilitar a manipulação e análise.
  - **deploy.py**: Aplica o modelo de análise de sentimento nos dados do Twitter. Este script implementa o modelo treinado para analisar novos dados coletados do Twitter.
  - **filter_paginas.ipynb**: Script para filtrar os dados, ajustado de acordo com a necessidade. Este notebook permite filtrar os dados para focar em informações específicas.
  - **query.ipynb**: Contém algumas consultas feitas nos dados. Este notebook realiza consultas no banco de dados para extrair informações relevantes.
  - **requirements.txt**: Lista as bibliotecas usadas no projeto. Este arquivo especifica todas as dependências necessárias para rodar os scripts.
  - **selecao_de_modelo.ipynb**: Compara qual modelo funciona melhor para o projeto. Este notebook avalia diferentes modelos de aprendizado de máquina para determinar o mais eficaz.

## Executando o Projeto

Cada script/notebook é rodado separadamente. Não é possível executar o projeto sem acesso aos dados, mas os scripts usados no projeto estão disponíveis aqui para referência e utilização.

## Requisitos

Para executar os scripts, você precisará instalar as bibliotecas listadas no arquivo `requirements.txt`. Você pode fazer isso utilizando o comando:

```bash
pip install -r requirements.txt
