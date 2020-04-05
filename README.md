# Análise da COVID19 no Brasil

Análise do surto de COVID19 no Brasil empregando-se principalmente modelos epidemiológicos e de processos hospitalares.

**ADVERTÊNCIA:** os modelos e números aqui apresentados não são afirmações formais médicas sobre o progresso da doença, mas apenas exercícios que demonstram técnicas de modelagem e cenários hipotéticos de aplicação.

## Introdução

A recente pandemia de COVID-19 vem motivando uma série de iniciativas ao redor do mundo para entender sua dinâmica e facilitar o trabalho de profissionais e gestores de saúde, no âmbito tanto público quanto privado. Aqui apresentamos uma contribuição por meio da implementação de análises, modelos epidemiológicos, estudos de processos de saúde e outros exercícios variados na linguagem Python, com o objetivo de *permitir a cientistas de dados, principalmente no Brasil, a terem um ponto de partida a partir do qual conduzirem seus próprios estudos*. Na medida do possível, buscaremos também exercitar esses modelos para produzir alguns resultados numéricos sugestivos, **porém por enquanto é preciso advertir que esses números não são afirmações formais sobre o progresso da doença, mas apenas exercício que demosntram o uso dos modelos propostos. Pequenas mudanças nos parâmetros dos modelos podem levar a vastas mudanças nos resultados.**

O repositório está organizado nas seguintes pastas:

  - `data/`: Dados históricos da COVID19, usado para estimação de parâmetros dos modelos.
  - `notebooks/`: *Notebooks* Jupyter com as análises e modelos.
  - `results/`: Resultados de análises e modelos, para reuso em outros contextos.
    - `results/eda/`: Imagens e CSVs resultantes das análises exploratórias de dados.
    - `results/notebooks/`: Com o uso da biblioteca [papermill](https://papermill.readthedocs.io/en/latest/index.html), os próprios *notebooks* podem ser customizados resultarem em novas versões, que são então nesta pasta.


## Modelos Epidemiológicos

Estão implementados alguns [modelos epidemiológicos clássicos](https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology), a saber:

  - SIR (Susceptible-Infectious-Recovered): ver *notebook* `epidemic_model_sir.ipynb`. Este é um modelo simples que usamos apenas para demonstrar as técnicas básicas envolvidas.
  - SEIR (Susceptible-Exposed-Infectious-Recovered): ver *notebook* `epidemic_model_seir.ipynb`. Este modelo é uma sofisticação do SIR. Ademais, focamos melhorias e análises nele.

Esses *notebooks* podem ser baixados por interessados e customizados de diversos modos. No próprio texto de cada um apresentamos algumas idéias e exercícios, que podem servir de base para estudos e modelos mais complexos.

Ademais, fornecemos um *notebook*  central, `models.ipynb`, por meio do qual os mesmos modelos podem ser re-executados com diversas variações de parâmetros, mediante o uso da biblioteca [papermill](https://papermill.readthedocs.io/en/latest/index.html).


![Exemplo de saida do SEIR](https://raw.githubusercontent.com/funcional-health-analytics/covid19-analytics/master/seir_output_example.png)
*Exemplo de saída em um dos exercícios com o modelo SEIR. Os números são meramente ilustrativos.*

## Modelos de Processos Hospitalares

Além da epidemia em si, é útil compreender como o sistema de saúde se comporta frente aos números projetados de infecções. Para tanto, também implementamos um modelo de processos hospitalares no *notebook* `hospitalization_process.ipynb`.


![Exemplo de saida do modelo de processos hospitalares](https://raw.githubusercontent.com/funcional-health-analytics/covid19-analytics/master/hospitalization_process_example.png)
*Exemplo de saída em um dos exercícios com o modelo de processos hospitalares. Os números são meramente ilustrativos.*

## Análises de Dados Exploratórias

Fazemos algumas análises em dados disponíveis publicamente, notoriamente os do [Our World in Data](https://ourworldindata.org/coronavirus-source-data ). Temos os seguintes *notebooks* disponíveis:

  - `eda.ipynb`: Centraliza a execução de outros *notebooks* com parâmetros customizados, mediante o uso da biblioteca [papermill](https://papermill.readthedocs.io/en/latest/index.html). Assim, uma mesma análise pode ser re-executada com diversas variações de parâmetros. Os resultados dessas análises customizadas são também *notebooks*, que são colocados em `results/notebooks/`.
  - `eda_international.ipynb`: Análises comparativas variadas do progresso da detecção de casos e óbitos ao redor do mundo. Esta análise gera diversos gráficos e dados comparativos, que são armazenados na pasta `results/` para conveniência.
 
![Razão óbitos por casos](https://raw.githubusercontent.com/funcional-health-analytics/covid19-analytics/master/results/eda/eda_deaths_per_cases_ratio_ordered_by_total_cases.png)
*Exemplo de análise exploratória. Números baseados em dados públicos.*
