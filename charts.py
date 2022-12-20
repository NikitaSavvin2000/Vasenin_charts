import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


print('Ation = 1 - print Charts Electricity consuption')
print('Ation = 2 - print Charts Energy consuption')
action = int(input('Input action '))

Electricity = 'Total Electricity Consumption.xlsx' # Total Electricity Consumption
Energy = 'Total energy consumption_World.xlsx' # Total energy consumption_World

TEC_World_df = pd.read_excel(Electricity, sheet_name='World')
TEC_Europe_df = pd.read_excel(Electricity, sheet_name='Europe')
TEC_Italy_df = pd.read_excel(Electricity, sheet_name='Italy')

''' parse_str_to_int - processing dry data from xlsx to clean data float type'''
def parse_str_to_int(dradt_array):
    clean_array = []
    for i in range(len(dradt_array)):
        p = str(dradt_array[i])
        s = list(p)
        for w in range(1, len(s)-1):
            if s[w] in [',', ':', ';', "'", '*']:
                s[w] = '.'
        if s[-1] in ['0','1','2','3','4','5','6','7','8','9']:
            a1 = 1
        else:
            del s[-1]
        if s[0] in ['0','1','2','3','4','5','6','7','8','9','-']:
            a = 2
        else:
            del s[0]
        s = ''.join(s)
        clean_array.append(float(s))
    return clean_array

''' creature_chart_percent - function creature charts paramentrs percent'''
def creature_chart_percent(year, params, country, label, nameChart):
    colorContry = {
        'World' : 'r',
        'Europe': 'g',
        'Italy': 'b'
    }
    fig, ax = plt.subplots()
    ax.set_xlabel('Year')
    ax.set_ylabel(label)

    ax.axhline(y=0, color='k', linewidth=0.8)
    ax.axvline(x=1990, color='k', linewidth=0.8, linestyle='--')
    ax.grid()
    label = country
    color = colorContry[country]
    ax.plot(year, params, '-o', label=label, color=color)
    plt.title(nameChart, loc='center', pad=31)
    ax.legend()
    plt.show()

''' creature_comparative_chart_percent - function creature comparative charts paramentrs percent'''
def creature_comparative_chart_percent(year, paramsW, paramsE, paramsI, label, nameChart):
    fig, ax = plt.subplots()
    ax.set_xlabel('Year')
    ax.set_ylabel(label)

    ax.axhline(y=0, color='k', linewidth = 0.8)
    ax.axvline(x=1990, color='k', linewidth = 0.8, linestyle = '--')
    ax.grid()

    ax.plot(year, paramsW, '-o', label='World', color = 'r')
    ax.plot(year, paramsE, '-o', label='Europe', color = 'g')
    ax.plot(year, paramsI,  '-o', label='Italy', color = 'b')
    plt.title(nameChart, loc = 'center', pad = 31)
    ax.legend()
    plt.show()

''' creature_chart - function creature charts paramentrs Watt'''
def creature_chart(year, params, country, label, nameChart):
    colorContry = {
        'World' : 'r',
        'Europe': 'g',
        'Italy': 'b'
    }
    fig, ax = plt.subplots()
    ax.set_xlabel('Year')
    ax.set_ylabel(label)

    ax.axvline(x=1990, color='k', linewidth=0.8, linestyle='--')
    ax.grid()
    label = country
    color = colorContry[country]
    ax.plot(year, params, '-o', label=label, color=color)
    plt.title(nameChart, loc='center', pad=31)
    ax.ticklabel_format(style='plain')
    ax.legend()
    plt.show()

''' ------------- 1. Data Electricity consuption-----------------'''
# Read and processing data

TEC_World_df = pd.read_excel(Electricity , sheet_name='World')
TEC_Europe_df = pd.read_excel(Electricity , sheet_name='Europe')
TEC_Italy_df = pd.read_excel(Electricity , sheet_name='Italy')

year_W = np.array(TEC_World_df['Year'])
TEC_G_I_TJ_W = np.array(TEC_World_df['TEC,G,I,TJ'])
TEC_R_I_TJ_W= np.array(TEC_World_df['TEC,R,I,TJ'])
TEC_G_W = np.array(TEC_World_df['∆%TEC,G'])
TEC_R_W = np.array(TEC_World_df['∆%TEC,R'])

year_E = np.array(TEC_Europe_df['Year'])
TEC_G_I_TJ_E = np.array(TEC_Europe_df['TEC,G,I,TJ'])
TEC_R_I_TJ_E= np.array(TEC_Europe_df['TEC,R,I,TJ'])
TEC_G_E = np.array(TEC_Europe_df['∆%TEC,G'])
TEC_R_E = np.array(TEC_Europe_df['∆%TEC,R'])

year_I = np.array(TEC_Italy_df['Year'])
TEC_G_I_TJ_I = np.array(TEC_Italy_df['TEC,G,I,TJ'])
TEC_R_I_TJ_I= np.array(TEC_Italy_df['TEC,R,I,TJ'])
TEC_G_I = np.array(TEC_Italy_df['∆%TEC,G'])
TEC_R_I = np.array(TEC_Italy_df['∆%TEC,R'])

year_W = parse_str_to_int(year_W)
TEC_G_I_TJ_W = parse_str_to_int(TEC_G_I_TJ_W)
TEC_R_I_TJ_W= parse_str_to_int(TEC_R_I_TJ_W)
TEC_G_W = parse_str_to_int(TEC_G_W)
TEC_R_W = parse_str_to_int(TEC_R_W)

year_E = parse_str_to_int(year_E)
TEC_G_I_TJ_E = parse_str_to_int(TEC_G_I_TJ_E)
TEC_R_I_TJ_E= parse_str_to_int(TEC_R_I_TJ_E)
TEC_G_E = parse_str_to_int(TEC_G_E)
TEC_R_E = parse_str_to_int(TEC_R_E)

year_I = parse_str_to_int(year_I)
TEC_G_I_TJ_I = parse_str_to_int(TEC_G_I_TJ_I)
TEC_R_I_TJ_I = parse_str_to_int(TEC_R_I_TJ_I)
TEC_G_I = parse_str_to_int(TEC_G_I)
TEC_R_I = parse_str_to_int(TEC_R_I)

''' ------------- 2. Data Energy consuption-----------------'''
# Read and processing data
TEC_World_Energy_df = pd.read_excel(Energy, sheet_name='World')
TEC_Europe_Energy_df = pd.read_excel(Energy, sheet_name='Europe')
TEC_Italy_Energy_df = pd.read_excel(Energy, sheet_name='Italy')

year_Energy_W = np.array(TEC_World_Energy_df['Year'])
TEC_G_I_TJ_Energy_W = np.array(TEC_World_Energy_df['TEC,G,I,TJ'])
TEC_R_I_TJ_Energy_W = np.array(TEC_World_Energy_df['TEC,R,I,TJ'])
TEC_G_Energy_W = np.array(TEC_World_Energy_df['∆%TEC,G'])
TEC_R_Energy_W = np.array(TEC_World_Energy_df['∆%TEC,R'])

year_Energy_E = np.array(TEC_Europe_Energy_df['Year'])
TEC_G_I_TJ_Energy_E = np.array(TEC_Europe_Energy_df['TEC,G,I,TJ'])
TEC_R_I_TJ_Energy_E= np.array(TEC_Europe_Energy_df['TEC,R,I,TJ'])
TEC_G_Energy_E = np.array(TEC_Europe_Energy_df['∆%TEC,G'])
TEC_R_Energy_E = np.array(TEC_Europe_Energy_df['∆%TEC,R'])

year_Energy_I = np.array(TEC_Italy_Energy_df['Year'])
TEC_G_I_TJ_Energy_I = np.array(TEC_Italy_Energy_df['TEC,G,I,TJ'])
TEC_R_I_TJ_Energy_I= np.array(TEC_Italy_Energy_df['TEC,R,I,TJ'])
TEC_G_Energy_I = np.array(TEC_Italy_Energy_df['∆%TEC,G'])
TEC_R_Energy_I = np.array(TEC_Italy_Energy_df['∆%TEC,R'])


year_Energy_W = parse_str_to_int(year_Energy_W)
TEC_G_I_TJ_Energy_W = parse_str_to_int(TEC_G_I_TJ_Energy_W)
TEC_R_I_TJ_Energy_W= parse_str_to_int(TEC_R_I_TJ_Energy_W)
TEC_G_Energy_W = parse_str_to_int(TEC_G_Energy_W)
TEC_R_Energy_W = parse_str_to_int(TEC_R_Energy_W)

year_Energy_E = parse_str_to_int(year_Energy_E)
TEC_G_I_TJ_Energy_E = parse_str_to_int(TEC_G_I_TJ_Energy_E)
TEC_R_I_TJ_Energy_E= parse_str_to_int(TEC_R_I_TJ_Energy_E)
TEC_G_Energy_E = parse_str_to_int(TEC_G_Energy_E)
TEC_R_Energy_E = parse_str_to_int(TEC_R_Energy_E)

year_Energy_I = parse_str_to_int(year_Energy_I)
TEC_G_I_TJ_Energy_I = parse_str_to_int(TEC_G_I_TJ_Energy_I)
TEC_R_I_TJ_Energy_I = parse_str_to_int(TEC_R_I_TJ_Energy_I)
TEC_G_Energy_I = parse_str_to_int(TEC_G_Energy_I)
TEC_R_Energy_I = parse_str_to_int(TEC_R_Energy_I)


''' ------------- 1. Charts Electricity consuption-----------------'''
# ---------1.1 Charts of parametrs by country(Electricity)-------

if action == 1:
    print('Charts Electricity consuption')
    creature_chart(year_W, TEC_G_I_TJ_W, 'World', 'TEC,G,I,TJ', 'Electricity Consuption')
    creature_chart(year_E, TEC_G_I_TJ_E, 'Europe', 'TEC,G,I,TJ', 'Electricity Consuption')
    creature_chart(year_I, TEC_G_I_TJ_I, 'Italy', 'TEC,G,I,TJ', 'Electricity Consuption')

    creature_chart(year_W, TEC_R_I_TJ_W, 'World', 'TEC,R,I,TJ', 'Electricity Consuption')
    creature_chart(year_I, TEC_R_I_TJ_E, 'Europe', 'TEC,R,I,TJ', 'Electricity Consuption')
    creature_chart(year_I, TEC_R_I_TJ_I, 'Italy', 'TEC,R,I,TJ', 'Electricity Consuption')

    creature_chart_percent(year_W, TEC_G_W, 'World', '∆% TEC,G', 'Electricity Consuption')
    creature_chart_percent(year_E, TEC_G_E, 'Europe', '∆% TEC,G', 'Electricity Consuption')
    creature_chart_percent(year_I, TEC_G_I, 'Italy', '∆% TEC,G', 'Electricity Consuption')

    creature_chart_percent(year_W, TEC_R_W, 'World', '∆% TEC,R', 'Electricity Consuption')
    creature_chart_percent(year_E, TEC_R_E, 'Europe', '∆% TEC,R', 'Electricity Consuption')
    creature_chart_percent(year_I, TEC_R_I, 'Italy', '∆% TEC,R', 'Electricity Consuption')


   #----------1.2 Comparison charts by country (Electricity)--------

    creature_comparative_chart_percent(
        year_W, TEC_G_W, TEC_G_E, TEC_G_I, '∆% TEC,G', 'Electricity Consuption'
    )
    creature_comparative_chart_percent(
        year_W, TEC_R_W, TEC_R_E, TEC_R_I, '∆% TEC,R', 'Electricity Consuption'
    )

# ------------- 2. Charts Energy consuption-----------------'''
# ---------2.1 Charts of parametrs by country(Energy)-------'''

elif action == 2:
    print('Charts Energy consuption')
    creature_chart(year_Energy_W, TEC_G_I_TJ_Energy_W, 'World', 'TEC,G,I,TJ', 'Energy Consuption')
    creature_chart(year_Energy_E, TEC_G_I_TJ_Energy_E, 'Europe', 'TEC,G,I,TJ', 'Energy Consuption')
    creature_chart(year_Energy_I, TEC_G_I_TJ_Energy_I, 'Italy', 'TEC,G,I,TJ', 'Energy Consuption')

    creature_chart(year_Energy_W, TEC_R_I_TJ_Energy_W, 'World', 'TEC,R,I,TJ', 'Energy Consuption')
    creature_chart(year_Energy_I, TEC_R_I_TJ_Energy_E, 'Europe', 'TEC,R,I,TJ', 'Energy Consuption')
    creature_chart(year_Energy_I, TEC_R_I_TJ_Energy_I, 'Italy', 'TEC,R,I,TJ', 'Energy Consuption')

    creature_chart_percent(year_Energy_W, TEC_G_Energy_W, 'World', '∆% TEC,G', 'Energy Consuption')
    creature_chart_percent(year_Energy_E, TEC_G_Energy_E, 'Europe', '∆% TEC,G', 'Energy Consuption')
    creature_chart_percent(year_Energy_I, TEC_G_Energy_I, 'Italy', '∆% TEC,G', 'Energy Consuption')

    creature_chart_percent(year_W, TEC_R_Energy_W, 'World', '∆% TEC,R', 'Energy Consuption')
    creature_chart_percent(year_E, TEC_R_Energy_E, 'Europe', '∆% TEC,R', 'Energy Consuption')
    creature_chart_percent(year_I, TEC_R_Energy_I, 'Italy', '∆% TEC,R', 'Energy Consuption')

# ----------2.2 Comparison charts by country (Energy)--------

    creature_comparative_chart_percent(
        year_Energy_W, TEC_G_Energy_W, TEC_G_Energy_E, TEC_G_Energy_I, '∆% TEC,G', 'Energy Consuption'
    )
    creature_comparative_chart_percent(
        year_Energy_W, TEC_R_Energy_W, TEC_R_Energy_E, TEC_R_Energy_I, '∆% TEC,R', 'Energy Consuption'
    )
