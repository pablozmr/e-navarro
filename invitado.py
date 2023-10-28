import streamlit as st
import pandas as pd

# Página de inicio de sesiónimport streamlit as st

# Página de inicio de sesión
    
def buscar_page():
    df = pd.read_csv("placas.csv")
    parametro = st.selectbox('Seleccione por cual parametro desea buscar', ("Fuente", "Televisor", "Numero"))
    if parametro == "Fuente":
        fuente = st.text_input("")
    elif parametro == "Televisor":
        televisor = st.selectbox("", df.televisor.values)
    elif parametro == "Numero":
        nro = st.number_input("",min_value=0, max_value=None , value= 0, step=1)
        
    
    if st.button('Buscar'):
        if parametro == "Fuente":
            st.dataframe(df.loc[df['fuente'] == fuente])
        elif parametro == "Televisor":
            st.dataframe(df.loc[df['televisor'] == televisor])
        elif parametro == "Numero":
            st.dataframe(df.loc[df['nro'] == nro])
    
    df = pd.read_csv('placas.csv')
    st.subheader('Tabla de stocks')
    st.dataframe(df)


def main():
    
    st.title('Electronica Navarro')
    
    buscar_page()
    
    
    


if __name__ == "__main__":
    
    main()

