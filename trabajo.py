import streamlit as st
from PIL import Image
from datetime import datetime
import base64
import time
import numpy as np
import random
import pandas as pd


def sidebar_bg(side_bg):

   side_bg_ext = 'gif'

   st.markdown(
      f"""
      <style>
      [data-testid="stSidebar"] > div:first-child {{
          background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()});
      }}
      </style>
      """,
      unsafe_allow_html=True,
      )



now = datetime.now()
st.write("Dia: ", now.day, " - ", now.month, " - ", now.year)
st.write("Hora: ", now.hour, ":", now.minute)

st.sidebar.image("UPC_logo_transparente.png", use_column_width=True)
st.sidebar.title("FORD FULKER - UPC")
st.sidebar.subheader("MENU")
options = st.sidebar.radio("",options = ["Introduccion", "Integrantes", "Problema", "Aplicacion"])


def introduccion():
    st.markdown("<h1 style='text-align: center;'>Fold Fulker</h1>", unsafe_allow_html=True)
    st.text("El algoritmo de Ford-Fulkerson, un tributo a los distinguidos matemáticos Delbert Fulkerson y Lester R. Ford, constituye una herramienta esencial en la teoría de grafos que se emplea para resolver desafiantes problemas relacionados con el flujo máximo en redes. Esta técnica encuentra aplicación en diversas esferas, como la logística, el transporte y la comunicación, donde es crucial determinar la cantidad óptima de flujo que puede circular a través de una estructura de red representada por un grafo dirigido ponderado. La piedra angular del algoritmo implica la búsqueda de lo que se conoce como caminos aumentantes en la red. En cada iteración, el algoritmo identifica rutas desde un nodo de origen hasta un nodo de destino, a lo largo de las cuales todavía sea factible incrementar el flujo. Al determinar el máximo flujo que puede ser transportado a lo largo de estos caminos específicos y ajustar los flujos en las aristas correspondientes, el algoritmo avanza gradualmente hacia una solución óptima. Para asegurar una convergencia eficaz y la terminación adecuada, la implementación del algoritmo demanda una estrategia cuidadosamente diseñada para la selección de los caminos aumentantes.")
    col1, col2 = st.columns(2)
    with col1:
        st.image("persona.jpg", caption = "Delbert Ray Fulkerson")
    
    with col2:
        st.image("algoritmo.png", caption = "Algoritmo")

def integrantes():

    st.title('Integrantes: \n \n')
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Sebastian Lara / U202214619")
        st.image('Foto.jpeg', width = 250)
    with col2:
        st.subheader("Nicole Silva / U202211152")
        st.image('nicol.jpeg', width = 200)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Samira / u20211a046")
        st.image('samira.jpg', width = 250)
    with col2:
        st.subheader("Sebastian Soto / U202211415")
        st.image('matiassoto.jpeg', width = 200)

    st.header('Profesor')
    st.write('- Luis Daniel Muños Ramos')
    st.header('Curso')
    st.write('- Matemática Computacional')
    st.header('Ciclo')
    st.write('2023 - 02')

def Problema():
    st.markdown("<h1 style='text-align: center;'>Problema del flujo máximo</h1>", unsafe_allow_html=True)
    st.write("Dado 𝑛 ∈ [5, 15] ingresado por el usuario, el programa debe generar aleatoriamente una matriz 𝑛 × 𝑛 (con elementos positivos) o solicitar el ingreso de cada elemento de la matriz (según decisión del usuario). Además, debe mostrar la red de flujos óptima asociada a esta matriz y calcular el flujo máximo que existe entre dos vértices seleccionados por el usuario.")
    st.subheader("Algunos ejemplos: ")

    st.image("algoritmo1.png", width = 600, caption = "Ejemplo 1" )
    st.image("Algoritmo2.jpg", width = 600, caption = "Ejemplo 2" )

    st.subheader("¿Como se planteo el desarrollo?")
    st.write("Al momento de plasmarlo en codigo desarrollado en python, se utilizo la misma logica para colocar una matriz de adyacencia. Cuando en la matriz de adyasencia se requiere conocer si un punto A esta conectado a un punto B, se le reconoce en la matrizcomo 1 y cuando no estan conectados, se le reconoce como 0.")
        
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Grafico")
        st.image('algoritmo2.png', width = 300)
    with col2:
        st.subheader("Matriz")
        st.image('algoritmo3.png', width = 300)

    st.write ("Sin embargo, orientado al codigo, cuando un punto ", ("A"), " esta conectado a un punto B, se le reconoce con el valor directo y cuando no se conecta se le reconoce como 0")
    
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Grafico")
        st.image('fordcito1.png', width = 300)
    with col2:
        st.subheader("Matriz")
        st.image('fordcito2.png', width = 300)

def Aplicacion():

    class grafico:

        def __init__(self, gra):
            self.gra = gra #residual
            self.fila = len(gra)


        def caminoEncontrado(self, s, t, padre):

            #Marcara los vertices como no encontrados
            visitado = [False] * (self.fila)

            #Crear lista para los vertices encontrados
            ver_contrados = []

            #Marcara el nodo de salida como visitado y lo sacara de la lista
            ver_contrados.append(s)
            visitado[s] = True

            #Inicia la lista

            while ver_contrados:

                #Consigue el primer vertice de la lista y lo guarda
                u = ver_contrados.pop(0)

                #Obtendra los vertices adyacentes a "a" y si un vertice no ha sido visitado, lo marcara como visitado y lo sacara de la cola
                for x, y in enumerate(self.gra[u]):
                    if visitado[x] == False and y > 0:
                        ver_contrados.append(x)
                        visitado[x] = True
                        padre[x] = u    
            #Si se llega al vertice de llegada desde el vertice de salida, devuelve True, sino es False 
            return True if visitado[t] else False 
    
        def FordFulkerson(self, salida, llegada):

            #Este vector almacenara a caminoEncontrado 
            padre = [-1] * (self.fila)

            maxFlu = 0 #Lo ponemos con valor 0 por defecto 

            #Aumentara el flujo mientras haya camino desde salida hasta la llegada

            while self.caminoEncontrado(salida, llegada, padre):

                #Establecera la variable como infinito para que se pueda comparar con las demas
                caminoFlu = float("Inf")
                s = llegada

                while (s != salida):
                    #min devuelve el valor minimo
                    caminoFlu = min(caminoFlu, self.gra[padre[s]][s])
                    s = padre[s]

                #se adjunta el flujo que se acaba de obtener al flujo final
                maxFlu += caminoFlu

                #actualiza la capacidad residual de las aristas y las mismas pero inversas 
                v = llegada
                while (v != salida):
                    u = padre[v]
                    self.gra[u][v] -= caminoFlu
                    self.gra[v][u] += caminoFlu
                    v = padre[v]
                gra1 = []
                st.write(f"Camino aumentante encontrado con flujo mínimo {caminoFlu}:")
                st.write(f"Camino: {llegada}", end=" -> ")
                s = llegada
                while s != salida:
                    u = padre[s]
                    st.write(f"{u} -> ", end="")
                    s = u
                st.write(f"{salida}")
                st.write("Matriz de capacidades residuales actualizada:")
                for fil in self.gra:
                    gra1.append(fil)
                gral1 = pd.DataFrame(gra1)
                st.dataframe(gral1)
                st.write(f"Flujo máximo actual: {maxFlu}")
                st.write("-" * 50)
            return maxFlu

    cargar = st.radio("Seleccione que opcion desea para generar los datos",
                      options=["Matriz con datos Random",
                               "Matriz con datos ingresados",
                               "Ejemplo 1",
                               "Ejemplo 2"])
    
    if  cargar == "Matriz con datos Random":
        
        def Generarmatriz(n):
            gra = []
            for _ in range(n):
                fil = [0] * n
                ceros_agregados = n // 2  # La mitad de la fila serán 0
                for _ in range(ceros_agregados):
                    col = random.randint(0, n - 1)
                    while col == _ or fil[col] != 0:  # Evita la diagonal y posiciones ya asignadas
                        col = random.randint(0, n - 1)
                    fil[col] = random.randint(1, 15)  # Se le agregará un valor aleatorio de 1 a 15
                gra.append(fil)
    
            # Asegura que la diagonal sea 0
            for i in range(n):
                gra[i][i] = 0
    
            # Asegura que la posición [n][n] sea 0
            if n > 0:
                gra[n-1][n-1] = 0
    
            return gra

        n = random.randint(5, 15)
        gra = Generarmatriz(n)
        salida = 0
        llegada = n - 1
        g = grafico(gra)

        gral = pd.DataFrame(gra)
        print("Matriz generada:")
        st.write("Matriz generada:")
        st.dataframe(gral)

        
        st.write("Flujo Maximo: %d " %  g.FordFulkerson(salida, llegada))
    elif cargar == "Matriz con datos ingresados":

        archivo = st.file_uploader("Cargar archivo", type="xlsx")
        if archivo is not None:
            df = pd.read_excel(archivo, engine='openpyxl', sheet_name='Hoja1', skiprows=1)
            gra = df.values
            st.dataframe(df)
            g = grafico(gra)
            for index, row in df.iterrows():
                st.write(f"Fila {index}: {row.tolist()}")
            salida = 0
            llegada = len(gra) - 1
            st.write("Flujo Maximo: %d " %  g.FordFulkerson(salida, llegada))
        else:
            st.write("Cargue su archivo .xlsx con las caracteristicas solicitadas")

    elif cargar == "Ejemplo 1":

        graph = [[0, 8, 0, 0, 3, 0],
        [0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 7, 2],
        [0, 0, 0, 0, 0, 5],
        [0, 0, 7, 4, 0, 0],
        [0, 0, 0, 0, 0, 0]]

        salida = 0
        llegada = 5
        g = grafico(graph)
        grol = pd.DataFrame(graph)
        st.subheader("Matriz generada:")
        st.dataframe(grol)
        st.write("Flujo Maximo: %d " %  g.FordFulkerson(salida, llegada))

        st.subheader("Grafico: ")
        st.image('FordFulkerson1.png', width = 600)

    elif cargar == "Ejemplo 2":

        graph2 = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]

        salida = 0
        llegada = 5
        g = grafico(graph2)
        grol2 = pd.DataFrame(graph2)
        st.subheader("Matriz generada:")
        st.dataframe(grol2)
        st.write("Flujo Maximo: %d " %  g.FordFulkerson(salida, llegada))

        st.subheader("Grafico: ")
        st.image('FordFulkerson2.png', width = 600)

if options == "Introduccion":
    introduccion()
    side_bg = 'boca.gif'
    sidebar_bg(side_bg)
elif options == "Integrantes":
    integrantes()
    side_bg = 'boca.gif'
    sidebar_bg(side_bg)
    
elif options == "Problema":
    Problema()
    side_bg = 'boca.gif'
    sidebar_bg(side_bg)
elif options == "Aplicacion":
    Aplicacion()
    side_bg = 'boca.gif'
    sidebar_bg(side_bg)
