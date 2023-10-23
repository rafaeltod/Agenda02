import streamlit as st
import pandas as pd
from views import Views
from datetime import datetime

class ManterAgendaUI:
    def main():
        st.header("Cadastro de Agendas")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterAgendaUI.Agenda_Listar()
        with tab2:
            ManterAgendaUI.Agenda_Inserir()
        with tab3:
            ManterAgendaUI.Agenda_Atualizar()
        with tab4:
            ManterAgendaUI.Agenda_Excluir()

    def Agenda_Listar():
        Agendas = Views.agenda_listar()
        dic = []
        for s in Agendas:
            dic.append(s.__dict__)
        df = pd.DataFrame(dic)
        st.dataframe(df)

    def Agenda_Inserir():
        data = st.text_input("Informe a data no formato dd/mm/aaaa HH MM")
        if st.button("Inserir"):
            data = datetime.strptime(data, "%d/%m/%Y %H:%M")
            Views.agenda_inserir(data)

    def Agenda_Atualizar():
        option = st.selectbox(
            'Atualização de Agendas',
            (Views.agenda_listar()))

        st.write('Você selecionou:', option)
        data = st.text_input("Informe a nova data no formato dd/mm/aaaa HH MM ")
        if st.button("Atualizar"):
            data = datetime.strptime(data, "%d/%m/%Y %H:%M")
            Views.agenda_atualizar(option.get_id(), data)

    def Agenda_Excluir():
        option = st.selectbox(
            'Exclusão de Agendas',
            (Views.agenda_listar()))

        st.write('Você selecionou:', option)
        if st.button("Excluir"):
            Views.agenda_excluir(option.get_id())