
from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
  
  """Representa um restaurante e suas características."""
  
  restaurantes = []
  
  def __init__(self, nome, categoria):
    
    """
        Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        """
        
    self._nome = nome.title()
    self.categoria = categoria.upper()
    self._ativo = False
    self._avaliacao = []
    self._cardapio = []
    Restaurante.restaurantes.append(self)
    
  def __str__(self):
    """Retorna uma representação em string do restaurante."""

    return f'{self._nome} | {self.categoria}'
  
  @classmethod
  def listar_restaurantes(cls):
    
    """Exibe uma lista formatada de todos os restaurantes."""
    
    print(f'{'nome do Restaurante'.ljust(25)} | {'categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
    for restaurante in cls.restaurantes:
      print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')
      
      
  @property
  def ativo(self):
      return 'verdadeiro 😃' if self._ativo else 'false 😟'
      
  def alternar_estado(self):
      self._ativo = not self._ativo
      
  def receber_avaliacao(self, cliente, nota):
      if 0 < nota <= 5:
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
      
  @property
  def media_avaliacoes(self):
      if not self._avaliacao:
          return '-' 
      soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
      quantidade_de_notas = len(self._avaliacao)
      media = round(soma_das_notas / quantidade_de_notas, 1)
      return media
      
  def adicionar_no_cardapeio(self,item):
      if isinstance(item,ItemCardapio):
          self._cardapio.append(item)
  @property       
  def exibir_cardapio(self):
      print(f'cardapio do restaurante {self._nome}\n')
      for i,item in enumerate(self._cardapio,start=1):
          if hasattr(item,'descricao'):
             mensagem_prato = f'{i}. Nome:{item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}'
             print(mensagem_prato)
          else:
            menssagem_bebida = f'{i}. Nome:{item._nome} | Preço: R${item._preco} |  Tamnho: {item.tamanho}'
            print(menssagem_bebida)
