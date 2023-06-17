# -*- coding: utf-8 -*-
#%% Importações

import pandas as pd
import matplotlib.pyplot as plt

#%% Configurações do usuário

arquivo_atos = 'atos.csv'
nome_arquivo = 'estatisticas_cargos_pira.csv'
nome_arquivo_1 = 'assuntos_11_pj.csv'
sel_cargo = '011º PROMOTOR DE JUSTIÇA'
periodo = ['2022-01', '2023-05']

#%% Leitura do dataset

atos = pd.read_csv (arquivo_atos, sep = ';', encoding='ISO-8859-1', on_bad_lines='skip', \
                    low_memory = False, parse_dates=['Disponibilização', 'Data da intimação'], dayfirst=True)

#%% Delimitação do período de análise

atos['mês_ano'] = pd.to_datetime(atos['Disponibilização']).dt.to_period('M')

criterio = (atos['mês_ano'] >= periodo[0])&(atos['mês_ano'] <= periodo[1])
atos = atos[criterio]
 
#%% Estatística dos cargos

estatistica_cargos = atos.groupby(['mês_ano','Cargo'])['Número do processo'].describe()

#%% Interações no período

interacoes = atos.groupby('mês_ano')['Número do processo'].count()
interacoes_proc_dist = atos.groupby('mês_ano')['Número do processo'].nunique()

#%% Plotagem

x = interacoes.index.strftime('%Y-%m').tolist()
width = 0.35

plt.figure(figsize=(20, 12))
fig, ax = plt.subplots()
rects1 = ax.bar(x, interacoes, width, label='total de interações')
rects2 = ax.bar(x, interacoes_proc_dist, width, label='processos distintos')

# Configurações adicionais
ax.set_xlabel('Meses')
ax.set_ylabel('Número')
ax.set_title('Interações no eSAJ - Foro')
ax.set_xticks(x)
ax.set_xticklabels(x, rotation=90, ha='center')
ax.legend(loc='lower right')

plt.grid(True)
plt.show()

#%% Cargo Específico

criterio = (atos['Cargo'] == sel_cargo)
atos_pj = atos[criterio]

#%% Interações no período

total_pj = atos_pj.groupby('mês_ano')['Número do processo'].count()

#%% Plotagem

total_pj.plot.bar()
plt.title(f'{sel_cargo}: interações no e-SAJ')
plt.show()

#%% Contagem de assuntos

contagem_de_assuntos_pj = atos_pj.groupby(['mês_ano','Assunto principal'])['Número do processo'].nunique()

#%% Gravação dos resultados em arquivos csv

estatistica_cargos.to_csv(nome_arquivo)
contagem_de_assuntos_pj.to_csv(nome_arquivo_1)
