# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 13:34:28 2023

@author: Nevermore
"""

import matplotlib.pyplot as plt
import seaborn as sns
from functions_and_variables import dpf_all_years

# plotting the spending for each designated 'function' by year
plt.figure(figsize=(64,128))
ax_log_dpf = sns.barplot(data=dpf_all_years,x="Liquidado",y="Função",hue="Ano",
                         palette="Spectral")
ax_log_dpf.axes.set_title("Despesas por Função",fontsize=18) # title
ax_log_dpf.set_xlabel("Valor Liquidado",fontsize=16) # x axis label
ax_log_dpf.set_ylabel("Função",fontsize=16) # y axis label
ax_log_dpf.tick_params(labelsize=20)
ax_log_dpf.set_xscale("log") # setting to log scale for better visualization
plt.show()


function_list = ["EDUCAÇÃO","ADMINISTRAÇÃO","SAÚDE","PREVIDÊNCIA SOCIAL",
                 "URBANISMO","TRANSPORTE","ENCARGOS ESPECIAIS","LEGISLATIVA",
                 "ASSISTÊNCIA SOCIAL","SEGURANÇA PÚBLICA","AGRICULTURA",
                 "CULTURA","ENERGIA","DESPORTO E LAZER","COMÉRCIO E SERVIÇOS",
                 "CIÊNCIA E TECNOLOGIA","TRABALHO","GESTÃO AMBIENTAL",
                 "DIREITOS DA CIDADANIA","SANEAMENTO","HABITAÇÃO","JUDICIÁRIA",
                 "COMUNICAÇÕES","ESSENCIAL À JUSTIÇA","INDÚSTRIA"]

# Education, Administration, Health, Social Previdence, Urbanism
dpf_all_findex = dpf_all_years.set_index("Função")
dpf_top5 = dpf_all_findex.loc[function_list[0:5]].reset_index()

plt.figure(figsize=(25,40))
ax_log1 = sns.barplot(data=dpf_top5,x="Liquidado",y="Função",hue="Ano",
                      palette="Spectral")
ax_log1.axes.set_title("Despesas por Função",fontsize=18) # title
ax_log1.set_xlabel("Valor Liquidado",fontsize=16) # x axis label
ax_log1.set_ylabel("Função",fontsize=16) # y axis label
ax_log1.tick_params(labelsize=20)
ax_log1.set_xscale("log") # setting to log scale for better visualization
ax_log1.set_xlim(left=1.0e3,right=7.0e9)
plt.show()

# next 5
dpf_all_findex = dpf_all_years.set_index("Função")
dpf_5to10 = dpf_all_findex.loc[function_list[5:10]].reset_index()

plt.figure(figsize=(25,40))
ax_log2 = sns.barplot(data=dpf_5to10,x="Liquidado",y="Função",hue="Ano",
                      palette="Spectral")
ax_log2.axes.set_title("Despesas por Função",fontsize=18) # title
ax_log2.set_xlabel("Valor Liquidado",fontsize=16) # x axis label
ax_log2.set_ylabel("Função",fontsize=16) # y axis label
ax_log2.tick_params(labelsize=20)
ax_log2.set_xscale("log") # setting to log scale for better visualization
ax_log2.set_xlim(left=1.0e3,right=7.0e9)
plt.show()

# next 5
dpf_all_findex = dpf_all_years.set_index("Função")
dpf_10to15 = dpf_all_findex.loc[function_list[10:15]].reset_index()

plt.figure(figsize=(25,40))
ax_log3 = sns.barplot(data=dpf_10to15,x="Liquidado",y="Função",hue="Ano",
                      palette="Spectral")
ax_log3.axes.set_title("Despesas por Função",fontsize=18) # title
ax_log3.set_xlabel("Valor Liquidado",fontsize=16) # x axis label
ax_log3.set_ylabel("Função",fontsize=16) # y axis label
ax_log3.tick_params(labelsize=20)
ax_log3.set_xscale("log") # setting to log scale for better visualization
ax_log3.set_xlim(left=1.0e3,right=7.0e9)
plt.show()

# next 5
dpf_all_findex = dpf_all_years.set_index("Função")
dpf_15to20 = dpf_all_findex.loc[function_list[15:20]].reset_index()

plt.figure(figsize=(25,40))
ax_log4 = sns.barplot(data=dpf_15to20,x="Liquidado",y="Função",hue="Ano",
                      palette="Spectral")
ax_log4.axes.set_title("Despesas por Função",fontsize=18) # title
ax_log4.set_xlabel("Valor Liquidado",fontsize=16) # x axis label
ax_log4.set_ylabel("Função",fontsize=16) # y axis label
ax_log4.tick_params(labelsize=20)
ax_log4.set_xscale("log") # setting to log scale for better visualization
ax_log4.set_xlim(left=1.0e3,right=7.0e9)
plt.show()

# next 5
dpf_all_findex = dpf_all_years.set_index("Função")
dpf_20to25 = dpf_all_findex.loc[function_list[20:25]].reset_index()

plt.figure(figsize=(25,40))
ax_log5 = sns.barplot(data=dpf_20to25,x="Liquidado",y="Função",hue="Ano",
                      palette="Spectral")
ax_log5.axes.set_title("Despesas por Função",fontsize=18) # title
ax_log5.set_xlabel("Valor Liquidado",fontsize=16) # x axis label
ax_log5.set_ylabel("Função",fontsize=16) # y axis label
ax_log5.tick_params(labelsize=20)
ax_log5.set_xscale("log") # setting to log scale for better visualization
ax_log5.set_xlim(left=1.0e3,right=7.0e9)
plt.show()