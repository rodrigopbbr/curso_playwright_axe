from playwright.sync_api import Page


class ConfirmacaoPage:
    def __init__(self, page: Page):
        self.page = page

    def numero_pedido(self):
        return self.page.get_by_test_id("confirmacao-numero-pedido").inner_text()
