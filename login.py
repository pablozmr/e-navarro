import streamlit as st
import pandas as pd
import gspread
# Página de inicio de sesiónimport streamlit as st
gc = gspread.service_account(filename='clase.json')
sht2 = gc.open_by_url('https://docs.google.com/spreadsheets/d/10kOz5eGToPogxndeAmXizvdGszqaD-Zin9mO5yoMNK0/edit?usp=sharing')
worksheet = sht2.get_worksheet(0)
list_of_dicts = worksheet.get_all_records()
df = pd.DataFrame(list_of_dicts)
# Página de inicio de sesión
    
def usuario():
    add_selectbox = st.sidebar.selectbox("Que desea hacer?",
    ("Buscar", "Añadir / Editar"))
    if add_selectbox == "Buscar":
        buscar_page()
    elif add_selectbox == "Añadir / Editar":
        editar_page()
        
    
    
def buscar_page():
    df = pd.DataFrame(list_of_dicts)
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
    df = pd.DataFrame(list_of_dicts)
    st.column_config.TextColumn("fuente")
    edited_df = st.data_editor(df, num_rows="dynamic")
    
    df = edited_df
    
    if st.button("Editar"):
        worksheet.update([df.columns.values.tolist()] + df.values.tolist())

    

def main():
    
    
    st.title('Electronica Navarro')
    
    usuario()
    
    
    


if __name__ == "__main__":
    
    main()



    
    
