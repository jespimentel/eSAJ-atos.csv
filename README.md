# eSAJ-atos.csv
Análises a partir do arquivo "atos.csv" exportado pelo e-SAJ

O portal e-SAJ, desenvolvido pela Softplan, é usado por membros do Ministério Público e Defensoria Pública como interface para o processo eletrônico.

A aplicação possui funcionalidades para atender ao art. 5º da Lei nº 11.419/06, relativas à intimação dos usuários membros dos órgãos auxiliares da Justiça.

Nas subdivisões da área de "Intimações on line", a saber, "Consulta de intimações recebidas" e "Recebimento de intimações eletrônicas", é possível exportar em arquivo "csv" ("atos.csv") a relação dos atos disponibilizados, de acordo com os filtros e período selecionados.

O script contido no presente Jupyter Notebook lê o arquivo "atos.csv" baixado do e-SAJ e movido para o mesmo diretório do JN (arquivo "eSAJ.ipynb") e, aplicando métodos da biblioteca Pandas (do Python), retorna algumas análises da área do e-SAJ selecionada, com suas respectivas visualizações gráficas.

A rotina também gera um sumário das informações obtidas.

O relatório e os gráficos são exportados nos formatos "txt" e "jpg", respectivamente, e salvos no diretório de trabalho.
