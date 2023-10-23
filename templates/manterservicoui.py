import streamlit as st
import pandas as pd
from views import Views

class ManterServicoUI:
    def main():
        st.header("Cadastro de Serviços")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterServicoUI.Servico_Listar()
        with tab2:
            ManterServicoUI.Servico_Inserir()
        with tab3:
            ManterServicoUI.Servico_Atualizar()
        with tab4:
            ManterServicoUI.Servico_Excluir()

    def Servico_Listar():
        Servicos = Views.servico_listar()
        dic = []
        for s in Servicos:
            dic.append(s.__dict__)
        df = pd.DataFrame(dic)
        st.dataframe(df)

    def Servico_Inserir():
        descricao = st.text_input("Informe o descricao")
        valor = st.text_input("Informe o valor")
        duracao = st.text_input("Informe o duracao")
        if st.button("Inserir"):
            Views.servico_inserir(descricao, valor, duracao)

    def Servico_Atualizar():
        option = st.selectbox(
            'Atualização de Servicos',
            (Views.servico_listar()))

        st.write('Você selecionou:', option)
        descricao = st.text_input("Informe o novo descricao")
        valor = st.text_input("Informe o novo valor")
        duracao = st.text_input("Informe o novo duracao")
        if st.button("Atualizar"):
            Views.servico_atualizar(option.get_id(), descricao, valor, duracao)

    def Servico_Excluir():
        option = st.selectbox(
            'Exclusão de Servicos',
            (Views.servico_listar()))

        st.write('Você selecionou:', option)
        if st.button("Excluir"):
            Views.servico_excluir(option.get_id())