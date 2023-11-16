import streamlit as st
import pandas as pd
import gspread
# Configuracion pag
st.set_page_config(
    page_title="e-Navarro",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded")

# Página de inicio de sesión
credentials = {
        "type": "service_account",
        "project_id": "e-navarro",
        "private_key_id": "a125c942b695da27678af50a8ae4449a86a359b6",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDPuTnizI8h/1XU\nkzruSLpfhNRx53P/ZAI3uK94jif1xPfdeyrmXO9pJuXJyztctYteFWdEVBiApz16\naz8iTDYSpsIj1Y7vn9+V1Myqfof42XTnxJ3/P89MpxRRk1Yt/WvMj+QT3Jl2KSZe\ncpSRFSvY/fqkD4kgUTitjYPIx7QjstC1N+j6eG3dF5lhz9LD+bH1qsIGK8ntychX\nGKDL+qIuDdNxQt2y0fdXeabwvVoqISdywxsF4EKFBSVEMsHOxFhwUP/jtj+Dz9YV\nGbvJFeDYWjKeie6J0jk/n8M5yNAccZOqpgnCTE1KZiy+tPErA0yDZlaeKj88WmM6\nsPRUStAdAgMBAAECggEAIRv2/A166wJV3fIxvHVfL4ZujlFEDfsU12jany6Zc/UX\nRPgy2FEL4AjRK573MUnGkxJ6SUvWM/t0MyURBRh8rfBilW+evtcOvkUS8kIEzkdq\n+N5ACMVU93TSKkZ/wAjau9pbkkbhNxJMCVXeFFn5iTbCUpAfXUVU8WTTEpeyQNYf\n73Owfqyl09IMHHPZ5M8zPA589GFmfYMB8Xp/OPOCUD9Bq7V4L8BH12zhuFByWQfS\nQKO10u7PXvreTV3oKmmi6EA/x63R8n4N43nhwXTycUKguyHpUF0d9xAOSCksJEPD\nw7WCc8giX6j6NM4BdrSQLRQ2TCYgZjVyHSpRXiOfCQKBgQD4/UckRPXEmjQSpuoI\nUjrQB7KX1DJ0GL21//tgF9tLBCPWp65d1P+z5AxiS3aYGhhyXnlmByrg4V/eCyzv\nWoP2rOCnQPhV7amqx+BCt52DkkycXfVoenRRJF+XxjDyGUl9DFo2n1Bb21vr8lcL\nrTkDSuQRYktbBqeY79A55F0ZmwKBgQDVkoDF09JxkecCCXfLgaX7e+uwxCyIlp2b\nhLxJMlDDvFRM/+icKqnvWaC0asxzs7yOpBiI3dqGzAb7DJxni/qm067jJqX0Knch\ngqfF8DiymhX38Wgns42W1j0MhLZlQXSlwIaWq7gBg++XwSMrzxqMn6x8nF5pkY3s\nfUDt/R0UpwKBgE1FtXVxHWD1hmGfgZQxiOUU7n0mMr5LC11XYzkwTjNaxpCQm5Gt\nT+oRRTKgPt73gkzEOyLJ6Km/6BOuHjTuP3QntNTTWf648mX5AAVUnMK/fZ0tn8Lb\n9gtUoYIl1PzdkiwH0FuRV8waKM3x+Me766y06lDm04Idb5gMHPBKigYvAoGAQnTw\n/x33qQFWmcqqbTftl0CrSXjxxprfdioqkLhIa2/p53/mONoJwQHpwNpOvl4aeWRU\nghpOyo0oSuxUqt/i4hCSpfo7v6uLIHFQlYY3jlPmLB4BZAE6OMp3erK9MurYSk+L\nUc0jV81fO6CMujAaudFh0fCybDUvrXwYPTX625cCgYEAzCHrC1NmzMrhvT9h8uKz\ndrQCPmDB8pm3mVAhRY2ZUDl5Omayq2s8/tB0lNarmm/wcJzRDy0LN8DcuUB75RLO\ns4Huvtx9sABAMJZcwJQHcdkvgtLddbAvlDc95Tg8PX1IXTiQ3iS4aMe25sLv8O0t\nBY5pUjxY+BStiePmiHhXCnM=\n-----END PRIVATE KEY-----\n",
        "client_email": "e-navarro@e-navarro.iam.gserviceaccount.com",
        "client_id": "109846752915441902407",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/e-navarro%40e-navarro.iam.gserviceaccount.com",
        "universe_domain": "googleapis.com"
}

gc = gspread.service_account_from_dict(credentials)
sht2 = gc.open_by_url('https://docs.google.com/spreadsheets/d/10kOz5eGToPogxndeAmXizvdGszqaD-Zin9mO5yoMNK0/edit?usp=sharing')
worksheet = sht2.get_worksheet(0)
list_of_dicts = worksheet.get_all_records()
    
    
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
            if fuente == "":
                st.write("El casillero esta vacio.")
            else:
                st.dataframe(df.loc[df['fuente'] == fuente])
        elif parametro == "Televisor":
            st.dataframe(df.loc[df['televisor'] == televisor])
        elif parametro == "Numero":
            if nro == 0:
                st.write("Elija un numero distinto de 0.")
            else:
                st.dataframe(df.loc[df['nro'] == nro])

def editar_page():
    df = pd.DataFrame(list_of_dicts)
    edited_df = st.data_editor(df, num_rows= "dynamic", hide_index=True)
    df = edited_df
    if st.button("Actualizar"):
        df.placa = df['televisor'].apply(lambda x: " " if pd.isnull(x) else x)
        df.televisor = df['televisor'].apply(lambda x: " " if pd.isnull(x) else x)
        df.nro = df['nro'].apply(lambda x: 0 if pd.isnull(x) else x)
        df.caja = df['caja'].apply(lambda x: 0 if pd.isnull(x) else x)
        worksheet.update([df.columns.values.tolist()] + df.values.tolist())
        st.rerun()
        
        
        

def main():
    
    st.title('Electronica Navarro')
    usuario()
    df = pd.DataFrame(list_of_dicts)
    st.subheader('Tabla de stocks')
    st.dataframe(df, hide_index=True)
    
    


if __name__ == "__main__":
    
    main()



    
    
    
