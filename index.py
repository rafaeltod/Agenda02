from templates.manterclienteui import ManterClienteUI
from templates.manterservicoui import ManterServicoUI
from templates.manteragendaui import ManterAgendaUI
from templates.abriragendaui import AbrirAgendaUI
import streamlit as st

class IndexUI:
  def sidebar():
      op = st.sidebar.selectbox("Menu", ["Manter Clientes", "Manter Serviços", "Manter Agenda", "Abrir Agenda"])
      if op == "Manter Clientes": ManterClienteUI.main()
      if op == "Manter Serviços": ManterServicoUI.main()
      if op == "Manter Agenda": ManterAgendaUI.main()
      if op == "Abrir Agenda": AbrirAgendaUI.main()

  def main():
    IndexUI.sidebar()


IndexUI.main()