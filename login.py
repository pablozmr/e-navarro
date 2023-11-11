import streamlit as st
import pandas as pd
import git

# Página de inicio de sesiónimport streamlit as st

# Página de inicio de sesión
def login():
    st.write("¡Bienvenido al sistema!.")
    
    st.title("Inicia sesion:")
    user = st.text_input("Usuario: ")
    password = st.text_input("Password: ", type= "password")
    if st.button("Iniciar Sesión"):
        if user == "usuario" and password == "password":
            st.success("Inicio de sesión correcto.")
            
            return True
    
def usuario():
    add_selectbox = st.sidebar.selectbox("Que desea hacer?",
    ("Buscar", "Añadir / Editar"))
    if add_selectbox == "Buscar":
        buscar_page()
    elif add_selectbox == "Añadir / Editar":
        editar_page()

    df = pd.read_csv("placas.csv")
    st.subheader('Tabla de stocks')
    st.dataframe(df)
    
    
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

def editar_page():
    df = pd.read_csv("placas.csv")
    st.column_config.TextColumn("fuente")
    edited_df = st.data_editor(df, num_rows="dynamic")
    
    
    
    if st.button("Guardar"):
        edited_df.to_csv("placas.csv", index= False)
        #URL del repositorio de GitHub
        repo_url = "https://github.com/pablozmr/e-navarro.git"
        local_path = "local_path"
        
        # Manejo de excepciones para clonar o abrir el repositorio
        try:
            # Intenta abrir el repositorio existente
            repo = git.Repo(local_path)
            st.success("Repositorio existente abierto con éxito.")
        
        except git.exc.NoSuchPathError:
            # Si el repositorio no existe, clónalo
            repo = git.Repo.clone_from(repo_url, local_path)
            st.success("Repositorio clonado con éxito.")
        
        except git.exc.InvalidGitRepositoryError:
            st.error(f"Error: {local_path} no es un repositorio Git válido.")

def main():
    
    st.title('Electronica Navarro')
    
    usuario()
    
    
    


if __name__ == "__main__":
    
    main()



    
    
    
