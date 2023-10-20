from ssl import Options
import streamlit as st
import pandas as pd
from views import Views

class ManterClienteUI:
    def main():
        st.header("Cadastro de Clientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterClienteUI.Cliente_Listar()
        with tab2:
            ManterClienteUI.Cliente_Inserir()
        with tab3:
            ManterClienteUI.Cliente_Atualizar()
        with tab4:
            ManterClienteUI.Cliente_Excluir()

    def Cliente_Listar():
        clientes = Views.cliente_listar()
        dic = []
        for c in clientes:
            dic.append(c.__dict__)
        df = pd.DataFrame(dic)
        st.dataframe(df)

    def Cliente_Inserir():
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")
        if st.button("Inserir"):
            Views.cliente_inserir(nome, email, fone)

    def Cliente_Atualizar():
        option = st.selectbox(
            'Atualização de Clientes',
            (Views.cliente_listar()))

        st.write('Você selecionou:', option)
        nome = st.text_input("Informe o novo nome")
        email = st.text_input("Informe o novo e-mail")
        fone = st.text_input("Informe o novo fone")
        if st.button("Atualizar"):
            Views.cliente_atualizar(option.get_id(), nome, email, fone)

    def Cliente_Excluir():
        option = st.selectbox(
            'Exclusão de Clientes',
            (Views.cliente_listar()))

        st.write('Você selecionou:', option)
        if st.button("Excluir"):
            Views.cliente_excluir(option.get_id())