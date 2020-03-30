# Analytics para Dados de COVID19 no Brasil

Análise do surto de COVID19 no Brasil empregando-se principalmente modelos epidemiológicos e de processos hospitalares.


## Introdução

A recente pandemia de COVID-19 vem motivando uma série de iniciativas ao redor do mundo para entender sua dinâmica e facilitar o trabalho de profissionais e gestores de saúde, no âmbito tanto público quanto privado. Aqui apresentamos uma contribuição por meio da implementação de análises, modelos epidemiológicos, estudos de processos de saúde e outros exercícios variados na linguagem Python, com o objetivo de permitir a cientistas de dados, principalmente no Brasil, a terem um ponto de partida a partir do qual conduzirem seus próprios estudos. Na medida do possível, buscaremos também exercitar esses modelos para produzir alguns resultados numéricos sugestivos, **porém por enquanto é preciso advertir que esses números não são afirmações formais sobre o progresso da doença, mas apenas exercício que demosntram o uso dos modelos propostos.**

O repositório está organizado nas seguintes pastas:

  - `data/`: Dados históricos da COVID19, usado para estimação de parâmetros dos modelos.
  - `notebooks/`: *Notebooks* Jupyter com as análises e modelos.
  - `results/`: Resultados de modelos, para reuso em outros contextos.


## Modelos Epidemiológicos

Estão implementados alguns [modelos epidemiológicos clássicos](https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology), a saber:

  - SIR: ver *notebook* `epidemic_model_sir.ipynb`. Este é um modelo simples que usamos apenas para demonstrar as técnicas básicas envolvidas.
  - SEIR: ver *notebook* `epidemic_model_seir.ipynb`. Este modelo é uma sofisticação do SEIR. Ademais, focamos melhorias e análises nele.

Esses *notebooks* podem ser baixados por interessados e customizados de diversos modos. No próprio texto de cada um apresentamos algumas idéias e exercícios, que podem servir de base para estudos e modelos mais complexos.



## Modelos de Processos Hospitalares

Além da epidemia em si, é útil compreender como o sistema de saúde se comporta frente aos números projetados de infecções. Para tanto, também implementamos um modelo de processos hospitalares no *notebook* `hospitalization_process.ipynb`.