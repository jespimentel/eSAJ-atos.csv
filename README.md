# eSAJ-atos.csv
#Análises dos dados de "Consulta de intimações recebidas" a partir do arquivo "atos.csv"

O portal e-SAJ, desenvolvido pela Softplan, é usado por membros do Ministério Público e Defensoria Pública como interface para o processo eletrônico.

A aplicação possui funcionalidades para atender ao art. 5º da Lei nº 11.419/06, relativas à intimação dos usuários membros dos órgãos auxiliares da Justiça.

Nas subdivisões da área de "Intimações on line" ("Consulta de intimações recebidas" e "Recebimento de intimações eletrônicas") é possível exportar em arquivo "csv" ("atos.csv") a relação dos atos disponibilizados, de acordo com os filtros e período selecionados.

O script está preparado para analisar exclusivamente os dados de "Consulta de intimações recebidas" a partir do arquivo "atos.csv" baixado do e-SAJ e movido para o mesmo diretório do Jupyter Notebook (arquivo "eSAJ.ipynb").

Aplicando métodos da biblioteca Pandas (do Python), retorna informações agrupadas por Vara, Cargo, Especialização, etc., relativas aos feitos recebidos na localidade ("Foro"), com suas respectivas visualizações gráficas.

A rotina também gera um sumário.

O relatório e os gráficos são exportados nos formatos "txt" e "jpg", respectivamente, e salvos no diretório de trabalho.
