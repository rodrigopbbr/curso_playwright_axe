from pytest_playwright_axe import Axe
from helpers import assert_sem_violacoes_graves
from pages.produto_detalhe_page import ProdutoDetalhePage
from pages.carrinho_page import CarrinhoPage


def test_a11y_carrinho(logado):
    produto = ProdutoDetalhePage(logado)
    produto.acessar('p1')
    produto.adicionar_ao_carrinho('p1')

    carrinho = CarrinhoPage(logado)
    carrinho.acessar()

    resultado = Axe().run(logado)
    assert_sem_violacoes_graves(resultado)
