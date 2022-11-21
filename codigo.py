import streamlit as st 
import pandas as pd
import numpy as np
import gdown
import os


st.title('Fallecidos por COVID19')

st.title('Fallecidos por COVID19')


# id = 1dSRlbtutz10Lgb4wiYPcWaK3w5QMUH8O
@st.experimental_memo
def download_data():
    #https://drive.google.com/uc?id=YOURFILEID\
    url = "https://drive.google.com/uc?id=1dSRlbtutz10Lgb4wiYPcWaK3w5QMUH8O"
    output = 'data.csv'
    gdown.download(url,output,quiet = False)

download_data()
#vamos a sacar el primer millon de datos:
data = pd.read_csv('data.csv', sep = ';', parse_dates= ['FECHA_CORTE', 'FECHA_FALLECIMIENTO'])
st.dataframe(data.head(20))
#df = df.drop(columns = ["FECHA_CORTE","FECHA_FALLECIMIENTO","EDAD_DECLARADA","SEXO", "CLASIFICACION_DEF", "DEPARTAMENTO", "PROVINCIA", "DISTRITO", "UBIGEO", "UUID"])


#edad = np.sort(df['EDAD_DECLARADA'].dropna().unique())          
#sexo = np.sort(df['SEXO'].dropna().unique())

edad= data['EDAD_DECLARADA']
sexo= data['SEXO']
departamento= data['DEPARTAMENTO']

#edad= df['EDAD_DECLARADA'].unique().tolist()
#edad = np.sort(df['EDAD_DECLARADA'].dropna().unique())

#crear un slider de edad
edad_selector = st.slider('Edad del fallecido: ',
                         min_value = min(edad),
                         max_value = max(edad),
                         value = (min(edad), max(edad)))


#sexo_selector = st.multiselect('SEXO:', sexo, default = ciudad)
st.write(sexo)
st.write(departamento)
opcion_departamento = st.selectbox('Selecciona un departamento:', departamento)

import tkinter as tk

fields = ('Annual Rate', 'Number of Payments', 'Loan Principle', 'Monthly Payment', 'Remaining Loan')

def monthly_payment(entries):
    # period rate:
    r = (float(entries['Annual Rate'].get()) / 100) / 12
    print("r", r)
    # principal loan:
    loan = float(entries['Loan Principle'].get())
    n =  float(entries['Number of Payments'].get())
    remaining_loan = float(entries['Remaining Loan'].get())
    q = (1 + r)** n
    monthly = r * ( (q * loan - remaining_loan) / ( q - 1 ))
    monthly = ("%8.2f" % monthly).strip()
    entries['Monthly Payment'].delete(0, tk.END)
    entries['Monthly Payment'].insert(0, monthly )
    print("Monthly Payment: %f" % float(monthly))

def final_balance(entries):
    # period rate:
    r = (float(entries['Annual Rate'].get()) / 100) / 12
    print("r", r)
    # principal loan:
    loan = float(entries['Loan Principle'].get())
    n =  float(entries['Number of Payments'].get()) 
    monthly = float(entries['Monthly Payment'].get())
    q = (1 + r) ** n
    remaining = q * loan  - ( (q - 1) / r) * monthly
    remaining = ("%8.2f" % remaining).strip()
    entries['Remaining Loan'].delete(0, tk.END)
    entries['Remaining Loan'].insert(0, remaining )
    print("Remaining Loan: %f" % float(remaining))

def makeform(root, fields):
    entries = {}
    for field in fields:
        print(field)
        row = tk.Frame(root)
        lab = tk.Label(row, width=22, text=field+": ", anchor='w')
        ent = tk.Entry(row)
        ent.insert(0, "0")
        row.pack(side=tk.TOP, 
                 fill=tk.X, 
                 padx=5, 
                 pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, 
                 expand=tk.YES, 
                 fill=tk.X)
        entries[field] = ent
    return entries

if __name__ == '__main__':
    root = tk.Tk()
    ents = makeform(root, fields)
    b1 = tk.Button(root, text='Final Balance',
           command=(lambda e=ents: final_balance(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b2 = tk.Button(root, text='Monthly Payment',
           command=(lambda e=ents: monthly_payment(e)))
    b2.pack(side=tk.LEFT, padx=5, pady=5)
    b3 = tk.Button(root, text='Quit', command=root.quit)
    b3.pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()
