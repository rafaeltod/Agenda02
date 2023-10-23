import streamlit as st
from views import Views
from datetime import datetime
from datetime import timedelta

class AbrirAgendaUI:
    def main():
        st.header("Abrir Agenda do Dia")
        AbrirAgendaUI.AbrirAgenda()

    def AbrirAgenda():
        data = st.text_input("Informe a data no formato dd/mm/aaaa")
        hinicio = st.text_input("Informe o horário inicial no formato HH MM")
        hfim = st.text_input("Informe o horário final no formato HH MM")
        intervalo = st.text_input("Informe o intervalo entre os horários (min)")
        if st.button("Inserir Horários"):
            data = datetime.strptime(data, "%d/%m/%Y")
            hinicio = datetime.strptime(hinicio, "%H:%M")
            hfim = datetime.strptime(hfim, "%H:%M")
            intervalo = timedelta(minutes=int(intervalo))
            Views.agenda_abrir_agenda_do_dia(data, hinicio, hfim, intervalo)


AbrirAgendaUI.main()