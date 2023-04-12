# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 14:44:44 2023

@author: Nevermore
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# importing the data for 2009, correcting column name
despesas_2009 = pd.read_csv("relatoriodespesas2009.csv", sep=";")
despesas_2009 = despesas_2009.drop("Unnamed: 25",axis=1)
despesas_2009.rename(columns = {"Subtitulo":"Subtítulo"}, inplace = True)
# grouping by desired column
dpf_2009 = despesas_2009.groupby("Função",
                                 as_index=False).sum(numeric_only=True)
# organizing by monetary value
dpf_2009 = dpf_2009.sort_values(by="Liquidado",ascending=False,
                                ignore_index=True)

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

# adding three extra columns
dpf_2009 = extra_columns(dpf_2009,2009,"José Roberto Arruda")

# repeating the process for other years
# 2010
despesas_2010 = pd.read_csv("relatoriodespesas2010.csv",sep=";")
despesas_2010 = despesas_2010.drop("Unnamed: 25", axis=1)
despesas_2010.rename(columns={"Subtitulo":"Subtítulo"}, inplace=True)
dpf_2010 = despesas_2010.groupby("Função",
                                 as_index=False).sum(numeric_only=True)
dpf_2010 = dpf_2010.sort_values(by="Liquidado",ascending=False,
                                ignore_index=True)
dpf_2010 = extra_columns(dpf_2010,2010,"José Roberto Arruda")

# 2011
despesas_2011 = pd.read_csv("relatoriodespesas2011.csv",sep=";")
despesas_2011 = despesas_2011.drop("Unnamed: 25", axis=1)
despesas_2011.rename(columns={"Subtitulo":"Subtítulo"}, inplace=True)
dpf_2011 = despesas_2011.groupby("Função",
                                 as_index=False).sum(numeric_only=True)
dpf_2011 = dpf_2011.sort_values(by="Liquidado",ascending=False,
                                ignore_index=True)
dpf_2011 = extra_columns(dpf_2011,2011,"Agnelo Queiroz")

# 2012
despesas_2012 = pd.read_csv("relatoriodespesas2012.csv",sep=";")
despesas_2012 = despesas_2012.drop("Unnamed: 25", axis=1)
despesas_2012.rename(columns={"Subtitulo":"Subtítulo"}, inplace=True)
dpf_2012 = despesas_2012.groupby("Função",
                                 as_index=False).sum(numeric_only=True)
dpf_2012 = dpf_2012.sort_values(by="Liquidado",ascending=False,
                                ignore_index=True)
dpf_2012 = extra_columns(dpf_2012,2012,"Agnelo Queiroz")

# 2013
despesas_2013 = pd.read_csv("relatoriodespesas2013.csv",sep=";")
despesas_2013 = despesas_2013.drop("Unnamed: 25", axis=1)
despesas_2013.rename(columns={"Subtitulo":"Subtítulo"}, inplace=True)
dpf_2013 = despesas_2013.groupby("Função",
                                 as_index=False).sum(numeric_only=True)
dpf_2013 = dpf_2013.sort_values(by="Liquidado",ascending=False,
                                ignore_index=True)
dpf_2013 = extra_columns(dpf_2013,2013,"Agnelo Queiroz")

# 2014
despesas_2014 = pd.read_csv("relatoriodespesas2014.csv",sep=";")
despesas_2014 = despesas_2014.drop("Unnamed: 25", axis=1)
despesas_2014.rename(columns={"Subtitulo":"Subtítulo"}, inplace=True)
dpf_2014 = despesas_2014.groupby("Função",
                                 as_index=False).sum(numeric_only=True)
dpf_2014 = dpf_2014.sort_values(by="Liquidado",ascending=False,
                                ignore_index=True)
dpf_2014 = extra_columns(dpf_2014,2014,"Agnelo Queiroz")

# 2015
despesas_2015 = pd.read_csv("relatoriodespesas2015.csv",sep=";")
despesas_2015 = despesas_2015.drop("Unnamed: 25", axis=1)
despesas_2015.rename(columns={"Subtitulo":"Subtítulo"}, inplace=True)
dpf_2015 = despesas_2015.groupby("Função",
                                 as_index=False).sum(numeric_only=True)
dpf_2015 = dpf_2015.sort_values(by="Liquidado",ascending=False,
                                ignore_index=True)
dpf_2015 = extra_columns(dpf_2015,2015,"Rodrigo Rollemberg")

# 2016
despesas_2016 = pd.read_csv("relatoriodespesas2016.csv",sep=";")
despesas_2016 = despesas_2016.drop("Unnamed: 25", axis=1)
despesas_2016.rename(columns={"Subtitulo":"Subtítulo"}, inplace=True)
dpf_2016 = despesas_2016.groupby("Função",
                                 as_index=False).sum(numeric_only=True)
dpf_2016 = dpf_2016.sort_values(by="Liquidado",ascending=False,
                                ignore_index=True)
dpf_2016 = extra_columns(dpf_2016,2016,"Rodrigo Rollemberg")

# 2017
despesas_2017 = pd.read_csv("relatoriodespesas2017.csv",sep=";")
despesas_2017 = despesas_2017.drop("Unnamed: 25", axis=1)
despesas_2017.rename(columns={"Fonte de Recursos":"Fonte de Recurso",
                              " Total Pago":"Total Pago"},inplace=True)
dpf_2017 = despesas_2017.groupby("Função",
                                 as_index=False).sum(numeric_only=True)
dpf_2017 = dpf_2017.sort_values(by="Liquidado",ascending=False,
                                ignore_index=True)
dpf_2017 = extra_columns(dpf_2017,2017,"Rodrigo Rollemberg")

# 2018
despesas_2018 = pd.read_csv("relatoriodespesas2018.csv",sep=";")
despesas_2018 = despesas_2018.drop("Unnamed: 25", axis=1)
despesas_2018.rename(columns={"Fonte de Recursos":"Fonte de Recurso",
                              " Total Pago":"Total Pago"},inplace=True)
dpf_2018 = despesas_2018.groupby("Função",
                                 as_index=False).sum(numeric_only=True)
dpf_2018 = dpf_2018.sort_values(by="Liquidado",ascending=False,
                                ignore_index=True)
dpf_2018 = extra_columns(dpf_2018,2018,"Rodrigo Rollemberg")

# 2019
despesas_2019 = pd.read_csv("relatoriodespesas2019.csv",sep=";")
despesas_2019 = despesas_2019.drop("Unnamed: 25", axis=1)
despesas_2019.rename(columns={"Fonte de Recursos":"Fonte de Recurso",
                              " Total Pago":"Total Pago"},inplace=True)
dpf_2019 = despesas_2019.groupby("Função",
                                 as_index=False).sum(numeric_only=True)
dpf_2019 = dpf_2019.sort_values(by="Liquidado",ascending=False,
                                ignore_index=True)
dpf_2019 = extra_columns(dpf_2019,2019,"Ibaneis Rocha")

# 2020
despesas_2020 = pd.read_csv("relatoriodespesas2020.csv",sep=";")
despesas_2020 = despesas_2020.drop("Unnamed: 25", axis=1)
despesas_2020.rename(columns={"Fonte de Recursos":"Fonte de Recurso",
                              " Total Pago":"Total Pago"},inplace=True)
dpf_2020 = despesas_2020.groupby("Função",
                                 as_index=False).sum(numeric_only=True)
dpf_2020 = dpf_2020.sort_values(by="Liquidado",ascending=False,
                                ignore_index=True)
dpf_2020 = extra_columns(dpf_2020,2020,"Ibaneis Rocha")

# putting all the created DataFrames together into a list
dpf_list = [dpf_2009,dpf_2010,dpf_2011,dpf_2012,
            dpf_2013,dpf_2014,dpf_2015,dpf_2016,
            dpf_2017,dpf_2018,dpf_2019,dpf_2020]

# concatenating to create a DataFrame contemplating all years
dpf_all_years = pd.concat(dpf_list, ignore_index=True)

# creating a correlation matrix
corr_matrix_dpf = dpf_all_years.corr(numeric_only=True)
# heatmap of the correlation matrix
# dpf_corr_hm = sns.heatmap(corr_matrix_dpf, cmap="magma", annot=True)

# plotting the spending for each designated 'function' by year
# plt.figure(figsize=(25,80))
# ax_log_dpf = sns.barplot(data=dpf_all_years,x="Liquidado",y="Função",hue="Ano",
#                          palette="Spectral")
# ax_log_dpf.axes.set_title("Despesas por Função",fontsize=18) # title
# ax_log_dpf.set_xlabel("Valor Liquidado",fontsize=16) # x axis label
# ax_log_dpf.set_ylabel("Função",fontsize=16) # y axis label
# ax_log_dpf.tick_params(labelsize=20)
# ax_log_dpf.set_xscale("log") # setting to log scale for better visualization
# plt.show()

# plotting the spending for each designated 'function' in 2020
# plt.figure(figsize=(20,15))
# ax_log_2020 = sns.barplot(dpf_2020,x="Liquidado",y="Função",palette="magma_r")
# ax_log_2020.axes.set_title("Despesas por Função - 2020",fontsize=18) # title
# ax_log_2020.set_xlabel("Valor Liquidado",fontsize=16) # x axis label
# ax_log_2020.set_ylabel("Função",fontsize=16) # y axis label
# ax_log_2020.tick_params(labelsize=12)
# ax_log_2020.set_xscale("log") # setting to log scale for better visualization
# plt.show()

# turning DataFrame to series for plotting percentages onto a pie chart
dpf_2020_series = pd.Series(data=list(dpf_2020["Liquidado"]),
                            index=list(dpf_2020["Função"]))
colors = sns.color_palette("icefire_r",n_colors=25) # selecting color palette
# plt.pie(dpf_2020_series,labels=dpf_2020_series.index,colors=colors,
#         autopct="%1.2f%%") # bad visualization of lower values
# plt.show()

# creating DataFrames for each year only for the Transportation 'function'
transporte_2009 = despesas_2009[despesas_2009["Função"] == "TRANSPORTE"]
transporte_2010 = despesas_2010[despesas_2010["Função"] == "TRANSPORTE"]
transporte_2011 = despesas_2011[despesas_2011["Função"] == "TRANSPORTE"]
transporte_2012 = despesas_2012[despesas_2012["Função"] == "TRANSPORTE"]
transporte_2013 = despesas_2013[despesas_2013["Função"] == "TRANSPORTE"]
transporte_2014 = despesas_2014[despesas_2014["Função"] == "TRANSPORTE"]
transporte_2015 = despesas_2015[despesas_2015["Função"] == "TRANSPORTE"]
transporte_2016 = despesas_2016[despesas_2016["Função"] == "TRANSPORTE"]
transporte_2017 = despesas_2017[despesas_2017["Função"] == "TRANSPORTE"]
transporte_2018 = despesas_2018[despesas_2018["Função"] == "TRANSPORTE"]
transporte_2019 = despesas_2019[despesas_2019["Função"] == "TRANSPORTE"]
transporte_2020 = despesas_2020[despesas_2020["Função"] == "TRANSPORTE"]

# removing unnecessary columns
columns_list = ["CPF/CNPJ do Credor","Número do Processo"]

for i in columns_list:
    transporte_2009 = transporte_2009.drop(i,axis=1)
    transporte_2010 = transporte_2010.drop(i,axis=1)
    transporte_2011 = transporte_2011.drop(i,axis=1)
    transporte_2012 = transporte_2012.drop(i,axis=1)
    transporte_2013 = transporte_2013.drop(i,axis=1)
    transporte_2014 = transporte_2014.drop(i,axis=1)
    transporte_2015 = transporte_2015.drop(i,axis=1)
    transporte_2016 = transporte_2016.drop(i,axis=1)

columns_list2 = ["Nº do Processo","CNPJ/CPF Credor"]

for i in columns_list2:
    transporte_2017 = transporte_2017.drop(i,axis=1)
    transporte_2018 = transporte_2018.drop(i,axis=1)
    transporte_2019 = transporte_2019.drop(i,axis=1)
    transporte_2020 = transporte_2020.drop(i,axis=1)

# adding 3 extra columns for each DataFrame
transporte_2009 = extra_columns(transporte_2009,2009,"José Roberto Arruda")
transporte_2010 = extra_columns(transporte_2010,2010,"José Roberto Arruda")
transporte_2011 = extra_columns(transporte_2011,2011,"Agnelo Queiroz")
transporte_2012 = extra_columns(transporte_2012,2012,"Agnelo Queiroz")
transporte_2013 = extra_columns(transporte_2013,2013,"Agnelo Queiroz")
transporte_2014 = extra_columns(transporte_2014,2014,"Agnelo Queiroz")
transporte_2015 = extra_columns(transporte_2015,2015,"Rodrigo Rollemberg")
transporte_2016 = extra_columns(transporte_2016,2016,"Rodrigo Rollemberg")
transporte_2017 = extra_columns(transporte_2017,2017,"Rodrigo Rollemberg")
transporte_2018 = extra_columns(transporte_2018,2018,"Rodrigo Rollemberg")
transporte_2019 = extra_columns(transporte_2019,2019,"Ibaneis Rocha")
transporte_2020 = extra_columns(transporte_2020,2020,"Ibaneis Rocha")

# creating a list of all DataFrames
transporte_list = [transporte_2009,transporte_2010,transporte_2011,
                   transporte_2012,transporte_2013,transporte_2014,
                   transporte_2015,transporte_2016,transporte_2017,
                   transporte_2018,transporte_2019,transporte_2020]

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
# ax = sns.barplot(transporte_yearly,x=transporte_yearly.index,y="Liquidado",
#                  palette="magma_r")
# ax.axes.set_title("Despesas por Ano em Transporte",fontsize=18)
# ax.set_xlabel("Ano",fontsize=16)
# ax.set_ylabel("Valor Liquidado (em bilhão)",fontsize=16)
# ax.tick_params(labelsize=12)
# plt.show()