# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 14:44:44 2023

@author: Nevermore
"""

import pandas as pd
import seaborn as sns

# importing the data for 2009
despesas_2009 = pd.read_csv("Despesa_Principal_2009.csv", sep=";")

# removing unnecessary columns
columns_list = ["EXERCÍCIO","CÓDIGO UG","CÓDIGO GESTÃO","CNPJ CPF DO CREDOR",
                "CÓDIGO FONTE DE RECURSOS","CÓDIGO ESFERA","CÓDIGO FUNÇÃO",
                "CÓDIGO SUBFUNÇÃO","CÓDIGO PROGRAMA","CÓDIGO AÇÃO",
                "CÓDIGO SUBTÍTULO","CÓDIGO CATEGORIA ECONÔMICA",
                "CÓDIGO MODALIDADE DE APLICAÇÃO",
                "CÓDIGO GRUPO DE NATUREZA DESPESA",
                "CÓDIGO ELEMENTO DESPESA","CÓDIGO PROGRAMA DE TRABALHO",
                "CÓDIGO TIPO DESPESA","PROCESSO"]

for i in columns_list:
    despesas_2009 = despesas_2009.drop(i, axis=1)
    
def extra_columns(data,year,governor):
    """
    Creates 3 additional columns for a given DataFrame type object.

    Parameters
    ----------
    data : DataFrame object to which the columns will be added.
    year : year that will be added to all rows.
    governor : name of the governor of the Federal District of Brazil for the
    specified year.

    Returns
    -------
    data : DataFrame object with the addition of the 3 columns.

    """
    years = [] # empty list that will be turned into the first column
    name = [] # empty list that will be turned into the second column
    elections = [] # empty list that will be turned into the third column
    for i in range(0,len(data)):
        years.append(year) # appends the year used as argument to first list
        name.append(governor) # appends governor name to the second list
        if year in [2010,2014,2018,2022]: # if the year was an election year,
            elections.append(True) # this will append True to the third list
        else:
            elections.append(False) # or False if it wasn't.
    data["Ano"] = years # adds the first column to the DataFrame
    data["Governador"] = name # adds the second column to the DataFrame
    data["Ano Eleitoral"] = elections # adds the third column to the DataFrame
    return data

# grouping by desired column
dpf_2009 = despesas_2009.groupby("FUNÇÃO",
                                 as_index=False).sum(numeric_only=True)
# organizing by monetary value
dpf_2009 = dpf_2009.sort_values(by="LIQUIDADO",ascending=False,
                                ignore_index=True)

# adding three extra columns
dpf_2009 = extra_columns(dpf_2009,2009,"José Roberto Arruda")

# repeating the process for other years
# 2010
despesas_2010 = pd.read_csv("Despesa_Principal_2010.csv",sep=";",
                            dtype={"CNPJ CPF DO CREDOR":str})

for i in columns_list:
    despesas_2010 = despesas_2010.drop(i, axis=1)

dpf_2010 = despesas_2010.groupby("FUNÇÃO",
                                 as_index=False).sum(numeric_only=True)
dpf_2010 = dpf_2010.sort_values(by="LIQUIDADO",ascending=False,
                                ignore_index=True)
dpf_2010 = extra_columns(dpf_2010,2010,"José Roberto Arruda")

# 2011
despesas_2011 = pd.read_csv("Despesa_Principal_2011.csv",sep=";")

for i in columns_list:
    despesas_2011 = despesas_2011.drop(i, axis=1)

dpf_2011 = despesas_2011.groupby("FUNÇÃO",
                                 as_index=False).sum(numeric_only=True)
dpf_2011 = dpf_2011.sort_values(by="LIQUIDADO",ascending=False,
                                ignore_index=True)
dpf_2011 = extra_columns(dpf_2011,2011,"Agnelo Queiroz")

# 2012
despesas_2012 = pd.read_csv("Despesa_Principal_2012.csv",sep=";")

for i in columns_list:
    despesas_2012 = despesas_2012.drop(i, axis=1)

dpf_2012 = despesas_2012.groupby("FUNÇÃO",
                                 as_index=False).sum(numeric_only=True)
dpf_2012 = dpf_2012.sort_values(by="LIQUIDADO",ascending=False,
                                ignore_index=True)
dpf_2012 = extra_columns(dpf_2012,2012,"Agnelo Queiroz")

# 2013
despesas_2013 = pd.read_csv("Despesa_Principal_2013.csv",sep=";")

for i in columns_list:
    despesas_2013 = despesas_2013.drop(i, axis=1)

dpf_2013 = despesas_2013.groupby("FUNÇÃO",
                                 as_index=False).sum(numeric_only=True)
dpf_2013 = dpf_2013.sort_values(by="LIQUIDADO",ascending=False,
                                ignore_index=True)
dpf_2013 = extra_columns(dpf_2013,2013,"Agnelo Queiroz")

# 2014
despesas_2014 = pd.read_csv("Despesa_Principal_2014.csv",sep=";")

for i in columns_list:
    despesas_2014 = despesas_2014.drop(i, axis=1)

dpf_2014 = despesas_2014.groupby("FUNÇÃO",
                                 as_index=False).sum(numeric_only=True)
dpf_2014 = dpf_2014.sort_values(by="LIQUIDADO",ascending=False,
                                ignore_index=True)
dpf_2014 = extra_columns(dpf_2014,2014,"Agnelo Queiroz")

# 2015
despesas_2015 = pd.read_csv("Despesa_Principal_2015.csv",sep=";")

for i in columns_list:
    despesas_2015 = despesas_2015.drop(i, axis=1)

dpf_2015 = despesas_2015.groupby("FUNÇÃO",
                                 as_index=False).sum(numeric_only=True)
dpf_2015 = dpf_2015.sort_values(by="LIQUIDADO",ascending=False,
                                ignore_index=True)
dpf_2015 = extra_columns(dpf_2015,2015,"Rodrigo Rollemberg")

# 2016
despesas_2016 = pd.read_csv("Despesa_Principal_2016.csv",sep=";")

for i in columns_list:
    despesas_2016 = despesas_2016.drop(i, axis=1)

dpf_2016 = despesas_2016.groupby("FUNÇÃO",
                                 as_index=False).sum(numeric_only=True)
dpf_2016 = dpf_2016.sort_values(by="LIQUIDADO",ascending=False,
                                ignore_index=True)
dpf_2016 = extra_columns(dpf_2016,2016,"Rodrigo Rollemberg")

# 2017
despesas_2017 = pd.read_csv("Despesa_Principal_2017.csv",sep=";")

for i in columns_list:
    despesas_2017 = despesas_2017.drop(i, axis=1)

dpf_2017 = despesas_2017.groupby("FUNÇÃO",
                                 as_index=False).sum(numeric_only=True)
dpf_2017 = dpf_2017.sort_values(by="LIQUIDADO",ascending=False,
                                ignore_index=True)
dpf_2017 = extra_columns(dpf_2017,2017,"Rodrigo Rollemberg")

# 2018
despesas_2018 = pd.read_csv("Despesa_Principal_2018.csv",sep=";")

for i in columns_list:
    despesas_2018 = despesas_2018.drop(i, axis=1)

dpf_2018 = despesas_2018.groupby("FUNÇÃO",
                                 as_index=False).sum(numeric_only=True)
dpf_2018 = dpf_2018.sort_values(by="LIQUIDADO",ascending=False,
                                ignore_index=True)
dpf_2018 = extra_columns(dpf_2018,2018,"Rodrigo Rollemberg")

# 2019
despesas_2019 = pd.read_csv("Despesa_Principal_2019.csv",sep=";")

for i in columns_list:
    despesas_2019 = despesas_2019.drop(i, axis=1)

dpf_2019 = despesas_2019.groupby("FUNÇÃO",
                                 as_index=False).sum(numeric_only=True)
dpf_2019 = dpf_2019.sort_values(by="LIQUIDADO",ascending=False,
                                ignore_index=True)
dpf_2019 = extra_columns(dpf_2019,2019,"Ibaneis Rocha")

# 2020
despesas_2020 = pd.read_csv("Despesa_Principal_2020.csv",sep=";")

for i in columns_list:
    despesas_2020 = despesas_2020.drop(i, axis=1)

dpf_2020 = despesas_2020.groupby("FUNÇÃO",
                                 as_index=False).sum(numeric_only=True)
dpf_2020 = dpf_2020.sort_values(by="LIQUIDADO",ascending=False,
                                ignore_index=True)
dpf_2020 = extra_columns(dpf_2020,2020,"Ibaneis Rocha")

# 2021
despesas_2021 = pd.read_csv("Despesa_Principal_2021.csv",sep=";")

for i in columns_list:
    despesas_2021 = despesas_2021.drop(i, axis=1)

dpf_2021 = despesas_2021.groupby("FUNÇÃO",
                                 as_index=False).sum(numeric_only=True)
dpf_2021 = dpf_2021.sort_values(by="LIQUIDADO",ascending=False,
                                ignore_index=True)
dpf_2021 = extra_columns(dpf_2021,2021,"Ibaneis Rocha")

# 2022
despesas_2022 = pd.read_csv("Despesa_Principal_2022.csv",sep=";")

for i in columns_list:
    despesas_2022 = despesas_2022.drop(i, axis=1)

dpf_2022 = despesas_2022.groupby("FUNÇÃO",
                                 as_index=False).sum(numeric_only=True)
dpf_2022 = dpf_2022.sort_values(by="LIQUIDADO",ascending=False,
                                ignore_index=True)
dpf_2022 = extra_columns(dpf_2022,2022,"Ibaneis Rocha")

# 2023
# despesas_2023 = pd.read_csv("Despesa_Principal_2023.csv",sep=";")
#
# for i in columns_list:
#     despesas_2023 = despesas_2023.drop(i, axis=1)
#
# dpf_2023 = despesas_2023.groupby("FUNÇÃO",
#                                  as_index=False).sum(numeric_only=True)
# dpf_2023 = dpf_2023.sort_values(by="LIQUIDADO",ascending=False,
#                                 ignore_index=True)
# dpf_2023 = extra_columns(dpf_2023,2023,"Ibaneis Rocha")

# putting all the created DataFrames together into a list
dpf_list = [dpf_2009,dpf_2010,dpf_2011,dpf_2012,
            dpf_2013,dpf_2014,dpf_2015,dpf_2016,
            dpf_2017,dpf_2018,dpf_2019,dpf_2020,
            dpf_2021, dpf_2022]

# concatenating to create a DataFrame contemplating all years
dpf_all_years = pd.concat(dpf_list, ignore_index=True)

# creating a correlation matrix
corr_matrix_dpf = dpf_all_years.corr(numeric_only=True)
# heatmap of the correlation matrix
# dpf_corr_hm = sns.heatmap(corr_matrix_dpf, cmap="magma", annot=True)

# plotting the spending for each designated 'function' by year
# plt.figure(figsize=(25,80))
# ax_log_dpf = sns.barplot(data=dpf_all_years,x="LIQUIDADO",y="FUNÇÃO",
#                          hue="Ano", palette="Spectral")
# ax_log_dpf.axes.set_title("Despesas por FUNÇÃO",fontsize=18) # title
# ax_log_dpf.set_xlabel("Valor LIQUIDADO",fontsize=16) # x axis label
# ax_log_dpf.set_ylabel("FUNÇÃO",fontsize=16) # y axis label
# ax_log_dpf.tick_params(labelsize=20)
# ax_log_dpf.set_xscale("log") # setting to log scale for better visualization
# plt.show()

# plotting the spending for each designated 'function' in 2020
# plt.figure(figsize=(20,15))
# ax_log_2020 = sns.barplot(dpf_2020,x="LIQUIDADO",y="FUNÇÃO",
#                           palette="magma_r")
# ax_log_2020.axes.set_title("Despesas por FUNÇÃO - 2020",fontsize=18) # title
# ax_log_2020.set_xlabel("Valor LIQUIDADO",fontsize=16) # x axis label
# ax_log_2020.set_ylabel("FUNÇÃO",fontsize=16) # y axis label
# ax_log_2020.tick_params(labelsize=12)
# ax_log_2020.set_xscale("log") # setting to log scale for better visualization
# plt.show()

# turning DataFrame to series for plotting percentages onto a pie chart
dpf_2020_series = pd.Series(data=list(dpf_2020["LIQUIDADO"]),
                            index=list(dpf_2020["FUNÇÃO"]))
colors = sns.color_palette("icefire_r",n_colors=25) # selecting color palette
# plt.pie(dpf_2020_series,labels=dpf_2020_series.index,colors=colors,
#         autopct="%1.2f%%") # bad visualization of lower values
# plt.show()

# adding 3 extra columns for each DataFrame &
# creating DataFrames for each year only for the Transportation 'function'
despesas_2009 = extra_columns(despesas_2009, 2009, "José Roberto Arruda")
despesas_2010 = extra_columns(despesas_2010, 2010, "José Roberto Arruda")
despesas_2011 = extra_columns(despesas_2011, 2011, "Agnelo Queiroz")
despesas_2012 = extra_columns(despesas_2012, 2012, "Agnelo Queiroz")
despesas_2013 = extra_columns(despesas_2013, 2013, "Agnelo Queiroz")
despesas_2014 = extra_columns(despesas_2014, 2014, "Agnelo Queiroz")
despesas_2015 = extra_columns(despesas_2015, 2015, "Rodrigo Rollemberg")
despesas_2016 = extra_columns(despesas_2016, 2016, "Rodrigo Rollemberg")
despesas_2017 = extra_columns(despesas_2017, 2017, "Rodrigo Rollemberg")
despesas_2018 = extra_columns(despesas_2018, 2018, "Rodrigo Rollemberg")
despesas_2019 = extra_columns(despesas_2019, 2019, "Ibaneis Rocha")
despesas_2020 = extra_columns(despesas_2020, 2020, "Ibaneis Rocha")
despesas_2021 = extra_columns(despesas_2021, 2021, "Ibaneis Rocha")
despesas_2022 = extra_columns(despesas_2022, 2022, "Ibaneis Rocha")

transporte_2009 = despesas_2009[despesas_2009["FUNÇÃO"] == "TRANSPORTE"]
transporte_2010 = despesas_2010[despesas_2010["FUNÇÃO"] == "TRANSPORTE"]
transporte_2011 = despesas_2011[despesas_2011["FUNÇÃO"] == "TRANSPORTE"]
transporte_2012 = despesas_2012[despesas_2012["FUNÇÃO"] == "TRANSPORTE"]
transporte_2013 = despesas_2013[despesas_2013["FUNÇÃO"] == "TRANSPORTE"]
transporte_2014 = despesas_2014[despesas_2014["FUNÇÃO"] == "TRANSPORTE"]
transporte_2015 = despesas_2015[despesas_2015["FUNÇÃO"] == "TRANSPORTE"]
transporte_2016 = despesas_2016[despesas_2016["FUNÇÃO"] == "TRANSPORTE"]
transporte_2017 = despesas_2017[despesas_2017["FUNÇÃO"] == "TRANSPORTE"]
transporte_2018 = despesas_2018[despesas_2018["FUNÇÃO"] == "TRANSPORTE"]
transporte_2019 = despesas_2019[despesas_2019["FUNÇÃO"] == "TRANSPORTE"]
transporte_2020 = despesas_2020[despesas_2020["FUNÇÃO"] == "TRANSPORTE"]
transporte_2021 = despesas_2021[despesas_2021["FUNÇÃO"] == "TRANSPORTE"]
transporte_2022 = despesas_2022[despesas_2022["FUNÇÃO"] == "TRANSPORTE"]

# creating a list of all DataFrames
transporte_list = [transporte_2009,transporte_2010,transporte_2011,
                   transporte_2012,transporte_2013,transporte_2014,
                   transporte_2015,transporte_2016,transporte_2017,
                   transporte_2018,transporte_2019,transporte_2020,
                   transporte_2021,transporte_2022]

# concatenating
transporte_all = pd.concat(transporte_list, ignore_index=True)

# correlation matrix
corr_matrix_tp = transporte_all.corr(numeric_only=True)
# heatmap of the correlation matrix
# tp_corr_hm = sns.heatmap(corr_matrix_tp,cmap="magma",annot=True)

# grouping by year
transporte_yearly = transporte_all.groupby("Ano").sum(numeric_only=True)

# plotting spending on Transportation by year
# plt.figure(figsize=(20,15))
# ax = sns.barplot(transporte_yearly,x=transporte_yearly.index,y="LIQUIDADO",
#                  palette="magma_r")
# ax.axes.set_title("Despesas por Ano em Transporte",fontsize=18)
# ax.set_xlabel("Ano",fontsize=16)
# ax.set_ylabel("Valor LIQUIDADO (em bilhão)",fontsize=16)
# ax.tick_params(labelsize=12)
# plt.show()