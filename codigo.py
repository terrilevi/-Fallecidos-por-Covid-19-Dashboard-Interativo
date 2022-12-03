import streamlit as st 
import pandas as pd
import numpy as np
import gdown
import plotly.express as px
from datetime import datetime
import plotly.graph_objects as go


# id = 1dSRlbtutz10Lgb4wiYPcWaK3w5QMUH8O
@st.experimental_memo
def download_data():
    #https://drive.google.com/uc?id=YOURFILEID\
    url = "https://drive.google.com/uc?id=1dSRlbtutz10Lgb4wiYPcWaK3w5QMUH8O"
    output = 'data.csv'
    gdown.download(url,output,quiet = False)

download_data()
data = pd.read_csv('data.csv', sep = ';', parse_dates= ['FECHA_CORTE' , 'FECHA_FALLECIMIENTO'])
data = data[["FECHA_CORTE","FECHA_FALLECIMIENTO","EDAD_DECLARADA","SEXO", "CLASIFICACION_DEF", "DEPARTAMENTO", "PROVINCIA", "DISTRITO", "UBIGEO", "UUID"]]
#Correción de mala lectura de tildes:
data["CLASIFICACION_DEF"] = data.CLASIFICACION_DEF.map(
        {"Criterio SINADEF":"Criterio SINADEF",
        "Criterio virolÃ³gico":"Criterio virológico",
        "Criterio serolÃ³gico":"Criterio serológico",
        "Criterio investigaciÃ³n EpidemiolÃ³gica":"Criterio investigación epidemiológica",
        "Criterio clÃ­nico":"Criterio clínico",
        "Criterio radiolÃ³gico":"Criterio radiológico",
        "Criterio nexo epidemiolÃ³gico":"Criterio nexo epidemiológico"})



st.title(' Fallecidos por COVID - 19 Dashboard ')
st.header("DataSet de Fallecidos por COVID-19")
st.write("Es el registro diario de muertes por Covid-19. Cada registro es igual a una persona, la cual puede caracterizarse por sexo, edad y ubicación geográfica hasta nivel de distrito; y el código UBIGEO.")
#DataSet de Fallecidos:
st.write(data)
st.write('Fallecidos en el Perú por COVID-19:')
#Contabilizador de cada registro en el DataSet:
st.code(data["SEXO"].count())
st.write('Fallecidos por COVID-19 en mujeres y varones:')
#Contabilizador de cada registro segun sexo en el DataSet:
st.code(data["SEXO"].value_counts())
st.sidebar.markdown('**Fallecidos por COVID - 19 Dashboard**  ')
st.sidebar.markdown('Filtros para visualizar datos en los 4 graficos:  ')

#Creacion de un slider de fechas:
opcion_fecha = st.slider(
    "Seleccione la fecha en la cual desea conocer la cifra de muertes por COVID-19: ",
    min_value = datetime(2020,3,3),
    max_value = datetime(2022,11,19),
    value = (datetime(2020,3,3), datetime(2022,11,19)),
    format="DD/MM/YYYY")
#Acumulacion de registros en las fechas seleccionadas en el slider:
date_var = (data["FECHA_FALLECIMIENTO"].between(*opcion_fecha))
numero_resultados = data[date_var].shape[0]
#Muestra la cantidad contabilizada:
st.write("*Muestra los fallecidos por COVID-19 desde {} hasta {}*".format(opcion_fecha[0], opcion_fecha[1]))
st.code(f'{numero_resultados}')



################################
st.header("Visualización de gráficos según filtros de ubicación geográfica ")
st.write("Para ver la data representada en los siguientes gráficos, debe hace uso de los filtros del sidebar:")

#Crear un selector de departamento en el sidebar:
departamento= np.sort(data['DEPARTAMENTO'].dropna().unique())
opcion_departamento = st.sidebar.selectbox('Selecciona un departamento:', departamento)
data_departamentos = data[data['DEPARTAMENTO'] == opcion_departamento]
num_filas= len(data_departamentos.axes[0])


#Crear un selector de provincia en el sidebar:
provincia= np.sort(data_departamentos['PROVINCIA'].dropna().unique())
opcion_provincia = st.sidebar.selectbox('Selecciona una provincia:', provincia)
data_provincia = data_departamentos[data_departamentos['PROVINCIA']==opcion_provincia]
num_filas= len(data_provincia.axes[0])

#Crear un selector de distritos en el sidebar:
distrito= np.sort(data_provincia['DISTRITO'].dropna().unique())
opcion_distrito = st.sidebar.selectbox('Selecciona una distrito:', distrito)
data_distrito = data_provincia[data_provincia['DISTRITO']==opcion_distrito]
num_filas= len(data_distrito.axes[0])

#Cambiar el aspecto a columnas y colocar respectivos titulos a cada grafico:
col7,col8=st.columns(2)
col1, col2 = st.columns(2)
col7.caption('Fallecidos por COVID-19 según el sexo:')
col8.caption('Fallecidos por COVID-19 según la edad:')
col9,col10= st.columns(2)
col3,col4 =st.columns(2)
col9.caption('Fallecidos por COVID-19 según el criterio:')
col10.caption('Fallecidos por COVID-19 según el criterio:')

#Creacion de 4 graficos:
#Creacion de un grafico de barras segun el sexo:
data_sexo = data_distrito.SEXO.value_counts()
graph1 = col1.bar_chart(data_sexo)

#Creacion de un grafico de barras segun la edad:
data_edad = data_distrito.EDAD_DECLARADA.value_counts()
graph2 = col2.bar_chart(data_edad)

#Creacion de un grafico de lineas segun el criterio:
data_criterio = data_distrito.CLASIFICACION_DEF.value_counts()
chart_data = pd.DataFrame(data_criterio)
col3.line_chart(chart_data)

#Creacion de un grafico circular segun el criterio:
pie_chart = px.pie(data_criterio, 
                   values = 'CLASIFICACION_DEF',
                   names = 'CLASIFICACION_DEF') 
col4.plotly_chart(pie_chart) 



################################
st.header(f"Visualización de la cantidad de muertos por fechas según un criterio")
#Crear un selector de criterios:
criterio= np.sort(data['CLASIFICACION_DEF'].dropna().unique())
opcion_criterio = st.selectbox('Selecciona un criterio:',criterio)
data_criterio = data[data['CLASIFICACION_DEF'] == opcion_criterio]

#Creacion de grafica de barras por fecha segun el criterio:
data_fecha = data_criterio.FECHA_FALLECIMIENTO.value_counts()
st.write('Distribución de la cantidad de muertos por fechas según el  {}'.format(opcion_criterio))
st.bar_chart(data_fecha)



################################
st.header(f"Visualización de la cantidad de muertos segun edad y departamento")
edad= data['EDAD_DECLARADA']
#Creacion de slider de edad, desde la edad minima hasta la maxima del dataset:
edad_selector = st.slider('Seleccione la edad del fallecido: ',
                         min_value = min(edad),
                         max_value = max(edad),
                         value = (min(edad), max(edad)))
#Creacion de multiselector de todos los departamentos del dataset:
departamento_selector = st.multiselect(
                                        'Seleccione departamento(s): ',
                                        departamento,
                                        default = departamento
)

#Union de los dos selectores y creacion del filtro:
filtro = (data['EDAD_DECLARADA'].between(*edad_selector))&(data['DEPARTAMENTO'].isin(departamento_selector))
numero_resultados = data[filtro].shape[0]
st.subheader(f'*Personas fallecidas por departamento(s) seleccionado(s): {numero_resultados}*')
#Agrupa por CALIFICACION y cuenta por los datos de EDAD PERSONA ENCUESTADA:
df_agrupado = data[filtro].groupby(by=['DEPARTAMENTO']).count()[['EDAD_DECLARADA']] 
##
df_agrupado =df_agrupado.rename(columns={'EDAD_DECLARADA': 'NUMERO DE FALLECIDOS'})
df_agrupado =df_agrupado.reset_index()

#Creacion de grafica de barras de personas fallecidas por departamento(s) seleccionado(s):
bar_chart = px.bar(df_agrupado, 
                   x='DEPARTAMENTO',
                   y='NUMERO DE FALLECIDOS',
                   text ='NUMERO DE FALLECIDOS',
                   color_discrete_sequence = ['#f5b632']*len(df_agrupado),
                   template = 'plotly_white')
st.plotly_chart(bar_chart) #mostrar el grafico de barras en streamlit
print(data.count())




#Descargar y crear dataframe para el dataset de ubigeos en el Perú:
# id = 10b-uWf6Io0wo3gbSSDcCjSpCIr6xwLOB
@st.experimental_memo
def download_data():
    #https://drive.google.com/uc?id=YOURFILEID\
    url = "https://drive.google.com/uc?id=10b-uWf6Io0wo3gbSSDcCjSpCIr6xwLOB"
    output = 'TB_UBIGEOS.csv'
    gdown.download(url,output,quiet = False)
download_data()
df_ubigeos = pd.read_csv('TB_UBIGEOS.csv', sep = ',')


data['UBIGEO']= data.UBIGEO.astype(str)
df_ubigeos['ubigeo_inei']= df_ubigeos['ubigeo_inei'].astype(str)
df_ubigeos = df_ubigeos.rename(columns={"ubigeo_inei": "UBIGEO"})
data1= data.merge(df_ubigeos, on="UBIGEO")


st.title("Visualizacion geográfica de fallecidos")
page_names = [ 'Ocultar mapa', 'Mostrar mapa']
page = st.radio('Seleccione una opción:', page_names)

if page == 'Mostrar mapa':
    data1.rename(columns={"latitud":"lat","longitud":"lon"}, inplace=True)
    st.map(data1)
else:
    st.write("")