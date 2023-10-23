<<<<<<< HEAD
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
=======
import streamlit as st

st.set_page_config(
    page_title="Streamlit PEOO",
    page_icon="🤓",
)

st.title("Página Inicial")
st.write("Seja bem-vindo ao Streamlit PEOO de Rafael Ricco!")
st.write("😎😋😎")
st.sidebar.success("Selecione uma página abaixo")
>>>>>>> 344575bc3c6153c093aa100b41a649fa6be0ac06
