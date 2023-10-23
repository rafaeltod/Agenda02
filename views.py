from cliente import Cliente, NCliente
from servico import Servico, NServico
from agenda import Agenda, NAgenda
from datetime import datetime

class Views:

  @classmethod
  def cliente_inserir(cls, nome, email, fone):
    cliente = Cliente(0, nome, email, fone)
    NCliente.inserir(cliente)

  @classmethod
  def cliente_listar(cls):
    return NCliente.listar()

  @classmethod
  def cliente_atualizar(cls, id, nome, email, fone):
    cliente = Cliente(id, nome, email, fone)
    NCliente.atualizar(cliente)

  @classmethod
  def cliente_excluir(cls, id):
    cliente = Cliente(id, "", "", "")
    NCliente.excluir(cliente)

  @classmethod
  def servico_inserir(cls, descricao, valor, duracao):
    servico = Servico(0, descricao, valor, duracao)
    NServico.inserir(servico)

  @classmethod
  def servico_listar(cls):
    return NServico.listar()

  @classmethod
  def servico_atualizar(cls, id, descricao, valor, duracao):
    servico = Cliente(id, descricao, valor, duracao)
    NServico.atualizar(servico)

  @classmethod
  def servico_excluir(cls, id):
    servico = Servico(id, "", "", "")
    NServico.excluir(servico)

  @classmethod
  def agenda_inserir(cls, data):
    agenda = Agenda(0, data, False, 0, 0)
    NAgenda.inserir(agenda)

  @classmethod
  def agenda_listar(cls):
    return NAgenda.listar()

  @classmethod
  def agenda_atualizar(cls, id, data):
    agenda = Cliente(id, data, False, 0, 0)
    NAgenda.atualizar(agenda)

  @classmethod
  def agenda_excluir(cls, id):
    agenda = Agenda(id, "", "", "", "")
    NAgenda.excluir(agenda)

  @classmethod
  def agenda_abrir_agenda_do_dia(cls, data, hinicio, hfim, intervalo):
    data_inicio = datetime.strptime(f"{data.strftime('%d/%m/%Y')} {hinicio.strftime('%H %M')}", "%d/%m/%Y %H %M")
    data_fim = datetime.strptime(f"{data.strftime('%d/%m/%Y')} {hfim.strftime('%H %M')}", "%d/%m/%Y %H %M")
    delta = intervalo
    aux = data_inicio
    while aux <= data_fim:
      NAgenda.inserir(Agenda(0, aux, False, 0, 0))
      aux += delta